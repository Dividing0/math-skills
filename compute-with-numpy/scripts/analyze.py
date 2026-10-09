#!/usr/bin/env python3
"""Compute matrix diagnostics, linear stability, regularized solves and covariance propagation."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("numpy",)
EVIDENCE = "numerical-evidence"
EXAMPLE = {
    "operation": "least-squares",
    "matrix": [[1, 0], [1, 1], [1, 2]],
    "rhs": [1, 2, 2],
}


def compute(data):
    import numpy as np

    def array(value, ndim):
        a = np.asarray(value, dtype=float)
        if a.ndim != ndim or not a.size or not np.isfinite(a).all():
            raise ValueError(
                "expected nonempty finite array with the declared dimension"
            )
        if a.size > 1000000:
            raise ValueError("array size exceeds one million entries")
        return a

    A = array(data["matrix"], 2)
    op = data["operation"]
    if max(A.shape) > 2000:
        raise ValueError("matrix dimension exceeds 2000")
    singular = np.linalg.svd(A, compute_uv=False)
    cutoff = float(data.get("rcond", max(A.shape) * np.finfo(float).eps))
    if not np.isfinite(cutoff) or not 0 <= cutoff < 1:
        raise ValueError("rcond must be finite and in [0,1)")
    rank = int(np.count_nonzero(singular > cutoff * singular[0]))
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        ratio = singular[0] / singular[-1]
    condition = float(ratio) if np.isfinite(ratio) else None
    result = {
        "shape": list(A.shape),
        "singular_values": singular.tolist(),
        "rank": rank,
        "relative_cutoff": cutoff,
        "condition_2": condition,
        "condition_note": "null denotes an infinite condition number",
    }
    if op in {"matrix", "least-squares", "tikhonov"}:
        if "rhs" in data:
            b = array(data["rhs"], 1)
            if len(b) != A.shape[0]:
                raise ValueError("rhs must match matrix rows")
            lam = float(data.get("regularization", 0)) if op == "tikhonov" else 0
            if not np.isfinite(lam) or lam < 0:
                raise ValueError("regularization must be finite and nonnegative")
            augmented = np.vstack([A, np.sqrt(lam) * np.eye(A.shape[1])]) if lam else A
            rhs = np.concatenate([b, np.zeros(A.shape[1])]) if lam else b
            x = np.linalg.lstsq(augmented, rhs, rcond=cutoff)[0]
            residual = A @ x - b
            result.update(
                solution=x.tolist(),
                residual_norm_2=float(np.linalg.norm(residual)),
                stationarity_norm_2=float(np.linalg.norm(A.T @ residual + lam * x)),
                regularization=lam,
                objective=float(residual @ residual + lam * (x @ x)),
                unique_unregularized_solution=rank == A.shape[1],
            )
        elif op != "matrix":
            raise ValueError("rhs is required")
    elif op == "stability":
        if A.shape[0] != A.shape[1]:
            raise ValueError("stability requires a square state matrix")
        timebase = data.get("timebase", "continuous")
        if timebase not in {"continuous", "discrete"}:
            raise ValueError("timebase must be continuous or discrete")
        eig = np.linalg.eigvals(A)
        tol = float(data.get("tolerance", 1e-10))
        if not np.isfinite(tol) or tol <= 0:
            raise ValueError("tolerance must be positive and finite")
        margin = (
            float(-max(np.real(eig)))
            if timebase == "continuous"
            else float(1 - max(abs(eig)))
        )
        result.update(
            eigenvalues=[[float(x.real), float(x.imag)] for x in eig],
            timebase=timebase,
            margin=margin,
            classification="asymptotically-stable"
            if margin > tol
            else (
                "unstable" if margin < -tol else "boundary-or-numerically-unresolved"
            ),
            scope="numerical spectrum of the supplied linear matrix; no nonlinear or robust stability certificate",
        )
    elif op == "propagate-covariance":
        covariance = array(data["covariance"], 2)
        if covariance.shape != (A.shape[1], A.shape[1]) or not np.allclose(
            covariance, covariance.T, rtol=0, atol=1e-12
        ):
            raise ValueError(
                "covariance must be symmetric with size matching matrix columns"
            )
        eigenvalues = np.linalg.eigvalsh(covariance)
        if min(eigenvalues) < -1e-12:
            raise ValueError("covariance is not positive semidefinite within tolerance")
        propagated = A @ covariance @ A.T
        result.update(
            output_covariance=propagated.tolist(),
            input_min_eigenvalue=float(min(eigenvalues)),
            scope="linear propagation; if matrix is a Jacobian this is a local approximation",
        )
    else:
        raise ValueError("unknown operation")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="-", help="JSON file, or - for stdin")
    parser.add_argument(
        "--example", action="store_true", help="Print an example input and exit"
    )
    args = parser.parse_args()
    if args.example:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    try:
        source = sys.stdin.read() if args.input == "-" else Path(args.input).read_text()
        data = json.loads(source, parse_constant=reject_constant)
        if not isinstance(data, dict):
            raise TypeError("input must be a JSON object")
        result = compute(data)
        payload = {
            "status": "completed",
            "evidence": EVIDENCE,
            "result": result,
            "input_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "versions": {
                "python": platform.python_version(),
                **{name: importlib.metadata.version(name) for name in DEPENDENCIES},
            },
        }
        print(json.dumps(payload, indent=2, allow_nan=False))
        return 0
    except ImportError as exc:
        print(json.dumps({"status": "dependency_missing", "error": str(exc)}))
        return 3
    except (
        ValueError,
        TypeError,
        KeyError,
        IndexError,
        ArithmeticError,
        OSError,
        SyntaxError,
        RuntimeError,
        NotImplementedError,
    ) as exc:
        print(
            json.dumps(
                {
                    "status": "failed",
                    "error_type": type(exc).__name__,
                    "error": str(exc),
                }
            )
        )
        return 1


def reject_constant(value):
    raise ValueError(f"nonfinite JSON number: {value}")


if __name__ == "__main__":
    sys.exit(main())
