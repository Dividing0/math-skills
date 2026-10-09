# Domain playbook

## Select the method

1. For explicit heat updates on a uniform one-dimensional mesh, derive the amplification factor or maximum-principle weights. The restriction r=κΔt/h²<=1/2 gives nonnegative three-point weights and the standard L2 stability condition; boundaries must be compatible with the analysis.
2. For implicit schemes, prove the operator or energy estimate for the actual discretization. Unconditional linear stability does not guarantee temporal accuracy, positivity for every method, or convergence of nonlinear solver iterations.
3. For hyperbolic conservation laws, check conservation, CFL, numerical flux and entropy selection. A converged discrete residual or a stable centered scheme cannot alone establish convergence to the intended weak solution.

## Worked check

For u_t=κu_xx, forward Euler gives U_j^{n+1}=rU_{j-1}^n+(1-2r)U_j^n+rU_{j+1}^n. With r=1/4 the weights are 1/4,1/2,1/4 and sum to one. On a periodic mesh each new value lies within the previous minimum and maximum, establishing an L-infinity bound by convexity.

## Invalid inference and witness

Small residual is not a small solution error without conditioning. For a scalar discrete equation εU=1, replacing the exact U=1/ε by U+1 changes the residual by only ε. Taking ε very small hides a unit forward error. A PDE residual needs a norm and inverse-operator stability estimate.

## Completion and handoff

Return continuous and discrete equations, boundary stencil, timestep, norms, consistency and stability assumptions, solver tolerance and observed refinement results. Stop if a nonlinear entropy or compactness obligation is missing. Hand implementation the stencil and failure criteria; hand analytic PDE work the exact solution notion, keeping experiments distinct from universal convergence guarantees.
