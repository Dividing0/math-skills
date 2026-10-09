# Command reference

Run exact symbolic algebra, calculus, matrix, dynamics and local metric calculations.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python compute-with-sympy/scripts/calculate.py --example > /tmp/compute-with-sympy-input.json
uv run --with sympy python compute-with-sympy/scripts/calculate.py --input /tmp/compute-with-sympy-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: sympy. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Declare `symbols` as a mapping from names to Boolean assumptions (`real`, `positive`, `nonnegative`, `nonzero`, `integer`). The default is real `x`. Expressions are strings using declared symbols, exact numbers, `+ - * / **`, constants `pi E I`, and unary `sin cos tan exp log sqrt Abs sinh cosh`. The AST reader does not evaluate Python calls or attributes. Decimal strings become exact rationals. Expressions are limited to 4,096 characters/512 nodes; numerical exponents have magnitude at most 1,000.

- `simplify`, `factor`, `expand`, `differentiate`, `integrate`, `series`, `solve`, `residue`: provide `expression`; calculus/solve operations also take `variable` (default `x`). Derivatives and series accept `order`; series and residues accept `point`. Series accepts `direction`. Solve intersects `domain: "real"` or `"complex"` with the declared variable assumptions, removes recorded denominator-zero sets, and reports the effective domain and unresolved `ConditionSet` results. For complex roots, declare the variable with empty assumptions rather than retaining the default real `x`. Integration returns an antiderivative derivative residual, not a global integrability theorem.
- `matrix`: provide a nonempty rectangular `matrix` (at most 20×20), optionally `rhs`. Reports RREF, rank, nullspace and residuals, determinant/characteristic polynomial for square matrices, and linear solution sets. Symbolic rank can change at exceptional parameter values.
- `groebner`: provide `variables`, `polynomials`, optional `order` (`lex` by default) and `query`. Computation is over QQ. A zero query remainder establishes membership in the computed ideal; generator reductions and reconstruction residual are reported. This is not an independent original-generator certificate.
- `dynamics`: provide distinct state `variables`, matching autonomous `field`, optional `point` and `invariant`. Reports Jacobian, equilibrium residual and Lie derivative. A zero symbolic derivative is conditional on the expression domains and solution regularity; no global stability follows.
- `metric`: provide 1–3 distinct `coordinates` and a symmetric `metric`. Reports determinant, Christoffel symbols, Ricci tensor and scalar curvature, with the curvature convention in output. Work where det(g)≠0. Positivity, chart domain and completeness remain separate obligations.

Division restrictions are recorded before simplification. Other transcendental branch/domain conditions are not exhaustively inferred. For nontrivial expressions, run with an external time budget through `run-math-python`.
