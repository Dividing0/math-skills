# Command reference

Inspect finite simple graph structure, shortest paths and maximum flows.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python analyze-graphs-with-networkx/scripts/graph_report.py --example > /tmp/analyze-graphs-with-networkx-input.json
uv run --with networkx python analyze-graphs-with-networkx/scripts/graph_report.py --input /tmp/analyze-graphs-with-networkx-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: networkx. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply distinct integer/string `nodes` (including isolates), Boolean `directed`, and `edges` with `source`, `target`, finite numeric `weight`. Loops and parallel edges are rejected rather than silently collapsed.

`operation: "summary"` returns components plus strong components for directed graphs or bipartiteness for undirected graphs. `shortest-path` takes source/target, chooses Dijkstra or Bellman–Ford based on weight signs, and recomputes path cost. Unreachable and source-reachable negative-cycle outcomes are distinct; a reachable cycle does not alone prove that a particular target has unbounded distance. `max-flow` requires directed nonnegative weights interpreted as capacities and distinct source/target; it returns flows, a cut, conservation residual and gap. Floating weights carry numerical error.
