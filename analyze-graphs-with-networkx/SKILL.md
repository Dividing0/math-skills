---
name: analyze-graphs-with-networkx
description: Implement and execute graph calculations using NetworkX. Use for finite directed or undirected graphs, paths, components, flows, centrality and graph-theory computational experiments.
---

# Analyze Graphs with NetworkX

## Workflow
1. Specify `Graph`, `DiGraph`, `MultiGraph` or `MultiDiGraph`; preserve isolated nodes, directedness, self-loops and edge multiplicity. Define edge weight and node identifiers explicitly.
2. Reject absent or nonfinite required weights rather than relying on an implicit default. Choose BFS for hop counts, Dijkstra for nonnegative costs, Bellman–Ford for negative costs with reachable negative-cycle handling. Do not use a static graph for time-dependent costs without a valid reduction.
3. For multigraph routes, retain the selected edge keys or state the minimum-parallel-edge aggregation; a node sequence alone does not identify the edge route. For flow, define capacities and check conservation and cut capacity; avoid unsupported graph types.
4. Verify paths against actual directed edges and recompute their costs. On small graphs compare with exhaustive simple-path enumeration. Treat no-path and unbounded-distance outcomes separately. Record iteration tolerance for iterative centrality and enforce its convergence checks.
5. Transfer to `research-graph-theory` or `research-spectral-graph-theory`; retain finite-input status and model assumptions.

## Execution and handoff
Read [the library playbook](references/library-playbook.md) for the API map, worked example and integration contract. Run `python scripts/example.py --self-test` with the interpreter selected by `run-math-python`; preserve stdout, stderr, exit status and dependency versions. Missing dependencies must produce a failed run, never a fabricated result. Keep the demonstration separate from the user's implementation.

Receive a mathematical statement, assumptions, input schema, target quantity, precision/tolerance and resource budget. Return runnable code, input provenance, versions, diagnostics, measured results, failed checks and limitations. Mark the result as exact on a specified finite object, numerical approximation, Monte Carlo estimate, or unexecuted; never label a computation a universal proof. Hand results to the named mathematical skill for interpretation and to `validate-math-implementation` for implementation checks.
