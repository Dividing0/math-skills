#!/usr/bin/env python3
"""Find pure equilibria and check supplied mixed strategies in a rational bimatrix game."""

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
    "row_payoffs": [[1, -1], [-1, 1]],
    "column_payoffs": [[-1, 1], [1, -1]],
    "row_strategy": ["1/2", "1/2"],
    "column_strategy": ["1/2", "1/2"],
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
    A, B = matrix(data["row_payoffs"]), matrix(data["column_payoffs"])
    m, n = len(A), len(A[0])
    if len(B) != m or len(B[0]) != n:
        raise ValueError("payoff matrices must have equal shapes")
    pure = [
        [i, j]
        for i in range(m)
        for j in range(n)
        if A[i][j] == max(A[k][j] for k in range(m)) and B[i][j] == max(B[i])
    ]
    result = {
        "pure_equilibria": pure,
        "scope": "two-player normal form with independent mixed strategies",
    }
    if "row_strategy" in data or "column_strategy" in data:
        x, y = (
            list(map(rational, data["row_strategy"])),
            list(map(rational, data["column_strategy"])),
        )
        if (
            len(x) != m
            or len(y) != n
            or any(v < 0 for v in x + y)
            or sum(x) != 1
            or sum(y) != 1
        ):
            raise ValueError(
                "strategies must be probability vectors of matching dimensions"
            )
        row = [sum(A[i][j] * y[j] for j in range(n)) for i in range(m)]
        column = [sum(B[i][j] * x[i] for i in range(m)) for j in range(n)]
        u, v = sum(a * b for a, b in zip(x, row)), sum(a * b for a, b in zip(y, column))
        regrets = [max(row) - u, max(column) - v]
        result.update(
            mixed_equilibrium=all(r == 0 for r in regrets),
            payoffs=[str(u), str(v)],
            regrets=list(map(str, regrets)),
            row_deviation_payoffs=list(map(str, row)),
            column_deviation_payoffs=list(map(str, column)),
        )
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
