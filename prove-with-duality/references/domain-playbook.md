# Dual bounds, equality and attainment

## Method branches
1. For finite linear programs, write one consistent primal convention and derive dual constraints from the Lagrangian. Weak duality follows for every feasible pair. Invoke strong duality only when its feasibility and finite-value hypotheses are met, and distinguish infeasibility from unboundedness.
2. For convex inequality-constrained problems, check convexity, affine equality constraints and an appropriate constraint qualification such as a strictly feasible point in the relevant domain. Slater conditions justify specific strong-duality conclusions; they do not license arbitrary nonconvex KKT certificates.
3. For norm or functional duality, specify the ambient space, continuous dual and pairing. In infinite dimensions topology controls closure, separation and attainment. An algebraic dual may answer a different question from the continuous dual.
4. For a proposed certificate, verify primal feasibility, dual feasibility and equality of objective values directly. Equality plus weak duality establishes optimality without numerical claims about solver success.

## Worked calculation
Minimize x over real x subject to x≥2. Write g(x)=2-x≤0. L(x,λ)=x+λ(2-x) for λ≥0. The infimum over x is finite only at λ=1, where it equals 2. The primal feasible x=2 and dual feasible λ=1 have equal values, proving both optimality and attainment. This also checks the dual inequality direction explicitly.

## Tempting inference and counterexample
Stationarity is not a global certificate for a nonconvex objective. For minimizing f(x)=-x² on [-1,1], x=0 is an interior stationary point with derivative zero, but f(0)=0 exceeds f(1)=-1. KKT necessity under a suitable qualification must not be presented as sufficiency without the required convex structure.

## Stop and handoff
If a dual value is computed but feasibility is unverified, label it a candidate rather than a bound. Pass the pairing, sign convention, exact constraint qualification, feasible witnesses and unresolved closure or attainment issues to proof review. Report infimum/supremum separately from optimizer existence and arithmetic uncertainty separately from the mathematical duality gap.
