# Command reference

Compute rational planar orientations and convex hulls with exact area.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-computational-geometry/scripts/planar_geometry.py --example > /tmp/research-computational-geometry-input.json
python research-computational-geometry/scripts/planar_geometry.py --input /tmp/research-computational-geometry-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: Python standard library only. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply rational planar `points`, using integers or strings. `operation: "orientation"` requires exactly three points and returns the determinant and sign. `operation: "convex-hull"` accepts up to 10,000 points, removes duplicates and interior collinear points, and returns counterclockwise extreme vertices and rational area; a collinear hull consists of endpoints. Exact arithmetic describes supplied rational coordinates, not measurement uncertainty.
