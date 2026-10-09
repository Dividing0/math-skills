# Experiments that distinguish specified claims

## Method branches
1. For linear parameter estimation y=Xθ+ε with known independent homoscedastic errors, inspect rank(X) before optimizing a criterion. D-optimality maximizes det(XᵀX), while A-optimality minimizes trace((XᵀX)⁻¹) when the matrix is invertible. Declare parameter scaling. A-optimal rankings generally change under scaling. Under one fixed nonsingular linear reparameterization θ=Cη used for every candidate design, the information matrix becomes CᵀMC and det(CᵀMC)=det(C)²det(M), so D-optimal rankings remain unchanged although determinant values scale. This invariance does not cover design-dependent transformations.
2. For competing deterministic models, choose feasible inputs where predictions separate relative to observational uncertainty. Require a prespecified discrimination rule; a large prediction difference is unhelpful if both models can freely recalibrate to match it.
3. For nonlinear models, use local Fisher-information design only after identifying a nominal parameter and regular likelihood. Check robustness across plausible parameters and distinguish local rank from global identifiability.
4. For causal questions, explicitly define treatment assignment, interference and outcome timing. Randomization can address confounding under a stated assignment mechanism; an observational parameter-fit experiment supplies a different form of evidence.

## Worked calculation
For y(t)=a+bt+ε, measurements at t=0 and t=1 give X=[[1,0],[1,1]]. Its determinant is 1, so the noiseless data determine a=y(0) and b=y(1)-y(0). Independent noise variance σ² yields Var(b-hat)=2σ². This calculation explains why distinct times identify the slope while also exposing noise amplification through subtraction.

## Tempting inference and counterexample
The largest response is not automatically the most discriminating experiment. Models m₁(t)=t and m₂(t)=t+1 have a constant prediction gap, although both responses increase with t. Choosing a large t solely because its response is large does not increase their separation.

## Stop and handoff
Stop before recommending an optimal design if feasible interventions, costs or noise structure are absent. Return candidate designs conditionally and name the missing choices. Pass design matrices, nominal parameters, feasible measurement times, budget, replication rules and held-out confirmation criteria to implementation. Keep exploratory model selection separate from the data subsequently used to claim confirmation.
