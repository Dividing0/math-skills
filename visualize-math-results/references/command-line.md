# Command reference

Render supplied finite data to a labeled PNG, SVG or PDF using a headless backend.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python visualize-math-results/scripts/plot_data.py --example > /tmp/visualize-math-results-input.json
uv run --with matplotlib python visualize-math-results/scripts/plot_data.py --input /tmp/visualize-math-results-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: matplotlib. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply aligned finite `x`, `y`, nonempty `xlabel`, `ylabel` (include units when applicable), and an `output` path ending in .png, .svg or .pdf. Optional `kind` is `scatter` (default) or `line` (requires strictly increasing x), `xscale`/`yscale` are `linear` or `log`, and `title` labels the figure. `yerr` requires aligned nonnegative values and an `uncertainty_label`; log error bars must stay positive. Uses the headless Agg backend, writes the chosen output file, and reports path/size. Split discontinuities before drawing lines; the tool cannot infer them from data.
