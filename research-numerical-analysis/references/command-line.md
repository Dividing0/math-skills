# Command reference

Measure empirical convergence orders from a supplied refinement/error table.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-numerical-analysis/scripts/refinement.py --example > /tmp/research-numerical-analysis-input.json
python research-numerical-analysis/scripts/refinement.py --input /tmp/research-numerical-analysis-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply equal-length positive finite `steps` and `errors`, with at least two rows and strictly decreasing steps. Computes log(error_i/error_(i+1))/log(h_i/h_(i+1)). Zero errors are rejected because logarithmic orders are undefined there. The input errors must already reflect the requested norm and a justified reference; these are observed rates, not a proof of stability, consistency or convergence.
