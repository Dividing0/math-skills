# Command reference

Estimate a polynomial integral with IID, antithetic or fixed-control samples.

From the collection root, or use the installed script's absolute path:

```sh
python compute-with-monte-carlo/scripts/integrate_polynomial.py --example > /tmp/compute-with-monte-carlo.json
uv run --with numpy python compute-with-monte-carlo/scripts/integrate_polynomial.py --input /tmp/compute-with-monte-carlo.json
```

Edit the example for your task before executing. Dependencies: numpy. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`coefficients` are 1..30 finite coefficients in ascending powers. `lower`/`upper` are finite with lower<upper (defaults 0,1). `samples` is 2..1,000,000 independent units, default 10,000; `seed` is an integer in [0,2**64), default 0.

`method` is `plain`, `antithetic`, or `control-variate`. The latter requires finite `control_coefficient`, chosen independently of the estimation sample, and uses X as the control. Antithetic mode uses paired points X and lower+upper-X.

Outputs include the estimate, standard error, approximate 95% interval, analytic polynomial integral, actual error, number of independent units and function evaluations. No arbitrary expression evaluation, MCMC or adaptive stopping is implemented.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
