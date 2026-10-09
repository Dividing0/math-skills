# Domain playbook: research-control-theory

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For finite-dimensional continuous-time LTI systems x'=Ax+Bu, test controllability using [B,AB,…,A^(n−1)B] or the PBH rank condition for each eigenvalue. Stabilizability only requires uncontrollable modes to lie in the open left half-plane; observability and detectability are distinct dual tests.
2. For state feedback u=−Kx, analyze the actual closed-loop matrix A−BK. Pole placement requires controllability for arbitrary poles; quadratic Lyapunov certification uses P≻0 and A_clᵀP+PA_cl≺0, with a declared state domain if constraints exist.
3. For sampled implementations calculate the actual update map, including hold and controller timing. Exact zero-order-hold discretization and explicit Euler have different matrices; require spectral radius below one for a discrete LTI stability claim and handle saturation as a nonlinear modification.

## Worked derivation

For A=[[0,1],[0,0]] and B=[0,1]ᵀ, [B,AB]=[[0,1],[1,0]] has full rank. With K=[2,3], A−BK=[[0,1],[−2,−3]], whose characteristic polynomial λ²+3λ+2=(λ+1)(λ+2) has negative roots. Thus the unconstrained continuous closed-loop origin is globally exponentially stable.

## Invalid inference and witness

Hurwitz A does not imply arbitrary Euler stability: x'=−x becomes x_(k+1)=(1−h)x_k. At h=3 the multiplier is −2, so nonzero states diverge despite stable continuous dynamics. The implementation must be included in the claim.

## Stop and handoff

Report the input and observation model, feedback sign, rank or eigenvalue evidence and sampling assumption. Stop before robustness claims when uncertainty bounds, delays or actuator limits are unspecified; pass those concrete missing data downstream.
