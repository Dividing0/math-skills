#!/usr/bin/env python3
"""Bracket the extinction probability of a finite-support Galton-Watson process with exact rationals."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-rational-extinction-bound-under-model-assumptions"
EXAMPLE = {"offspring_probabilities": ["1/4", 0, "3/4"], "bisections": 80}

from fractions import Fraction


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
    probabilities = list(map(rational, data["offspring_probabilities"]))
    if (
        not 1 <= len(probabilities) <= 21
        or any(p < 0 for p in probabilities)
        or sum(probabilities) != 1
    ):
        raise ValueError(
            "supply probabilities for offspring counts 0..20, nonnegative with exact sum one"
        )
    mean = sum(k * p for k, p in enumerate(probabilities))
    if probabilities[0] == 0:
        lower = upper = Fraction(0)
        reason = (
            "at least one child almost surely; extinction impossible from one ancestor"
        )
    elif mean <= 1:
        lower = upper = Fraction(1)
        reason = "subcritical or nondegenerate critical finite-support offspring law"
    else:

        def residual(q):
            value = Fraction(0)
            for p in reversed(probabilities):
                value = value * q + p
            return value - q

        lower, upper = Fraction(0), Fraction(1, 2)
        for _ in range(512):
            if residual(upper) < 0:
                break
            upper = (upper + 1) / 2
        else:
            raise ValueError(
                "unable to bracket nontrivial root within 512 exact refinements"
            )
        steps = data.get("bisections", 80)
        if type(steps) is not int or not 1 <= steps <= 256:
            raise ValueError("bisections must be an integer in 1..256")
        for _ in range(steps):
            middle = (lower + upper) / 2
            value = residual(middle)
            if value == 0:
                lower = upper = middle
                break
            if value > 0:
                lower = middle
            else:
                upper = middle
        if not residual(lower) >= 0 >= residual(upper):
            raise ArithmeticError("bracket sign verification failed")
        reason = "least PGF fixed point: positive p0, mean>1 and strict convexity give a unique root below one"
    return {
        "mean_offspring": str(mean),
        "extinction_lower": str(lower),
        "extinction_upper": str(upper),
        "interval_width": str(upper - lower),
        "reason": reason,
        "scope": "one ancestor, independent identically distributed offspring, finite-support Galton-Watson model",
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
