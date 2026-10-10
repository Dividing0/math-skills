#!/usr/bin/env python3
"""Evaluate exact stationary M/M/1 queue formulas with an explicit stability check."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-model-formulas-under-stationary-MM1-assumptions"
EXAMPLE = {"arrival_rate": 2, "service_rate": 3, "population": 2}

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
    arrival, service = rational(data["arrival_rate"]), rational(data["service_rate"])
    if arrival < 0 or service <= 0:
        raise ValueError("arrival rate must be nonnegative and service rate positive")
    rho = arrival / service
    if rho >= 1:
        return {
            "stationary": False,
            "rho": str(rho),
            "reason": "arrival rate must be less than service rate",
        }
    n = data.get("population", 0)
    if type(n) is not int or not 0 <= n <= 10000:
        raise ValueError("population must be an integer in 0..10000")
    L, Lq = rho / (1 - rho), rho * rho / (1 - rho)
    W, Wq = 1 / (service - arrival), rho / (service - arrival)
    return {
        "stationary": True,
        "rho": str(rho),
        "L": str(L),
        "Lq": str(Lq),
        "W": str(W),
        "Wq": str(Wq),
        "population_probability": str((1 - rho) * rho**n),
        "population": n,
        "little_law_residual": str(L - arrival * W),
        "scope": "Poisson arrivals, independent exponential service, one server, infinite waiting room, stationary regime; at zero arrivals W describes a hypothetical tagged arrival",
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
