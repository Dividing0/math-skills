# Command reference

Run pinned Lean file checks and named theorem axiom diagnostics with captured host output.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python audit-lean4-proofs/scripts/check_project.py --example > /tmp/audit-lean4-proofs-input.json
python audit-lean4-proofs/scripts/check_project.py --input /tmp/audit-lean4-proofs-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply `project` containing `lean-toolchain`, `files` relative to that project and/or `modules` plus `theorems` using simple dotted identifiers. `timeout` is per command (default 60 seconds, maximum 3600). Files are checked with `lake env lean`. Named axiom checks use a temporary module importing the requested built modules, then `#check` and `#print axioms`; the scratch source is removed afterward. Build imports first using the project's Lake targets. No build, update or cache command is run automatically.

Results contain exact commands, exit codes, stdout/stderr, timeout flags, `checker_success` and a `sorry_marker_detected` diagnostic. Always inspect the axiom output: arbitrary custom axioms are not classified automatically, comments and warnings can affect text searches, and Lean acceptance does not establish correspondence to the informal theorem. The example assumes a project with Main.lean; replace it with the real project. Missing Lake is an execution failure. Elan can provision the pinned toolchain when Lake runs.
