# Feasible plans, map constraints and dual witnesses

## Method branches
1. For a finite transport problem, specify nonnegative marginals with equal total mass and costs cᵢⱼ. Feasible plans π have row and column sums equal to the marginals. Exact marginal checks are required before interpreting a numerical objective.
2. For a discrete dual, choose potentials uᵢ,vⱼ satisfying uᵢ+vⱼ≤cᵢⱼ. Every feasible pair gives a lower bound. Equality of primal and dual objectives certifies optimality through weak duality; solver termination alone does not.
3. For a Monge map, require pushforward equality and account for indivisible source atoms. A plan may split mass, while a deterministic map cannot split one atom. Map-existence theorems require their actual measure and cost hypotheses.
4. For continuous transport, specify spaces, lower-semicontinuity of the cost and moment/integrability requirements of the chosen theorem. Distinguish optimal-plan existence, dual attainment and regularity of an optimal map.

## Worked calculation
Let both marginals on two labels equal (1/2,1/2), and costs be [[0,1],[1,0]]. The plan with diagonal entries 1/2 and off-diagonal zero has the required marginals and cost zero. Potentials u=v=0 are dual feasible and also have value zero. Weak duality proves optimality exactly. This example separates feasibility, value calculation and certification.

## Tempting inference and counterexample
Equal total mass alone does not ensure finite transport cost. On R, take μ=δ₀ and ν a Cauchy distribution with cost |x-y|. Every feasible plan must pair 0 with a Cauchy variable, whose absolute first moment is infinite. A coupling exists, but its objective is infinite; claims about finite Wasserstein distance need moment assumptions.

## Stop and handoff
Stop before presenting an entropically regularized value as the original optimal transport cost. Pass marginals, cost matrix or cost function, plan residuals, dual potentials and regularization convention to numerical optimization. Declare whether reported errors arise from discretization, regularization or arithmetic. For maps, pass atomic structure and unresolved pushforward or regularity obligations rather than inferring a map from a feasible plan.
