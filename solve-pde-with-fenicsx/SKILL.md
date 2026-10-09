---
name: solve-pde-with-fenicsx
description: Implement finite-element PDE calculations with FEniCSx DOLFINx, UFL and PETSc; validate weak forms, boundary conditions, solver convergence and discretization. Use for Poisson, elliptic models and finite-element convergence studies; distinguish missing dependencies from failed mathematics.
---

# Solve PDEs with FEniCSx

Read [library-playbook.md](references/library-playbook.md) for API locators, worked example, failure analysis and the integration contract. Run `scripts/example.py --self-test` using the task's selected Python interpreter before adapting it. Missing dependencies must be reported explicitly; do not invent executions.

## Workflow

1. Record DOLFINx/UFL/Basix/PETSc/MPI versions and scalar type; match documentation to the installed version. Main documentation may describe unreleased APIs. Check function signatures; new `LinearProblem` requires `petsc_options_prefix`, older versions may not accept it.
2. State strong PDE, domain, coefficients, boundary partitions, source and units. Derive the weak form with outward-normal signs explicitly. Check coercivity or nullspaces/compatibility; pure Neumann Poisson needs compatibility and a gauge, not an arbitrary pinned value silently changing the model.
3. Construct mesh and finite-element space with `fem.functionspace`; tag boundaries and locate boundary DOFs. Apply essential conditions with `fem.dirichletbc`; include natural conditions in UFL forms. Inspect tag coverage rather than trusting a plot.
4. Solve with documented PETSc options and a unique options prefix on every rank when supported. Require positive KSP convergence reason or `ksp_error_if_not_converged`. Scatter ghost values and perform global MPI reductions for norms. A small algebraic residual addresses the discretized system only.
5. Use a manufactured solution or independently known limit, mesh refinement and sufficiently accurate quadrature. Separate algebraic error, discretization error and modeling error. Report degrees of freedom, mesh sizes, norms, BCs and solver evidence; never call one mesh a PDE accuracy certificate.

## Handoff

Use the existing mathematical skills (research-partial-differential-equations, research-finite-element-methods, research-numerical-pde, audit-numerical-methods) to establish assumptions and interpret conclusions. Use `run-math-python` for reproducible execution records. Return the actual executed code, versions, inputs, status, diagnostics, oracle checks and artifacts. Label evidence as numerical, exact symbolic, validated enclosure or formal proof; do not upgrade evidence without a checker.
