#!/usr/bin/env python3
"""Measure empirical convergence orders from a supplied refinement/error table."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from itertools import pairwise
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "empirical-convergence"
EXAMPLE = {"steps": [0.25, 0.125, 0.0625], "errors": [0.0625, 0.015625, 0.00390625]}


def compute(data):
    h, errors = data["steps"], data["errors"]
    if len(h) != len(errors) or len(h) < 2:
        raise ValueError("need matching step/error sequences with at least two rows")
    h, errors = list(map(float, h)), list(map(float, errors))
    if any(not math.isfinite(v) or v <= 0 for v in h + errors):
        raise ValueError(
            "steps and errors must be finite and positive; exact zeros have undefined log rates"
        )
    if any(a <= b for a, b in pairwise(h)):
        raise ValueError("steps must be strictly decreasing")
    orders = [
        math.log(a / b) / math.log(x / y)
        for (x, y), (a, b) in zip(pairwise(h), pairwise(errors))
    ]
    return {
        "observed_orders": orders,
        "error_ratios": [a / b for a, b in pairwise(errors)],
        "scope": "empirical rates relative to supplied reference; no stability or convergence theorem",
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
