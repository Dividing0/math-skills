#!/usr/bin/env python3
"""Solve stationary distributions of a finite rational Markov chain without claiming mixing."""

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
EXAMPLE = {"transition": [[0, 1], [1, 0]], "initial": [1, 0], "steps": 3}


def compute(data):
    import sympy as sp

    def rational(value):
        if isinstance(value, bool) or not isinstance(value, (str, int)):
            raise TypeError(
                "transition probabilities must be integers or rational strings"
            )
        return sp.Rational(Fraction(value))

    rows = data["transition"]
    n = len(rows)
    if not 1 <= n <= 50 or any(len(row) != n for row in rows):
        raise ValueError("transition matrix must be square with 1..50 states")
    P = sp.Matrix([[rational(v) for v in row] for row in rows])
    if any(v < 0 for v in P) or any(sum(P.row(i)) != 1 for i in range(n)):
        raise ValueError("matrix must be row stochastic exactly")
    equations = (P.T - sp.eye(n)).col_join(sp.ones(1, n))
    rhs = sp.zeros(n, 1).col_join(sp.ones(1, 1))
    solution = sp.linsolve((equations, rhs))
    value = next(iter(solution))
    parameters = set().union(*(v.free_symbols for v in value))
    result = {
        "stationary_family": list(map(str, value)),
        "unique": not parameters,
        "free_parameters": sorted(map(str, parameters)),
        "probability_constraints": "each coordinate >=0",
        "scope": "stationary equations only; periodicity and convergence of powers are not inferred",
    }
    if not parameters:
        vector = sp.Matrix(value)
        result["stationary_distribution"] = list(map(str, value))
        result["residual"] = list(map(str, P.T * vector - vector))
    if "initial" in data:
        initial = sp.Matrix([rational(v) for v in data["initial"]])
        steps = data.get("steps", 1)
        if len(initial) != n or any(v < 0 for v in initial) or sum(initial) != 1:
            raise ValueError("initial must be a probability vector")
        if type(steps) is not int or not 0 <= steps <= 1000:
            raise ValueError("steps must be an integer in 0..1000")
        result["distribution_after_steps"] = list(map(str, (P.T**steps) * initial))
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
