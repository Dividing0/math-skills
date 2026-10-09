# Command reference

Solve stationary distributions of a finite rational Markov chain without claiming mixing.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-stochastic-processes/scripts/markov_chain.py --example > /tmp/research-stochastic-processes-input.json
uv run --with sympy python research-stochastic-processes/scripts/markov_chain.py --input /tmp/research-stochastic-processes-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: sympy. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply a rational row-stochastic square `transition` matrix (1–50 states). Entries are integers or strings; row sums must equal one exactly. The helper solves πP=π and sum(π)=1, reports uniqueness and free parameters, and retains nonnegativity as constraints for a stationary family. Optional probability vector `initial` and integer `steps` (0–1000) compute its exact finite-time distribution. A unique stationary distribution does not establish aperiodicity or mixing; the periodic two-state example makes this visible.
