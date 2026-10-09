# Domain playbook: research-optimal-control

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For linear dynamics with quadratic cost and a finite horizon, specify control space and endpoint conditions; convexity can turn an explicit variational inequality into global optimality, while existence still requires feasibility and compactness/coercivity arguments. For the Pontryagin principle, state the Hamiltonian sign convention, cost multiplier, transversality and control constraints; the conditions are generally necessary. For dynamic programming, define the value function and admissible concatenation; classical HJB verification needs sufficient regularity, while nonsmooth problems require a suitable viscosity framework. For bounded bang-bang controls, inspect singular arcs separately.

## Worked valid example

Minimize J(u)=∫₀¹u(t)²dt over u∈L²[0,1], with x'=u, x(0)=0,x(1)=2. The endpoint condition gives ∫₀¹u=2. Cauchy–Schwarz yields 4=(∫u)²≤∫u², so J≥4. The constant control u=2 is feasible and attains four; equality forces u constant almost everywhere, proving uniqueness in L². This is a global sufficiency argument, not merely a stationary-control calculation.

## Tempting invalid inference

Stationarity alone can select a maximum: with x'=u,x(0)=0, no terminal constraint, |u|≤1 and cost J=-∫₀¹u²dt, the feasible control u=0 is stationary under first variations but has cost zero. The feasible u=1 has cost -1 and is better. A first-order candidate needs a separate optimality argument.

## Stop and handoff

Return dynamics, horizon, admissible function space and feasible trajectory, with necessary/sufficient conclusions separated. Stop when endpoint or state constraints are infeasible; hand PDE verification, numerical discretization or uncertain model parameters to their dedicated skills.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
