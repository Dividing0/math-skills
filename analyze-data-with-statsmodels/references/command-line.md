# Command reference

Fit a user-supplied full-rank OLS design with conventional or HC3 uncertainty.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python analyze-data-with-statsmodels/scripts/fit_ols.py --example > /tmp/analyze-data-with-statsmodels-input.json
uv run --with numpy --with statsmodels python analyze-data-with-statsmodels/scripts/fit_ols.py --input /tmp/analyze-data-with-statsmodels-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: numpy, statsmodels. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply finite aligned `design` (rows × predictors) and `response`. `intercept` defaults to true and explicitly adds a column; set false if the supplied design already contains it. Rank deficiency and nonpositive residual degrees of freedom are rejected. `covariance` is `HC3` (default) or `nonrobust`; near-unit leverage rejects unstable HC3 estimates. `alpha` defaults to 0.05. Returns coefficients, intervals, residuals, rank/conditioning diagnostics and normal-equation residual. Optional `prediction_design` uses the same raw predictor columns. Covariance choice and sampling assumptions require justification; no causal interpretation follows.
