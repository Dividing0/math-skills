# Library playbook

## API selection
`nx.DiGraph`, `nx.single_source_dijkstra`, `nx.bellman_ford_path`, `nx.NetworkXNoPath`, `nx.NetworkXUnbounded`; prefer explicit weighted algorithms over implicit dispatch.

Use installed-version API documentation when signatures differ. Official references checked on 2026-10-08:
- https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html
- https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.weighted.bellman_ford_path.html

## Worked computation
Directed routes s→a cost4, a→t cost3, s→b cost2, b→t cost8 give path s,a,t of cost7. The demonstration enumerates simple paths independently and checks the optimum; it also checks a negative edge without a negative cycle using Bellman–Ford.

Execute [the demonstration](../scripts/example.py) with `--self-test`; it emits JSON and raises on failed independent checks. Default execution performs the same calculation; `--self-test` additionally validates known failure cases when provided.

## Wrong inference
An undirected copy can invent a reverse route in a one-way network. A minimum-cost node path through a multigraph does not determine which parallel edge was used.

## Integration contract
Input: problem statement, mathematical assumptions, serialized data or provenance, target quantity, domain/support or graph/complex semantics, tolerance, resource budget. Obtain missing essential semantics before computing.
Output: actual execution status; Python and library versions; method and options; result with units and object semantics; checks, diagnostics and warnings; code/artifact paths. Explicitly distinguish exact arithmetic, floating estimates and Monte Carlo estimates. Do not substitute stdout for mathematical validation. Route unsupported requirements back to the originating mathematical skill and preserve open obligations.

## Dependency failures
Import the required package in the selected interpreter. If absent, return nonzero status with a dependency message; do not create an output labeled successful. Environment preparation belongs to `run-math-python`, and skill creation never implies dependency installation.
