---
name: compute-with-scipy
description: Solve numerical mathematical tasks using SciPy integration, ODE, sparse
  linear algebra, roots and optimization APIs. Use when choosing solvers, checking
  convergence/status and translating residuals or tolerances into scoped computational
  evidence.
---

# Compute with SciPy

## Workflow

1. Normalize the problem, domains, input uncertainty, desired norm, tolerance and performance budget. Select the SciPy submodule matching the mathematical structure; send exact identities and rigorous enclosures to other tools.
2. For scalar roots, prefer a bracketed method when continuity and a sign-changing bracket are justified. Record existence separately from uniqueness and completeness. For optimization, check feasibility, gradient/optimality residuals and assumptions; solver success is not global optimality for a nonconvex problem.
3. For quadrature, specify finite/infinite domain, singularities, oscillation and integration tolerances. Interpret returned error estimates as estimates rather than certified bounds unless another argument validates them. Split known trouble points and compare to an independent analytic or higher-precision reference.
4. For solve_ivp, state RHS/state shapes, interval, boundary versus initial conditions, events and method. Use RK methods for nonstiff tasks and consider Radau/BDF for stiffness. Inspect success, final time and event termination. Local error tolerances and dense output do not guarantee a global mathematical error bound or complete event detection.
5. For sparse systems, choose a representation and solver based on symmetry/definiteness. CG requires Hermitian positive-definite structure; inspect info, iterations and true residual. A limited iteration count or nonzero info is a failure to converge, not a valid answer merely because a vector was returned.
6. Read [library-playbook.md](references/library-playbook.md); run scripts/example.py --self-test. Return actual settings/status, analytic-reference or refinement checks and unresolved proof obligations. Hand results back to numerical-analysis, ODE/PDE, optimization or probability skills through run-math-python.

## Completion

Preserve exact assumptions and distinguish planned code from an actual run. Do not invent solver outputs or dependency availability. Use the user’s language. Read the linked playbook for detailed gates and report which result checks actually ran.

## Runnable helper

Use [numerical.py](scripts/numerical.py) to solve finite linear programs, discrete transport and polynomial ODE initial-value problems. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
