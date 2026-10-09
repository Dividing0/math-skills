# Library playbook

## API selection
`gudhi.SimplexTree.insert`, `get_filtration`, `compute_persistence(homology_coeff_field=2, persistence_dim_max=True)`, `persistence_intervals_in_dimension`, `persistent_betti_numbers`.

Use installed-version API documentation when signatures differ. Official references checked on 2026-10-08:
- https://gudhi.inria.fr/python/latest/simplex_tree_ref.html
- https://gudhi.inria.fr/python/latest/rips_complex_ref.html

## Worked computation
Insert three vertices at0, three triangle edges at1 and a filled triangle at2. Over F2, the H1 interval is[1,2); before filling, the boundary cycle has Betti numbers(1,1), and afterward(1,0). The script independently row-reduces boundary matrices modulo2 and compares ranks.

Execute [the demonstration](../scripts/example.py) with `--self-test`; it emits JSON and raises on failed independent checks. Default execution performs the same calculation; `--self-test` additionally validates known failure cases when provided.

## Wrong inference
Computing only vertices and edges and seeing an infinite H1 bar does not establish a persistent hole in the full Rips complex: omitted triangles can kill it. Coefficients in a composite modulus do not satisfy the field requirement.

## Integration contract
Input: problem statement, mathematical assumptions, serialized data or provenance, target quantity, domain/support or graph/complex semantics, tolerance, resource budget. Obtain missing essential semantics before computing.
Output: actual execution status; Python and library versions; method and options; result with units and object semantics; checks, diagnostics and warnings; code/artifact paths. Explicitly distinguish exact arithmetic, floating estimates and Monte Carlo estimates. Do not substitute stdout for mathematical validation. Route unsupported requirements back to the originating mathematical skill and preserve open obligations.

## Dependency failures
Import the required package in the selected interpreter. If absent, return nonzero status with a dependency message; do not create an output labeled successful. Environment preparation belongs to `run-math-python`, and skill creation never implies dependency installation.
