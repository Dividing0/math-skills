#!/usr/bin/env python3
"""Compute rational planar orientations and convex hulls with exact area."""

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
    "operation": "convex-hull",
    "points": [[0, 0], [1, 0], [1, 1], [0, 1], ["1/2", "1/2"]],
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


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def compute(data):
    points = [tuple(map(rational, p)) for p in data["points"]]
    if not points or any(len(p) != 2 for p in points) or len(points) > 10000:
        raise ValueError("supply 1..10000 planar points")
    if data["operation"] == "orientation":
        if len(points) != 3:
            raise ValueError("orientation requires exactly three points")
        value = cross(*points)
        return {"determinant": str(value), "orientation": (value > 0) - (value < 0)}
    if data["operation"] != "convex-hull":
        raise ValueError("operation must be orientation or convex-hull")
    unique = sorted(set(points))
    if len(unique) == 1:
        hull = unique
    else:
        lower, upper = [], []
        for p in unique:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        for p in reversed(unique):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        hull = lower[:-1] + upper[:-1]
    area = (
        abs(sum(a[0] * b[1] - a[1] * b[0] for a, b in zip(hull, hull[1:] + hull[:1])))
        / 2
    )
    return {
        "hull": [list(map(str, p)) for p in hull],
        "area": str(area),
        "boundary_policy": "counterclockwise extreme vertices; collinear interior points removed",
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
