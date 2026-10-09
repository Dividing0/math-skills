#!/usr/bin/env python3
"""Check exact rational linear-system and linear-program optimality certificates."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from fractions import Fraction
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {
    "operation": "linear-program",
    "A": [[1, 1]],
    "b": [1],
    "c": [1, 1],
    "x": [1, 0],
    "y": [1],
}


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise TypeError("exact inputs must be integers or rational/decimal strings")
    return Fraction(value)


def matrix(values):
    if (
        not isinstance(values, list)
        or not values
        or not all(isinstance(row, list) for row in values)
    ):
        raise ValueError("matrix must have at least one row")
    width = len(values[0])
    if not width or any(len(row) != width for row in values):
        raise ValueError("matrix must be nonempty and rectangular")
    return [[rational(x) for x in row] for row in values]


def compute(data):
    A = matrix(data["A"])
    b = list(map(rational, data["b"]))
    x = list(map(rational, data["x"]))
    if len(b) != len(A) or len(x) != len(A[0]):
        raise ValueError("A, b and x dimensions differ")
    Ax = [sum(a * v for a, v in zip(row, x)) for row in A]
    if data["operation"] == "linear-system":
        residual = [v - w for v, w in zip(Ax, b)]
        return {
            "valid": all(v == 0 for v in residual),
            "residual": list(map(str, residual)),
            "scope": "Ax=b only; uniqueness is not certified",
        }
    if data["operation"] != "linear-program":
        raise ValueError("operation must be linear-system or linear-program")
    c = list(map(rational, data["c"]))
    y = list(map(rational, data["y"]))
    if len(c) != len(x) or len(y) != len(b):
        raise ValueError("c or y has wrong dimension")
    primal_slack = [v - w for v, w in zip(Ax, b)]
    dual_slack = [
        c[j] - sum(A[i][j] * y[i] for i in range(len(A))) for j in range(len(x))
    ]
    primal = sum(a * v for a, v in zip(c, x))
    dual = sum(a * v for a, v in zip(b, y))
    feasible = all(v >= 0 for v in x + y + primal_slack + dual_slack)
    return {
        "convention": "min c^T x: Ax>=b, x>=0; max b^T y: A^T y<=c, y>=0",
        "valid": feasible and primal == dual,
        "feasible": feasible,
        "primal_objective": str(primal),
        "dual_objective": str(dual),
        "gap": str(primal - dual),
        "primal_slack": list(map(str, primal_slack)),
        "dual_slack": list(map(str, dual_slack)),
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
