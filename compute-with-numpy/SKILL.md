---
name: compute-with-numpy
description: Implement and validate NumPy array, dense linear-algebra and random-sampling
  calculations. Use for shapes, broadcasting, dtype decisions, dense systems, SVD-based
  rank, vectorized math experiments and numeric-to-mathematical handoff.
---

# Compute with NumPy

## Workflow

1. Specify scalar field, units, array shapes, dtype, norm and desired error. Choose floating, complex or bounded integer arrays deliberately; NumPy integer arithmetic is not arbitrary-precision arithmetic. Hand exact algebra to compute-with-sympy or certify-with-python-flint.
2. Check dimensions before broadcasting and matrix operations. Use @ for matrix products and explicit axes for reductions. Reject NaN/Inf unless the problem assigns a precise meaning to them. Do not silently reshape incompatible observations.
3. Solve dense nonsingular square systems with numpy.linalg.solve, not by explicitly forming an inverse. Use lstsq for declared least-squares problems, state its rank cutoff and characterize nullspace/uniqueness. Use SVD or eigensolvers under the appropriate Hermitian hypotheses; numerical rank needs a tolerance and scale.
4. Vectorize only after validating the scalar or small analytic reference. Estimate materialized array sizes and avoid unnecessary copies; broadcasting can create a much larger result despite a short expression. Preserve semantics before optimizing.
5. Use a local numpy.random.default_rng(seed), record the bit generator and version, and distinguish Monte Carlo error from deterministic approximation error. A seed does not make sampled outcomes exhaustive or prove a concentration statement.
6. Read [library-playbook.md](references/library-playbook.md) and execute scripts/example.py --self-test. Return results with shape/dtype, residual and independently measured forward error where available. Pass conditioning and unresolved exact-rank questions to research-linear-algebra/research-numerical-analysis; use run-math-python to capture execution.

## Completion

Preserve exact assumptions and distinguish planned code from an actual run. Do not invent solver outputs or dependency availability. Use the user’s language. Read the linked playbook for detailed gates and report which result checks actually ran.

## Runnable helper

Use [analyze.py](scripts/analyze.py) to compute matrix diagnostics, linear stability, regularized solves and covariance propagation. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
