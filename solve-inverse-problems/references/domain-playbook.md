# Recovery limited by the forward operator

## Method branches
1. For a finite linear model y=Ax+ε, inspect rank and singular values before selecting a solver. A null space means observational ambiguity; small nonzero singular values mean noise amplification. These are different obstacles requiring different reports.
2. For Tikhonov regularization, minimize ||Ax-y||²+α||Lx||² with α>0. Uniqueness follows if ker A∩ker L={0} in finite dimensions. Derive the normal equation (AᵀA+αLᵀL)x=Aᵀy and check invertibility rather than presuming it.
3. For truncated SVD, specify a threshold and explain omitted singular directions. Noise bounds and source assumptions govern accuracy; filtering creates bias even when the optimization problem is solved exactly.
4. For nonlinear inversion, examine the observation Jacobian locally, multiple initializations and global symmetries. Local nonsingularity can support local recovery but does not establish global uniqueness of a noninjective forward map.

## Worked calculation
Let A=diag(1,ε), y=(1,ε), and L=I. For α>0 the normal equations give x_α=(1/(1+α), ε²/(ε²+α)). Exact noiseless data correspond to x=(1,1), but regularization shrinks both components and suppresses the second strongly when ε²≪α. This explicit solution separates stabilizing the solve from faithfully recovering each feature.

## Tempting inference and counterexample
Zero residual does not prove uniqueness. For A=[1,1] and y=1, every vector (t,1-t) fits exactly. The minimum-Euclidean-norm fit is (1/2,1/2), selected by an additional criterion rather than by the observation itself. More numerical precision cannot identify the missing direction.

## Stop and handoff
Stop claims of true-signal recovery if the noise model, prior or observable modes are unspecified. Return a conditional reconstruction and resolvability statement. Pass operator scaling, singular/null directions, regularizer, strength-selection rule, residuals and noise perturbation tests to implementation. Cross-validation and discrepancy principles require their own sampling or noise assumptions; do not invent a noise bound just to justify a convenient parameter choice.
