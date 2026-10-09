# Solvers with an explicit mathematical target

Separate a root, minimizer, quadrature value, trajectory and linear-system solve before choosing an API. Choose `brentq` for a continuous scalar function on a supplied sign-changing interval; a returned zero is interval-scoped and needs a monotonicity or other argument for uniqueness. `minimize` can be useful for candidate optimization, but KKT or solver status alone does not establish global optimality of an arbitrary nonlinear objective.

For ODE initial values, `solve_ivp` takes an RHS returning the state shape and a one-dimensional initial state. Stiffness can invalidate an otherwise plausible explicit-step choice. Its rtol/atol control local estimates; compare the returned trajectory to an analytic solution or a refined solve when evaluating empirical accuracy. An event can terminate successfully before the requested final time; report the event and fulfilled scope explicitly.

The executable example checks four distinct references. For y'=-2y, y(0)=1, the exact trajectory is exp(-2t). For integral exp(-x) from zero to one, the exact value is 1-exp(-1). For x²-2 on [1,2], the positive root is sqrt(2). For [[4,1],[1,3]]x=[1,2], elimination gives (1/11,7/11). These references are not obtained by calling a second implementation of the same SciPy routine.

The script additionally forces CG to stop after one iteration and verifies nonconvergence info, and verifies rejection of an invalid sign-change bracket for x²+1. Do not manufacture a root from that rejection or infer that all functions with same-sign endpoints have no roots. A missing bracket is inconclusive in general.

Input handoff: model equations, initial/boundary conditions, operator properties, domain, tolerance and desired evidence. Output: executed source, versions, solver statuses, evaluation/iteration counts where relevant, residuals, reference/refinement comparisons and interpretation. A quadrature error estimate or small ODE residual is approximate evidence; certify-with-python-flint or a theorem-backed exact certificate must justify a stronger claim.

Primary APIs checked 2026-10-08: solve_ivp https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html; cg https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html; brentq https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.brentq.html; quad https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html.
