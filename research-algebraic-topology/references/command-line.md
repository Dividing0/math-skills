# Command reference

Compute unreduced homology dimensions of a finite simplicial complex over F_p.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-algebraic-topology/scripts/simplicial_homology.py --example > /tmp/research-algebraic-topology-input.json
python research-algebraic-topology/scripts/simplicial_homology.py --input /tmp/research-algebraic-topology-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply `simplices` as nonempty lists of distinct integer vertex labels and optional `prime` (default 2; prime at most 251). All faces are added automatically. The helper builds signed boundary matrices over F_p, verifies consecutive boundaries compose to zero, and returns unreduced Betti numbers, ranks and Euler characteristic. It caps simplex size at 10 vertices and total faces at 2,000. Integer torsion and topological classification are not computed; filling a triangle must be represented by its 2-simplex.
