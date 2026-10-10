#!/usr/bin/env python3
"""Solve finite linear programs, discrete transport and polynomial ODE initial-value problems."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("numpy", "scipy")
EVIDENCE = "numerical-evidence"
EXAMPLE = {
    "operation": "polynomial-ivp",
    "initial": [1],
    "powers": [[1]],
    "coefficients": [[-2]],
    "times": [0, 0.5, 1],
}


def compute(data):
    import numpy as np
    from scipy.integrate import solve_ivp
    from scipy.optimize import linprog
    from scipy.sparse import csr_matrix, eye, kron, vstack

    def array(values, ndim):
        a = np.asarray(values, dtype=float)
        if a.ndim != ndim or not a.size or not np.isfinite(a).all():
            raise ValueError(
                "arrays must be nonempty, finite and have the declared dimensions"
            )
        return a

    op = data["operation"]
    if op in {"linear-program", "transport"}:
        cost = None
        if op == "linear-program":
            c = array(data["c"], 1)
            A = array(data["A_ub"], 2) if "A_ub" in data else None
            b = array(data["b_ub"], 1) if "b_ub" in data else None
            E = array(data["A_eq"], 2) if "A_eq" in data else None
            f = array(data["b_eq"], 1) if "b_eq" in data else None
            bounds = data.get("bounds", [(0, None)] * len(c))
        else:
            cost = array(data["cost"], 2)
            source, target = array(data["source"], 1), array(data["target"], 1)
            m, n = cost.shape
            if (
                cost.size > 10000
                or len(source) != m
                or len(target) != n
                or min(source) < 0
                or min(target) < 0
            ):
                raise ValueError("invalid transport dimensions or masses")
            if abs(source.sum() - target.sum()) > 1e-12 * max(
                1, source.sum(), target.sum()
            ):
                raise ValueError("transport masses must have equal totals")
            c = cost.ravel()
            E = vstack(
                [
                    kron(eye(m), csr_matrix(np.ones((1, n)))),
                    kron(csr_matrix(np.ones((1, m))), eye(n)),
                ],
                format="csr",
            )
            f = np.concatenate([source, target])
            A, b, bounds = None, None, [(0, None)] * len(c)
        if len(c) > 10000:
            raise ValueError("at most 10000 LP variables")
        fit = linprog(c, A_ub=A, b_ub=b, A_eq=E, b_eq=f, bounds=bounds, method="highs")
        result = {
            "success": bool(fit.success),
            "solver_status": int(fit.status),
            "message": fit.message,
        }
        if not fit.success:
            return result
        x = fit.x
        result.update(
            solution=x.tolist(),
            objective=float(c @ x),
            max_inequality_violation=float(max(0, np.max(A @ x - b)))
            if A is not None
            else 0.0,
            max_equality_residual=float(np.max(abs(E @ x - f)))
            if E is not None
            else 0.0,
        )
        result["bound_violation"] = float(
            max(
                [0]
                + [
                    max(
                        0,
                        (low - v) if low is not None else 0,
                        (v - high) if high is not None else 0,
                    )
                    for v, (low, high) in zip(x, bounds)
                ]
            )
        )
        if cost is not None:
            result["plan"] = x.reshape(cost.shape).tolist()
        return result
    if op != "polynomial-ivp":
        raise ValueError("unknown operation")
    y0 = array(data["initial"], 1)
    powers = np.asarray(data["powers"])
    coefficients = array(data["coefficients"], 2)
    n = len(y0)
    if (
        powers.ndim != 2
        or powers.shape[1] != n
        or not np.issubdtype(powers.dtype, np.integer)
        or np.any(powers < 0)
        or np.any(powers > 20)
    ):
        raise ValueError(
            "powers must be nonnegative integer exponent rows, with one column per state"
        )
    if coefficients.shape != (n, len(powers)):
        raise ValueError(
            "coefficients must have one row per state and one column per monomial"
        )
    times = array(data["times"], 1)
    if len(times) < 2 or len(times) > 10000 or np.any(np.diff(times) <= 0):
        raise ValueError("times must be strictly increasing, with 2..10000 entries")
    rtol, atol = float(data.get("rtol", 1e-8)), float(data.get("atol", 1e-10))
    if not np.isfinite([rtol, atol]).all() or rtol <= 0 or atol <= 0:
        raise ValueError("tolerances must be finite and positive")

    def rhs(_time, y):
        value = coefficients @ np.prod(y[None, :] ** powers, axis=1)
        if not np.isfinite(value).all():
            raise ValueError("nonfinite polynomial vector field")
        return value

    fit = solve_ivp(
        rhs,
        (times[0], times[-1]),
        y0,
        t_eval=times,
        rtol=rtol,
        atol=atol,
        method=data.get("method", "RK45"),
    )
    return {
        "success": bool(fit.success),
        "message": fit.message,
        "times": fit.t.tolist(),
        "states": fit.y.T.tolist(),
        "evaluations": fit.nfev,
        "rtol": rtol,
        "atol": atol,
        "scope": "numerical autonomous polynomial IVP; no global error or existence certificate",
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
        source = (
            sys.stdin.read()
            if args.input == "-"
            else Path(args.input).read_text(encoding="utf-8-sig")
        )
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
