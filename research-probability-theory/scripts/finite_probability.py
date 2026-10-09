#!/usr/bin/env python3
"""Compute exact finite joint-law moments, dependence and information quantities."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from fractions import Fraction
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-law-with-numerical-entropies"
EXAMPLE = {
    "outcomes": [
        {"x": -1, "y": 1, "p": "1/3"},
        {"x": 0, "y": 0, "p": "1/3"},
        {"x": 1, "y": 1, "p": "1/3"},
    ]
}


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise TypeError(
            "use integers or rational strings for exact probabilities and values"
        )
    return Fraction(value)


def compute(data):
    rows = data["outcomes"]
    if not rows:
        raise ValueError("outcomes must be nonempty")
    joint = {}
    for row in rows:
        x, y, p = rational(row["x"]), rational(row["y"]), rational(row["p"])
        if p < 0:
            raise ValueError("negative probability")
        joint[x, y] = joint.get((x, y), Fraction(0)) + p
    if sum(joint.values()) != 1:
        raise ValueError("probabilities must sum exactly to one")
    xs, ys = sorted({x for x, _ in joint}), sorted({y for _, y in joint})
    px = {x: sum(p for (a, _), p in joint.items() if a == x) for x in xs}
    py = {y: sum(p for (_, b), p in joint.items() if b == y) for y in ys}
    ex = sum(x * p for x, p in px.items())
    ey = sum(y * p for y, p in py.items())
    covariance = sum(x * y * p for (x, y), p in joint.items()) - ex * ey
    independent = all(joint.get((x, y), 0) == px[x] * py[y] for x in xs for y in ys)

    def entropy(probabilities):
        return -sum(float(p) * math.log2(p) for p in probabilities if p > 0)

    hx, hy, hxy = entropy(px.values()), entropy(py.values()), entropy(joint.values())
    return {
        "E_X": str(ex),
        "E_Y": str(ey),
        "covariance": str(covariance),
        "independent": independent,
        "marginal_X": [{"value": str(x), "p": str(p)} for x, p in px.items()],
        "marginal_Y": [{"value": str(y), "p": str(p)} for y, p in py.items()],
        "entropy_X_bits": hx,
        "entropy_Y_bits": hy,
        "joint_entropy_bits": hxy,
        "mutual_information_bits": hx + hy - hxy,
        "scope": "moments and independence exact; logarithmic quantities use floating arithmetic",
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
