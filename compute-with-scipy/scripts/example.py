"""Independent analytic checks for ODE, quadrature, root and sparse solve."""

if not __debug__:
    raise RuntimeError('Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE.')

import argparse,json,math,sys
try:
 import numpy as np
 import scipy
 from scipy.integrate import solve_ivp,quad
 from scipy.optimize import brentq
 from scipy.sparse import csr_matrix
 from scipy.sparse.linalg import cg
except ImportError:sys.exit('dependency_unavailable: numpy/scipy; use the declared Python environment')

def example():
    times=np.linspace(0,1,11)
    sol=solve_ivp(lambda t,y:-2*y,(0,1),[1.],t_eval=times,rtol=1e-10,atol=1e-12)
    assert sol.success and sol.t[-1]==1
    ode_error=float(np.max(np.abs(sol.y[0]-np.exp(-2*times))));assert ode_error<1e-8
    integral,estimated_error=quad(lambda x:math.exp(-x),0,1,epsabs=1e-11,epsrel=1e-11)
    integral_error=abs(integral-(1-math.exp(-1)));assert integral_error<1e-10
    root=brentq(lambda x:x*x-2,1,2,xtol=1e-12);assert abs(root-math.sqrt(2))<1e-10
    A=csr_matrix([[4.,1.],[1.,3.]]);b=np.array([1.,2.]);x,info=cg(A,b,rtol=1e-12,atol=0.)
    assert info==0 and np.max(np.abs(x-np.array([1/11,7/11])))<1e-10
    _,limited_info=cg(A,b,rtol=1e-15,atol=0.,maxiter=1);assert limited_info>0
    bracket_rejected=False
    try:brentq(lambda x:x*x+1,-1,1)
    except ValueError:bracket_rejected=True
    assert bracket_rejected
    return {'library':'scipy','version':scipy.__version__,'classification':'approximate_numeric',
            'ode_error_against_analytic':ode_error,'quadrature_value':integral,'quadrature_estimated_error':estimated_error,
            'quadrature_forward_error':integral_error,'quadrature_estimate_is_rigorous_bound':False,
            'root':root,'cg_solution':x.tolist(),'cg_info':int(info),'limited_cg_info':int(limited_info),
            'invalid_root_bracket_rejected':bracket_rejected,
            'checks':['ODE_analytic_oracle','quadrature_analytic_oracle','root_analytic_oracle','sparse_analytic_oracle','iteration_failure','invalid_bracket']}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--self-test',action='store_true');parser.parse_args()
    print(json.dumps(example(),indent=2))
