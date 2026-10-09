#!/usr/bin/env python3
"""Compute conditional finite-class Hoeffding bounds from bounded binary losses."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = (
    "conditional-probabilistic-bound; assumptions supplied, not established by data"
)
EXAMPLE = {
    "losses": [[0, 1, 0, 0], [1, 1, 0, 1]],
    "delta": 0.05,
    "class_size": 2,
    "iid": True,
    "class_fixed_before_data": True,
}


def compute(data):
    losses = data["losses"]
    if (
        not isinstance(losses, list)
        or not losses
        or any(not isinstance(row, list) for row in losses)
    ):
        raise ValueError("losses must be hypothesis rows on a common sample")
    n, rows = len(losses[0]), len(losses)
    if n < 1 or rows * n > 1000000 or any(len(row) != n for row in losses):
        raise ValueError(
            "loss matrix must be rectangular, nonempty, and at most one million entries"
        )
    if any(
        type(v) not in (int, float) or v not in (0, 1) for row in losses for v in row
    ):
        raise ValueError("this helper accepts only binary zero-one losses")
    size, delta = data.get("class_size", rows), data.get("delta", 0.05)
    if type(size) is not int or not rows <= size <= 10**12:
        raise ValueError(
            "class_size must be a predeclared integer >= supplied hypotheses and <= 10**12"
        )
    if type(delta) not in (int, float) or not math.isfinite(delta) or not 0 < delta < 1:
        raise ValueError("delta must be in (0,1)")
    if data.get("iid") is not True or data.get("class_fixed_before_data") is not True:
        raise ValueError(
            "bound requires explicit IID data and a hypothesis class fixed before these data"
        )
    empirical = [sum(row) / n for row in losses]
    radius = math.sqrt((math.log(2) + math.log(size) - math.log(delta)) / (2 * n))
    selected = min(range(rows), key=lambda i: empirical[i])
    return {
        "sample_size": n,
        "class_size": size,
        "delta": delta,
        "uniform_radius": radius,
        "empirical_risks": empirical,
        "risk_intervals": [[max(0, r - radius), min(1, r + radius)] for r in empirical],
        "selected_hypothesis": selected,
        "excess_risk_bound_over_supplied_candidates": min(1, 2 * radius),
        "scope": "simultaneous two-sided Hoeffding plus union bound; IID/fixed-class assumptions cannot be verified from losses; no unrestricted model-class guarantee",
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
