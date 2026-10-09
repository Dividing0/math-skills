# Command reference

Capture or compare Lean pins and source hashes without changing a project.

From the collection root, or use the installed script's absolute path:

```sh
python migrate-lean4-projects/scripts/project_snapshot.py --example > /tmp/migrate-lean4-projects.json
python migrate-lean4-projects/scripts/project_snapshot.py --input /tmp/migrate-lean4-projects.json
```

Edit the example for your task before executing. Dependencies: Python standard library only. Heavy dependencies are imported only when computing, so `--help` and `--example` do not need them. Helpers never install dependencies themselves; the optional `uv run --with` invocation provisions an isolated environment.

## Inputs and limits

`operation: "snapshot"` requires `project`, an existing directory containing `lean-toolchain`. It hashes present `lakefile.toml`, `lakefile.lean`, `lake-manifest.json`, and up to 10,000 non-generated Lean source files. It performs no build or installation.

`operation: "compare"` requires `before` and `after`: the **result objects** returned by two snapshot calls, not their outer CLI envelopes. The returned changes classify hashes only. `--example` uses the current directory; replace it with the actual Lean project.

## Output and exit status

The JSON envelope contains `status`, `result`, `evidence`, Python/dependency versions and the input SHA-256. CLI exit 0 means the computation completed, not that a theorem, solver model or test passed. Inspect result fields such as `solver_status`, `passed` and the stated scope. Invalid inputs or execution failures exit 1; missing Python dependencies exit 3. Nonfinite JSON literals are rejected. Relative input paths are resolved from the invoking process; prefer absolute project paths. No helper evaluates Python source supplied in JSON.
