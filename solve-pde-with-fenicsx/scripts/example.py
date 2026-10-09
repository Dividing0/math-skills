#!/usr/bin/env python3
"""Small executable independent-oracle check; ordinary Python required."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse, json, sys

parser = argparse.ArgumentParser()
parser.add_argument("--self-test", action="store_true")
args = parser.parse_args()
try:
    import inspect
    import numpy as np
    import dolfinx
    from dolfinx import fem, mesh
    from dolfinx.fem.petsc import LinearProblem
    from mpi4py import MPI
    from petsc4py import PETSc
    import ufl

    comm = MPI.COMM_WORLD
    if comm.size != 1:
        raise RuntimeError(
            "This compact LU demo requires one MPI rank; use a distributed-capable solver for multiple ranks"
        )

    def solve(n):
        domain = mesh.create_interval(comm, n, [0.0, 1.0])
        V = fem.functionspace(domain, ("Lagrange", 1))
        facets = mesh.locate_entities_boundary(
            domain, 0, lambda x: np.logical_or(np.isclose(x[0], 0), np.isclose(x[0], 1))
        )
        dofs = fem.locate_dofs_topological(V, 0, facets)
        bc = fem.dirichletbc(PETSc.ScalarType(0), dofs, V)
        u = ufl.TrialFunction(V)
        v = ufl.TestFunction(V)
        a = ufl.inner(ufl.grad(u), ufl.grad(v)) * ufl.dx
        L = ufl.inner(fem.Constant(domain, PETSc.ScalarType(2)), v) * ufl.dx
        opts = {
            "ksp_type": "preonly",
            "pc_type": "lu",
            "ksp_error_if_not_converged": True,
        }
        kwargs = {"bcs": [bc], "petsc_options": opts}
        # The retrieved main API is development documentation. Gate the new required
        # prefix by the actual installed signature; do not pass it to older releases.
        if "petsc_options_prefix" in inspect.signature(LinearProblem).parameters:
            kwargs["petsc_options_prefix"] = f"math_demo_{n}_"
        problem = LinearProblem(a, L, **kwargs)
        uh = problem.solve()
        uh.x.scatter_forward()
        assert problem.solver.getConvergedReason() > 0
        x = ufl.SpatialCoordinate(domain)
        exact = x[0] * (1 - x[0])
        measure = ufl.Measure("dx", domain=domain, metadata={"quadrature_degree": 6})
        local = fem.assemble_scalar(
            fem.form(ufl.inner(uh - exact, uh - exact) * measure)
        )
        error = float(np.sqrt(comm.allreduce(float(np.real(local)), op=MPI.SUM)))
        assert error > 0 and np.isfinite(error)
        return error, {
            "dofs_global": V.dofmap.index_map.size_global * V.dofmap.index_map_bs,
            "KSP_converged_reason": int(problem.solver.getConvergedReason()),
            "solver_options": opts,
        }

    runs = [solve(n) for n in [8, 16]]
    errors = [r[0] for r in runs]
    ratio = errors[0] / errors[1]
    # The linear interpolant of this quadratic has L2 error h^2/sqrt(30).
    expected = [(1 / n) ** 2 / np.sqrt(30) for n in [8, 16]]
    np.testing.assert_allclose(errors, expected, rtol=1e-6, atol=1e-12)
    assert 3.9 < ratio < 4.1
    import basix, mpi4py

    result = {
        "dolfinx": dolfinx.__version__,
        "ufl": ufl.__version__,
        "basix": basix.__version__,
        "petsc": list(PETSc.Sys.getVersion()),
        "mpi4py": mpi4py.__version__,
        "MPI_library": MPI.Get_library_version(),
        "scalar_dtype": str(np.dtype(PETSc.ScalarType)),
        "runs": [r[1] for r in runs],
        "mesh_intervals": [8, 16],
        "L2_errors": errors,
        "error_ratio": ratio,
        "oracle": "h^2/sqrt(30) for the piecewise-linear interpolant of x(1-x)",
        "evidence": "discretization error verified for a manufactured quadratic; not general PDE certification",
    }
except ModuleNotFoundError as exc:
    print(json.dumps({"status": "dependency-unavailable", "dependency": exc.name}))
    sys.exit(2)
print(
    json.dumps(
        {"status": "passed", "self_test": args.self_test, **result}, allow_nan=False
    )
)
