# Command reference

Search local Lean source for a literal query and return bounded file/line matches.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python search-mathlib/scripts/search_local.py --example > /tmp/search-mathlib-input.json
python search-mathlib/scripts/search_local.py --input /tmp/search-mathlib-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply existing `project`, nonempty literal `query` and optional `limit` (1–1000, default 50). Search project Lean source and the installed `.lake/packages/mathlib/Mathlib` directory if present, skipping generated/hidden directories and symlink files. Returns bounded file/line matches and a truncation flag. Comments and theorem uses can match; confirm declarations with Lean's `#check`. No match is not a claim of mathematical absence, and core Lean/Batteries may need separate searches.
