# Command reference

Compare coupled Euler-Maruyama and Milstein paths against exact scalar GBM.

From the collection root, or use the installed script's absolute path:

```sh
python simulate-stochastic-differential-equations/scripts/simulate_gbm.py --example > /tmp/simulate-stochastic-differential-equations.json
uv run --with numpy python simulate-stochastic-differential-equations/scripts/simulate_gbm.py --input /tmp/simulate-stochastic-differential-equations.json
```

Edit the example for your task before executing. Dependencies: numpy. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

The helper supports scalar geometric Brownian motion only. Supply finite `drift`, nonnegative `diffusion`, optional `initial` (default 1), positive `duration` (default 1), and `interpretation` (`ito` default, or `stratonovich`). `steps` is even and at least 2; `paths` is at least 2; their product is at most 2,000,000. Defaults: 64 steps, 2,000 paths. `seed` is an integer in [0,2**64), default 0.

The output compares `steps/2` and `steps` using shared noise, giving terminal RMSEs, means, observed strong orders, and an exact-path sample standard error. It is not a general SDE solver or a rigorous confidence certificate.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
