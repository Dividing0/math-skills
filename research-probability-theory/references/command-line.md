# Command reference

Compute exact finite joint-law moments, dependence and information quantities.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-probability-theory/scripts/finite_probability.py --example > /tmp/research-probability-theory-input.json
python research-probability-theory/scripts/finite_probability.py --input /tmp/research-probability-theory-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply nonempty `outcomes` with rational `x`, `y`, `p` (integers or strings). Repeated value pairs are combined. Nonnegative probabilities must sum exactly to one. Results include exact marginals, expectations, covariance and an exhaustive product-law independence check; zero covariance does not imply independence. Entropies and mutual information use floating base-2 logarithms. Zero-probability outcomes contribute no logarithm term. This is a finite discrete law, not differential entropy or a limit theorem.
