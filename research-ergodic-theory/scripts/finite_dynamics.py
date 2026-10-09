#!/usr/bin/env python3
"""Classify a finite measure-preserving permutation and compute exact orbit averages."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from fractions import Fraction
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-dynamical-system-analysis"
EXAMPLE = {"permutation": [1, 2, 0], "observable": [0, 1, 5]}


def rational(value):
    if type(value) not in (int, str):
        raise TypeError("exact inputs must be integers or rational strings")
    return Fraction(value)


def compute(data):
    permutation = data["permutation"]
    n = len(permutation)
    if (
        not 1 <= n <= 10000
        or any(type(v) is not int for v in permutation)
        or sorted(permutation) != list(range(n))
    ):
        raise ValueError(
            "permutation must bijectively map 0..n-1, with 1..10000 states"
        )
    weights = list(map(rational, data.get("weights", [f"1/{n}"] * n)))
    observable = list(map(rational, data["observable"]))
    if (
        len(weights) != n
        or len(observable) != n
        or min(weights) < 0
        or sum(weights) != 1
    ):
        raise ValueError(
            "observable/weights must match states; weights form a probability law"
        )
    invariant = all(weights[i] == weights[permutation[i]] for i in range(n))
    if not invariant:
        return {
            "measure_preserving": False,
            "scope": "ergodicity and mixing not classified for a noninvariant supplied measure",
        }
    unseen = set(range(n))
    cycles, averages = [], [Fraction(0)] * n
    while unseen:
        start = min(unseen)
        cycle, current = [], start
        while current in unseen:
            unseen.remove(current)
            cycle.append(current)
            current = permutation[current]
        mean = sum((observable[i] for i in cycle), Fraction(0)) / len(cycle)
        for i in cycle:
            averages[i] = mean
        cycles.append(cycle)
    positive_cycles = [cycle for cycle in cycles if weights[cycle[0]] > 0]
    return {
        "measure_preserving": True,
        "cycles": cycles,
        "ergodic": len(positive_cycles) == 1,
        "mixing": sum(w > 0 for w in weights) == 1,
        "orbit_time_averages": list(map(str, averages)),
        "space_average": str(
            sum((w * f for w, f in zip(weights, observable)), Fraction(0))
        ),
        "scope": "finite invertible system only; zero-mass cycles do not affect almost-everywhere claims",
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
