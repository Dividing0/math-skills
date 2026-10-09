# Command reference

Validate a finite topology and compute separation and closure properties.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-general-topology/scripts/finite_topology.py --example > /tmp/research-general-topology-input.json
python research-general-topology/scripts/finite_topology.py --input /tmp/research-general-topology-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply `points` as an integer count 0–12 and `opens` as lists of distinct point indices. Up to 512 open sets are accepted. The helper checks empty/whole sets and pairwise union/intersection closure, sufficient for a finite family. It reports T0, T1, Hausdorffness and finite-space compactness. Optional `subset` adds closure and interior. This gives finite counterexamples, not conclusions about arbitrary infinite spaces.
