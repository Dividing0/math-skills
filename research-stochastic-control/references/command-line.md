# Command reference

Solve a fully observed finite-horizon MDP by exact rational backward induction.

From the collection root, or use the installed script's absolute path:

```sh
python research-stochastic-control/scripts/finite_horizon_mdp.py --example > /tmp/research-stochastic-control.json
python research-stochastic-control/scripts/finite_horizon_mdp.py --input /tmp/research-stochastic-control.json
```

Edit the example for your task before executing. Dependencies: Python standard library only. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`transitions[state][action][next_state]` contains exact integer/rational-string probabilities. Use 1..50 states and 1..20 available actions per state; each row must sum exactly to one. `costs[state][action]` has matching exact values. `terminal_costs` defaults to zeros and must have one value per state.

`horizon` is an integer 0..100. `discount` is an exact value in [0,1], default 1. Values are returned as rational strings for times 0..T, and policy rows for 0..T-1. Costs are stationary in the supplied model; policies may depend on time. The objective is minimum expected discounted cost.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
