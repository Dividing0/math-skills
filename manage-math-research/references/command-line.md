# Command reference

Audit a mathematical dependency ledger for cycles and unresolved prerequisites.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python manage-math-research/scripts/dependencies.py --example > /tmp/manage-math-research-input.json
python manage-math-research/scripts/dependencies.py --input /tmp/manage-math-research-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply `claims` with unique string `id`, `status` in `proved`, `assumed`, `conjecture`, `blocked`, `observation`, and optional `depends_on` IDs. Unknown dependencies fail. The report finds cycles, topological order, declared proved claims with unresolved prerequisites, assumptions and ready obligations. An observation never automatically discharges a proof dependency. The helper checks the ledger; it does not inspect the proof bodies or justify declared statuses.
