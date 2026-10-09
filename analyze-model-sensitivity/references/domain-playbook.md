# Sensitivity with an explicit perturbation model

## Method branches
1. Use a local Jacobian when the output map is differentiable on an open neighborhood of the baseline. Report physical units and the norm of admissible perturbations. A derivative at one parameter is a local statement; validate finite perturbations by recomputing the forward model.
2. Use adjoints for a scalar objective with many parameters when the state equation is differentiable and its linearized state operator is invertible. Derive the transpose system rather than importing a sign convention. Compare one directional derivative with an independently computed centered difference over several step sizes.
3. Use classical variance-based Sobol decomposition for square-integrable outputs with mutually independent inputs and nonzero output variance. For dependent inputs specify a joint distribution and a dependence-aware attribution convention; different conventions answer different questions.
4. For nondifferentiable switches, active-set changes or threshold events, use one-sided perturbations and region-specific analysis. Do not average opposite slopes into a nonexistent derivative.

## Worked calculation
For y(a,b)=ab at (2,3), the gradient is (3,2). Thus perturbations (h,k) change y by 3h+2k+hk. The omitted term is exactly hk, so the linear approximation can be bounded on a declared rectangle. The normalized elasticities are a(∂y/∂a)/y=1 and b(∂y/∂b)/y=1. Equal elasticities do not mean equal absolute sensitivities, and neither quantity identifies the two factors from their product.

## Tempting inference and counterexample
A zero first derivative does not imply insensitivity over a finite range. For y(a)=a² at a=0, y'(0)=0 but y(h)-y(0)=h². Normalizing by y(0) is undefined rather than evidence of perfect robustness.

## Stop and handoff
Stop before assigning variance shares if the input law or dependence is unspecified. Pass the output definition, baseline, units, perturbation region, Jacobian or adjoint convention, solver tolerance and unverified derivative checks to uncertainty propagation. For identification questions pass the full observation Jacobian and null directions to identifiability analysis; a sensitivity ranking alone cannot decide whether parameters are recoverable.
