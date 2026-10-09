# Domain playbook: research-dynamical-systems

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For autonomous C¹ flows, compute equilibria and linearization; eigenvalues strictly in the left half-plane give local asymptotic stability, while a positive real part gives instability. Zero or purely imaginary eigenvalues require nonlinear information rather than a verdict from the Jacobian alone.
2. For maps, use eigenvalue moduli instead of real parts. Verify the map and invariant domain explicitly; continuous-time and discrete-time tests cannot be interchanged.
3. For nonlinear global claims choose a coercive Lyapunov function or a trapping region. LaSalle's method needs a positively invariant compact set and asks for the largest invariant subset of {V'=0}; vanishing dissipation at isolated observed points does not imply attraction of the whole zero set.

## Worked derivation

For x'=−x³, the origin has zero linearization. Take V=x²/2, so V'=−x⁴<0 for x≠0. Direct separation gives x(t)=x_0/(1+2x_0²t)^(1/2) for t≥0, preserving the sign and tending to zero. Thus the equilibrium is globally asymptotically stable but the displayed polynomial decay is not an exponential-stability proof.

## Invalid inference and witness

The identical zero Jacobian occurs for x'=x³, where x(t)=x_0/(1−2x_0²t)^(1/2) departs from any small neighborhood and blows up for nonzero x_0. A zero eigenvalue does not imply either stability or instability without nonlinear analysis.

## Stop and handoff

Return stability type, local or global domain, invariance and solution-existence interval. Separate observed irregular trajectories from chaos proofs. Hand off nonhyperbolic classification to center-manifold or bifurcation analysis with the decisive coefficients.
