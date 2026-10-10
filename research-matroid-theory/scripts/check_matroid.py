#!/usr/bin/env python3
"""Check every hereditary and exchange axiom in an explicitly listed finite independence system."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {
    "elements": 3,
    "independent_sets": [[], [0], [1], [2], [0, 1], [0, 2], [1, 2]],
    "weights": [3, 2, 1],
}

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


from itertools import combinations


def compute(data):
    n = data["elements"]
    if type(n) is not int or not 0 <= n <= 16:
        raise ValueError("elements must be in 0..16")
    family = set()
    for subset in data["independent_sets"]:
        if any(type(x) is not int or not 0 <= x < n for x in subset) or len(
            set(subset)
        ) != len(subset):
            raise ValueError("independent sets need distinct ground-set indices")
        family.add(frozenset(subset))
    if len(family) > 1024:
        raise ValueError("at most 1024 explicitly listed independent sets")
    if frozenset() not in family:
        return {"is_matroid": False, "failure": "empty set missing"}
    ordered = sorted(family, key=lambda s: (len(s), sorted(s)))
    for subset in ordered:
        for x in subset:
            if subset - {x} not in family:
                return {
                    "is_matroid": False,
                    "failure": "hereditary axiom",
                    "witness": sorted(subset),
                    "missing_subset": sorted(subset - {x}),
                }
    for small, large in combinations(ordered, 2):
        if len(small) < len(large) and not any(
            small | {x} in family for x in large - small
        ):
            return {
                "is_matroid": False,
                "failure": "exchange axiom",
                "witness": [sorted(small), sorted(large)],
            }
    rank = max(map(len, family))
    result = {
        "is_matroid": True,
        "rank": rank,
        "bases": [sorted(s) for s in ordered if len(s) == rank],
        "sets_checked": len(family),
    }
    if "weights" in data:
        weights = list(map(rational, data["weights"]))
        if len(weights) != n:
            raise ValueError("weights must match the ground set")
        chosen = frozenset()
        for x in sorted(range(n), key=lambda x: (-weights[x], x)):
            if weights[x] > 0 and chosen | {x} in family:
                chosen = chosen | {x}
        weight = sum((weights[x] for x in chosen), Fraction(0))
        optimum = max(sum((weights[x] for x in s), Fraction(0)) for s in family)
        result.update(
            greedy_independent_set=sorted(chosen),
            greedy_weight=str(weight),
            exhaustive_optimum=str(optimum),
            greedy_verified=weight == optimum,
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
