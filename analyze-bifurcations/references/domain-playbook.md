# Domain playbook: analyze-bifurcations

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For a scalar saddle-node candidate f(x,μ)=0 require C² regularity, f=f_x=0 and f_μ f_xx≠0 at the critical point. Taylor expansion then separates parameter displacement and quadratic state displacement; solve branches and test f_x signs.
2. For a transcritical or pitchfork candidate, first identify an existing equilibrium branch and symmetry or invariant factor. A vanishing eigenvalue alone does not select a normal form; expand nonlinear coefficients and check their first nonzero order.
3. For Hopf analysis require a simple conjugate pair crossing the imaginary axis with nonzero crossing speed, no other imaginary eigenvalues, and the needed smoothness. Require a nonzero first Lyapunov coefficient before generic supercritical/subcritical Hopf classification; a zero coefficient requires higher-order analysis and a degenerate-candidate handoff. Compute the coefficient using a declared normal-form sign convention. Numerical continuation proposes branches but does not discharge these conditions.

## Worked derivation

For x'=μ−x², equilibria are ±√μ when μ≥0. At (0,0), f_μ=1 and f_xx=−2, so the scalar saddle-node conditions hold. For μ>0, f_x(√μ)=−2√μ<0 and f_x(−√μ)>0: the positive equilibrium attracts locally and the negative one repels. At μ<0 there are no equilibria. These statements describe the local branches, not all trajectories for all time.

## Invalid inference and witness

The equation x'=μx−x³ also has a zero eigenvalue at (0,0), but equilibria x=0 persist for every μ and two additional branches ±√μ appear for μ>0. Calling this a saddle-node loses the persistent branch and symmetry; it is the standard supercritical pitchfork.

## Stop and handoff

Stop at a candidate classification when coefficients, crossing conditions or center-manifold hypotheses remain unverified. Pass the exact derivatives, parameter direction and branch domain to proof or validated-continuation work.
