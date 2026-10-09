#!/usr/bin/env python3
"""Tiny NUTS smoke run against a conjugate benchmark, not certification."""

if not __debug__:
    raise RuntimeError('Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE.')

import argparse,json,sys,platform,math
p=argparse.ArgumentParser();p.add_argument('--self-test',action='store_true');args=p.parse_args()
try:
 import numpy as np
 import pymc as pm
 import arviz as az
 import pytensor
except ImportError as exc:
 print(json.dumps({'status':'dependency_missing','dependency':'numpy/pymc/arviz','error':str(exc)}),file=sys.stderr);sys.exit(2)
# Portable smoke backend: avoid relying on Python shared-library headers/linker.
# This is explicit and recorded; production jobs may select a compiled backend.
pytensor.config.cxx=''
a,b,successes,n=2,3,6,10
post_a,post_b=a+successes,b+n-successes
exact_mean=post_a/(post_a+post_b)
exact_variance=post_a*post_b/((post_a+post_b)**2*(post_a+post_b+1))
with pm.Model() as model:
 probability=pm.Beta('probability',alpha=a,beta=b)
 observed=pm.Binomial('observed',n=n,p=probability,observed=successes)
 step=pm.NUTS(target_accept=0.9)
 idata=pm.sample(draws=500,tune=500,chains=2,cores=1,random_seed=20261008,step=step,progressbar=False,return_inferencedata=True,compute_convergence_checks=True)
values=np.asarray(idata.posterior['probability'])
assert values.shape==(2,500) and np.isfinite(values).all() and ((values>0)&(values<1)).all()
mean=float(values.mean());variance=float(values.var())
assert abs(mean-exact_mean)<0.06, 'smoke mean differs from conjugate benchmark'
assert abs(variance-exact_variance)<0.012, 'smoke variance differs from conjugate benchmark'
diagnostics={
 'rhat':float(az.rhat(idata)['probability']),
 'ess_bulk':float(az.ess(idata,method='bulk')['probability']),
 'ess_tail':float(az.ess(idata,method='tail')['probability']),
 'mcse_mean':float(az.mcse(idata,method='mean')['probability']),
 'divergences':int(idata.sample_stats['diverging'].sum())}
assert all(math.isfinite(float(v)) for v in diagnostics.values())
checks=['posterior_support','conjugate_mean_smoke_tolerance','conjugate_variance_smoke_tolerance','finite_diagnostics']
if args.self_test:
 assert post_a==8 and post_b==7 and abs(exact_mean-8/15)<1e-15
 assert abs(exact_variance-56/(225*16))<1e-15
 checks.append('independent_conjugate_formula')
print(json.dumps({'status':'passed','claim_status':'monte_carlo_smoke_only','python':platform.python_version(),'pymc':pm.__version__,'pytensor':pytensor.__version__,'backend':'pytensor_python_cxx_disabled','arviz':az.__version__,'draws_per_chain':500,'tune_per_chain':500,'chains':2,'posterior_beta':[post_a,post_b],'analytic_mean':exact_mean,'analytic_variance':exact_variance,'sample_mean':mean,'sample_variance':variance,'diagnostics':diagnostics,'checks':checks,'limitation':'Loose smoke checks are not a convergence certificate or general-model validation.'}))
