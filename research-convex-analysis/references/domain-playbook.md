# Convexity, subgradients and attainment

## Choose a branch
- Finite-dimensional existence: a proper lower-semicontinuous function with a nonempty bounded sublevel set has compact sublevels at the relevant height and attains its infimum there. Convexity alone does not supply boundedness or closedness.
- Subgradient optimality: for a proper convex f, define p in partial f(x) by f(y)>=f(x)+<p,y-x> for every y. Then 0 in partial f(x) characterizes global minimization. For differentiable convex f this reduces to gradient zero; nonsmooth functions require the set-valued condition.
- Constraints and duality: on a closed convex set C, write the normal cone and explicit constraint convention. Use sum rules only after their qualification hypotheses; in finite-dimensional convex inequalities, a feasible point strictly satisfying all inequality constraints is a common sufficient Slater condition, with affine equalities treated separately.

## Worked nonsmooth optimum
Let f(x)=|x|+x² on R. For x=0, every p in [-1,1] satisfies |y|+y²>=p*y; outside that interval the inequality fails for sufficiently small y of the matching sign. Thus partial f(0)=[-1,1], containing zero. Directly, f(x)>=0=f(0), and equality requires x=0, so the minimizer is unique. A derivative-based solver must account for the kink instead of inventing f'(0).

## Tempting inference and counterexample
Strict convexity does not guarantee attainment. f(x)=exp(x) is strictly convex and continuous on R, with infimum zero, but exp(x)>0 at every finite x. Values tend to zero only as x→-infinity. Neither uniqueness of a possible minimum nor a decreasing sequence establishes existence.

## Stop or hand off
In infinite-dimensional spaces, norm boundedness is not norm compactness; verify a weak compactness and weak lower-semicontinuity route separately. Pass the ambient topology, properness convention, domain, subgradient inequalities and qualification conditions to optimization. If only an infimum or dual bound is known, keep primal attainment and multiplier existence unresolved. Check whether a candidate lies in the effective domain before applying any stationarity criterion.
