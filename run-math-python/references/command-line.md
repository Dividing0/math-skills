# Command reference

Report host interpreters, executables and installed package metadata without installing dependencies.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python run-math-python/scripts/host_capabilities.py --example > /tmp/run-math-python-input.json
python run-math-python/scripts/host_capabilities.py --input /tmp/run-math-python-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Input may be `{}`. Optional `packages` and `executables` lists override the inventory. Reports the exact interpreter, platform, site-packages location, installed distribution versions (null when absent), and PATH locations. This does not import heavy packages, run executables, install software, or assert solver/backend health. Run a library's own smoke check after selecting an environment; keep execution records with the existing `run_math.py`.
