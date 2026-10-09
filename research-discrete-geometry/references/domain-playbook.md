# Domain playbook: research-discrete-geometry

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For finite point configurations, separate affine dimension from ambient dimension before using dimension-dependent theorems. For planar incidence counts, state which points or lines are distinct and whether collinearity, parallelism or concurrency is excluded. For convex-hull membership, exhibit convex coefficients; for separation, provide a linear functional and verify its inequalities on every point. For packing or covering, distinguish a feasible configuration from an upper bound and inspect boundary/periodicity assumptions before claiming optimality.

## Worked valid example

The point p=(1,1) lies in the triangle with vertices A=(0,0),B=(3,0),C=(0,3), because p=(1/3)A+(1/3)B+(1/3)C and the coefficients are nonnegative and sum to one. Conversely q=(2,2) is outside: the functional ℓ(x,y)=x+y has maximum three on the three vertices and therefore on every convex combination, but ℓ(q)=4. This gives exact membership and separation certificates.

## Tempting invalid inference

Counting intersection points as one per pair of lines fails under concurrency: three distinct lines through the origin have three pairs but only one distinct intersection. Pair counts measure incidences with multiplicity unless a nonconcurrency assumption is imposed.

## Stop and handoff

Return the configuration, degeneracy assumptions and the nature of the bound. If an abstract incidence pattern is supplied, realizability needs its own argument. Transfer algorithmic predicate issues to computational geometry and unproved extremal claims to counterexample search.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
