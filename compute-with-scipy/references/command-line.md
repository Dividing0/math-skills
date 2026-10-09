# Command reference

Solve finite linear programs, discrete transport and polynomial ODE initial-value problems.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python compute-with-scipy/scripts/numerical.py --example > /tmp/compute-with-scipy-input.json
uv run --with numpy --with scipy python compute-with-scipy/scripts/numerical.py --input /tmp/compute-with-scipy-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: numpy, scipy. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

- `linear-program`: provide objective `c`, optional paired `A_ub,b_ub` and `A_eq,b_eq`, and per-variable `[lower,upper]` `bounds` (null denotes unbounded). Default bounds are nonnegative. Uses HiGHS minimization. Read `success`, solver status and primal residuals before interpreting a solution.
- `transport`: provide rectangular `cost` and nonnegative `source`/`target` masses with equal totals (checked to tolerance). Returns a finite Kantorovich plan, objective and marginal residuals, not a Monge map or an exact certificate.
- `polynomial-ivp`: provide `initial`, strictly increasing `times`, `powers` (one monomial per row, one nonnegative integer exponent per state) and `coefficients` (one row per state, one column per monomial). For y'=-2y use powers=[[1]], coefficients=[[-2]]. Supports `method`, `rtol` (default 1e-8), `atol` (default 1e-10). Returns actual solver success, trajectory and evaluation count. No events or nonautonomous terms are encoded; blow-up may stop integration before the last time.

LPs are limited to 10,000 variables, trajectories to 10,000 output times. Numerical solver failure is a result with `success: false`, not a proved infeasibility certificate. Run expensive cases through the execution runner with a time budget.
