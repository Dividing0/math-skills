# Domain playbook: research-optimization-theory

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For convex differentiable unconstrained objectives, stationarity is sufficient for global minimality; strict convexity gives at most one minimizer but does not ensure existence. For existence check compact feasible sets with continuity or coercivity plus lower semicontinuity in finite dimensions.
2. For constrained smooth problems distinguish necessary KKT conditions from sufficient ones. Verify a constraint qualification for necessity; convex objective and inequalities plus affine equalities make feasible KKT certificates sufficient, and Slater-type hypotheses can justify strong duality under the appropriate setting.
3. For nonconvex problems use Hessian information only locally and search for global bounds separately. Positive-definite Hessian at a stationary point gives a strict local minimum; positive semidefiniteness is inconclusive. A solver's stopping condition is numerical evidence until feasibility and a bound gap are established.

## Worked derivation

Minimize x² subject to x≥1. Write g(x)=1−x≤0 and L=x²+λ(1−x). At x=1, λ=2 satisfies stationarity 2x−λ=0, nonnegative multiplier, feasibility and complementary slackness. Convexity gives global optimality. Equivalently every feasible x has x²≥1; the primal value 1 matches the dual value L(1,2)=1.

## Invalid inference and witness

For f(x)=x³, x=0 is stationary and f''(0)=0, but it is not a local minimum: f(−δ)<f(0)<f(δ). For f(x)=e^x, strict convexity likewise does not imply a minimizer on R: its infimum zero is not attained.

## Stop and handoff

Return feasible domain, attainment status, qualification checks and certificate strength. Hand off missing global lower bounds or unverified constraints. In infinite-dimensional spaces do not import finite-dimensional compactness; require the relevant weak compactness and semicontinuity.
