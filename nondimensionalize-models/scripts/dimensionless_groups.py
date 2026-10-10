#!/usr/bin/env python3
"""Find exact rational dimensionless exponent vectors from a base-unit matrix."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from fractions import Fraction
from pathlib import Path

DEPENDENCIES = ("sympy",)
EVIDENCE = "exact-finite-computation"
EXAMPLE = {
    "quantities": ["length", "time", "speed"],
    "dimensions": [[1, 0, 1], [0, 1, -1]],
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
    import sympy as sp

    values = matrix(data["dimensions"])
    names = data["quantities"]
    if len(names) != len(values[0]) or len(set(names)) != len(names):
        raise ValueError("quantities must be unique and match dimension-matrix columns")
    A = sp.Matrix(
        [[sp.Rational(v.numerator, v.denominator) for v in row] for row in values]
    )
    basis = A.nullspace()
    groups = []
    for vector in basis:
        scale = sp.ilcm(*[v.q for v in vector]) if len(vector) > 1 else vector[0].q
        integers = [int(scale * v) for v in vector]
        groups.append(
            {
                "exponents": dict(zip(names, integers)),
                "dimension_residual": list(map(str, A * sp.Matrix(integers))),
            }
        )
    return {
        "rank": A.rank(),
        "independent_groups": len(basis),
        "groups": groups,
        "scope": "dimensionless monomials; no constitutive law or asymptotic reduction is proved",
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
