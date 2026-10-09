#!/usr/bin/env python3
"""Small executable independent-oracle check; ordinary Python required."""

if not __debug__:
    raise RuntimeError('Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE.')

import argparse,json,sys
parser=argparse.ArgumentParser(); parser.add_argument('--self-test',action='store_true'); args=parser.parse_args()
try:
    import numpy as np
    import cvxpy as cp
    b=np.array([2.,-1.]); x=cp.Variable(2)
    constraints=[x>=0, cp.sum(x)==1]
    p=cp.Problem(cp.Minimize(cp.sum_squares(x-b)),constraints)
    assert p.is_dcp()
    solvers=cp.installed_solvers(); solver=next((s for s in ['CLARABEL','OSQP','SCS'] if s in solvers),None)
    if solver is None: raise RuntimeError('No compatible installed solver')
    options={'tol_gap_abs':1e-9,'tol_feas':1e-9} if solver=='CLARABEL' else ({'eps_abs':1e-9,'eps_rel':1e-9} if solver=='OSQP' else {'eps':1e-7})
    p.solve(solver=solver,**options)
    assert p.status==cp.OPTIMAL, p.status
    v=np.asarray(x.value); objective=float(np.sum((v-b)**2))
    assert np.max(np.abs(v-[1.,0.]))<1e-5
    assert abs(v.sum()-1)<1e-7 and v.min()>-1e-7 and abs(objective-2)<1e-5
    bad=cp.Problem(cp.Minimize(cp.sum_squares(x)),[x[0]>=2,x[0]<=1]); bad.solve(solver=solver,**options)
    assert bad.status==cp.INFEASIBLE and x.value is None
    import importlib.metadata
    result={'cvxpy':cp.__version__,'solver':solver,'solver_version':importlib.metadata.version(solver.lower()),'solver_options':options,'solver_status':p.status,'x':v.tolist(),'objective_recomputed':objective,'max_constraint_violation':float(max(max(0,-v.min()),abs(v.sum()-1))),'infeasible_status':bad.status,'evidence':'numerical; not a rigorous optimality certificate'}
except ModuleNotFoundError as exc:
    print(json.dumps({'status':'dependency-unavailable','dependency':exc.name})); sys.exit(2)
print(json.dumps({'status':'passed','self_test':args.self_test,**result},allow_nan=False))
