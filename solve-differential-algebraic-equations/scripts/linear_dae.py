#!/usr/bin/env python3
"""Solve a constant linear index-one DAE by elimination and backward Euler."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("numpy", "scipy")
EVIDENCE = "numerical-index-one-linear-DAE-evidence"
EXAMPLE = {
    "A": [[-1]],
    "B": [[1]],
    "C": [[1]],
    "D": [[1]],
    "f": [0],
    "g": [0],
    "initial": [1],
    "duration": 1,
    "steps": 40,
}


def compute(data):
    import numpy as np
    from scipy.linalg import expm

    def array(name, ndim):
        value = np.asarray(data[name], dtype=float)
        if value.ndim != ndim or not value.size or not np.isfinite(value).all():
            raise ValueError(
                f"{name} must be a finite nonempty {ndim}-dimensional array"
            )
        return value

    A, B, C, D = (array(name, 2) for name in ("A", "B", "C", "D"))
    f, g, x0 = (array(name, 1) for name in ("f", "g", "initial"))
    n, m = len(x0), len(g)
    if (
        n + m > 50
        or A.shape != (n, n)
        or B.shape != (n, m)
        or C.shape != (m, n)
        or D.shape != (m, m)
        or len(f) != n
    ):
        raise ValueError("incompatible DAE dimensions or more than 50 variables")
    condition = float(np.linalg.cond(D))
    if not math.isfinite(condition) or condition > 1e12:
        raise ValueError(
            "D must be nonsingular and well-conditioned for index-one elimination"
        )
    eliminated = np.linalg.solve(D, C)
    offset = np.linalg.solve(D, g)
    R, q = A - B @ eliminated, f - B @ offset
    z0 = -eliminated @ x0 - offset
    if "algebraic_initial" in data:
        supplied = array("algebraic_initial", 1)
        if supplied.shape != z0.shape or not np.allclose(
            supplied, z0, rtol=1e-10, atol=1e-12
        ):
            raise ValueError("inconsistent algebraic initial condition")
    steps, duration = data.get("steps", 40), data.get("duration", 1)
    if (
        type(steps) is not int
        or not 1 <= steps <= 10000
        or type(duration) not in (int, float)
        or not math.isfinite(duration)
        or duration <= 0
    ):
        raise ValueError("steps must be 1..10000 and duration positive finite")
    augmented = np.zeros((n + 1, n + 1))
    augmented[:n, :n], augmented[:n, n] = R, q
    exact = (expm(float(duration) * augmented) @ np.append(x0, 1))[:n]
    if not np.isfinite(exact).all():
        raise ValueError("matrix exponential produced nonfinite reference values")
    levels = []
    for count in (steps, 2 * steps):
        h = duration / count
        matrix = np.eye(n) - h * R
        step_condition = float(np.linalg.cond(matrix))
        if not math.isfinite(step_condition) or step_condition > 1e12:
            raise ValueError(
                "backward Euler step matrix is singular or ill-conditioned; reduce the step size"
            )
        x = x0.copy()
        z = z0.copy()
        algebraic_residual = differential_residual = 0.0
        for _ in range(count):
            old = x
            x = np.linalg.solve(matrix, old + h * q)
            z = -eliminated @ x - offset
            if not np.isfinite(x).all() or not np.isfinite(z).all():
                raise ValueError("backward Euler produced nonfinite states")
            algebraic_residual = max(
                algebraic_residual, float(np.max(np.abs(C @ x + D @ z + g)))
            )
            differential_residual = max(
                differential_residual,
                float(np.max(np.abs((x - old) / h - A @ x - B @ z - f))),
            )
        levels.append(
            {
                "steps": count,
                "terminal_x": x.tolist(),
                "terminal_z": z.tolist(),
                "terminal_error_inf": float(np.max(np.abs(x - exact))),
                "max_algebraic_residual": algebraic_residual,
                "max_discrete_differential_residual": differential_residual,
            }
        )
    errors = [level["terminal_error_inf"] for level in levels]
    return {
        "algebraic_initial": z0.tolist(),
        "D_condition_2": condition,
        "exact_terminal_x": exact.tolist(),
        "levels": levels,
        "observed_order": math.log2(errors[0] / errors[1]) if min(errors) > 0 else None,
        "scope": "x_prime=A*x+B*z+f, 0=C*x+D*z+g; constant coefficients and invertible D only",
    }


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
