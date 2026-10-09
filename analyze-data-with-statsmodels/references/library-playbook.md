# Library playbook

## API selection
`sm.add_constant`, `sm.OLS(..., missing="raise").fit(cov_type="HC3")`, `params`, `resid`, `conf_int`; consult covariance API before cluster/HAC settings.

Use installed-version API documentation when signatures differ. Official references checked on 2026-10-08:
- https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLS.html
- https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html

## Worked computation
For x=[0,1,2,3,4,5] and y=[2,3,7,7,11,11], compute the slope independently using centered sums, then fit OLS with intercept and HC3 covariance. Check coefficients, residual orthogonality and interval shape; these checks verify implementation, not the data-generating assumptions.

Execute [the demonstration](../scripts/example.py) with `--self-test`; it emits JSON and raises on failed independent checks. Default execution performs the same calculation; `--self-test` additionally validates known failure cases when provided.

## Wrong inference
A small OLS p-value in observational data does not establish a causal effect. HC3 modifies uncertainty under suitable conditions; it cannot remove confounding.

## Integration contract
Input: problem statement, mathematical assumptions, serialized data or provenance, target quantity, domain/support or graph/complex semantics, tolerance, resource budget. Obtain missing essential semantics before computing.
Output: actual execution status; Python and library versions; method and options; result with units and object semantics; checks, diagnostics and warnings; code/artifact paths. Explicitly distinguish exact arithmetic, floating estimates and Monte Carlo estimates. Do not substitute stdout for mathematical validation. Route unsupported requirements back to the originating mathematical skill and preserve open obligations.

## Dependency failures
Import the required package in the selected interpreter. If absent, return nonzero status with a dependency message; do not create an output labeled successful. Environment preparation belongs to `run-math-python`, and skill creation never implies dependency installation.
