# Command reference

Compute matrix diagnostics, linear stability, regularized solves and covariance propagation.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python compute-with-numpy/scripts/analyze.py --example > /tmp/compute-with-numpy-input.json
uv run --with numpy python compute-with-numpy/scripts/analyze.py --input /tmp/compute-with-numpy-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: numpy. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

All operations take a finite real `matrix`, at most 2,000 in either dimension and one million entries. `rcond` defaults to max(shape) times machine epsilon and sets relative numerical rank cutoff; rank is not an exact algebraic assertion.

- `matrix`: report singular values, rank and 2-norm condition ratio; optional `rhs` adds a least-squares solution.
- `least-squares`: require `rhs`; return solution, original residual, stationarity residual and column-rank uniqueness diagnostic.
- `tikhonov`: additionally take nonnegative `regularization` (lambda) for minimizing ||Ax-b||² + lambda||x||², solved as augmented least squares.
- `stability`: square state matrix, `timebase: "continuous"` (default) or `"discrete"`, and positive `tolerance` (default 1e-10). Eigenvalues and spectral margin give a numerical stable/unstable/boundary classification for that linear system.
- `propagate-covariance`: provide symmetric PSD `covariance` matching matrix columns. Report AΣAᵀ, with symmetry/PSD checked to 1e-12; using a Jacobian makes this a local approximation.

`condition_2: null` denotes a singular/infinite ratio. For rectangular matrices, full row rank does not establish uniqueness of Ax=b; inspect rank and the explicit uniqueness flag.
