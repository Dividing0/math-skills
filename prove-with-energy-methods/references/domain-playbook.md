# Domain playbook: prove-with-energy-methods

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For smooth ODEs, choose a coercive Lyapunov or energy function and compute its derivative exactly. Negative semidefinite derivative bounds energy; asymptotic decay requires a stronger estimate or an invariance argument and its compactness hypotheses.
2. For PDEs, state the test function and solution space before integrating by parts. Check traces and boundary conditions; weak solutions require a justified approximation or weak formulation instead of differentiating unavailable classical quantities.
3. For forced estimates of the form E'≤aE+b, integrate the differential inequality or apply Gronwall on the specified time interval. For uniqueness, estimate the difference of two solutions in a controlled norm, with coefficients integrable in time; an individual solution bound alone does not prove uniqueness.

## Worked derivation

For u_t=u_xx on (0,L) with u=0 at both ends, let E=½∫u²dx for a smooth solution. Integration by parts yields E'=∫u u_xx dx=−∫u_x²dx. Poincaré's inequality ∫u²≤(L/π)²∫u_x² gives E'≤−2(π/L)²E, hence E(t)≤E(0)e^(−2(π/L)²t). The endpoint term vanishes because of the Dirichlet traces.

## Invalid inference and witness

Bounded L² energy does not bound derivatives: on (0,2π), u_n(x)=sin(nx) has ∫u_n²=π while ∫(u_n')²=πn². Claiming smoothness from a uniform L² bound skips the norm needed to control gradients.

## Stop and handoff

Return the energy identity or inequality, boundary contributions, coercivity constants and controlled norm. Stop at an a priori estimate when existence or regularity is unproved; hand off compactness, approximation and passage-to-limit obligations explicitly.
