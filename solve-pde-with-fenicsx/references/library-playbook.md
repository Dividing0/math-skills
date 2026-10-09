# Library playbook

## Primary documentation

Retrieved/checked 2026-10-08. Recheck documentation against installed versions before adapting API calls.

- https://docs.fenicsproject.org/dolfinx/main/python/generated/dolfinx.fem.petsc.html
- https://docs.fenicsproject.org/dolfinx/main/python/generated/dolfinx.fem.html
- https://docs.fenicsproject.org/dolfinx/main/python/generated/dolfinx.mesh.html

The workflow names the relevant API locators; use the actual installed signatures and recorded version, especially for release/development discrepancies.

## Worked calculation

Solve -u''=2 on [0,1] with u(0)=u(1)=0 using linear elements on 8 and 16 intervals. Compare to u=x(1-x), integrate L2 error and verify approximately second-order convergence.

Execute `../scripts/example.py --self-test`. The script emits JSON and fails its assertions if the independent oracle disagrees. An unavailable dependency emits a dependency-unavailable status and exits 2; that is not a passed numerical check. Assertions run in ordinary Python, so do not launch with `-O`.

## False inference

KSP converged, therefore the continuum PDE solution is accurate to solver tolerance. This confuses algebraic and discretization errors.

## Integration contract

Receive a precise mathematical statement, assumptions, units, dimensions, data provenance, desired error/accuracy, available interpreter and runtime constraints from the mathematical skill. Return the exact implementation, dependency versions, executed inputs, raw outcomes, failure/status information, and independent checks. Keep numerical tolerance separate from mathematical guarantees. If an assumption or dependency is missing, return the missing item and any valid partial analysis rather than a fabricated computed result.

## Scope and escalation

Hand back to research-partial-differential-equations, research-finite-element-methods, research-numerical-pde, audit-numerical-methods when the issue concerns mathematical assumptions or justification rather than an API. Prefer the smaller supported calculation to an unvalidated large model. Preserve input data and task-local outputs; avoid modifying environments or external services without the task's authorization.

## API locators and release boundary

- Mesh reference: `mesh.create_interval`, `mesh.locate_entities_boundary`; FEM reference: `fem.functionspace`, `fem.locate_dofs_topological`, `fem.dirichletbc`, `fem.Constant`, `fem.form`, `fem.assemble_scalar`.
- PETSc reference: `LinearProblem` and `.solver.getConvergedReason()`. Retrieved main documentation identifies 0.12.0.dev0; it is development documentation, not an installed-release assertion. Use signature inspection to gate `petsc_options_prefix`; otherwise match the installed version's reference.
- The manufactured solution u=x(1-x) has -u''=2 and zero endpoints. For its P1 interpolation the local error is (x-a)(b-x), so squared error integrated over [0,1] is h^4/30 and L2 error is h^2/sqrt(30). For this constant-coefficient 1D problem the Galerkin nodal values equal exact nodal values. This independent oracle validates this example, not arbitrary FEM solutions.
- The demo requires one MPI rank and a compatible PETSc LU build. It scatters ghosts and uses a global norm reduction; do not copy its serial LU assumption into distributed production. DOLFINx was unavailable in the authoring environment; the numerical demo remains unexecuted until a compatible runtime is provided.
