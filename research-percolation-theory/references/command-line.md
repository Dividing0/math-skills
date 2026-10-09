# Command reference

Enumerate exact two-terminal connection probabilities in a small independent bond-percolation graph.

## Run

From the collection root, or use an installed absolute script path:

```sh
python research-percolation-theory/scripts/bond_connection.py --example > /tmp/research-percolation-theory-input.json
python research-percolation-theory/scripts/bond_connection.py --input /tmp/research-percolation-theory-input.json
```

Only the Python standard library is required. Edit the example for the actual task. `--input -` reads stdin. JSON output records `status`, `evidence`, `result`, dependency/Python versions and `input_sha256`. Exit 0 means the calculation completed; inspect `is_matroid`, `stationary` and other result fields before interpreting the result. Invalid input exits 1. Use the `run-math-python` execution runner to bound expensive tasks and retain logs.

## Inputs and interpretation

Supply `vertices` (1–30), distinct undirected `edges` (at most 18) with endpoints indexed 0..vertices-1, `source`, `target`, and rational `probability` in [0,1]. Every subset of edges is enumerated, and connected configurations are counted by edge cardinality. The connection probability is summed exactly under independent bonds with a common opening probability. Self-loops and parallel edges are rejected. Isolates and p=0/1 are supported. This is a finite two-terminal result, not an infinite-cluster threshold estimate or a dependent-bond model.
