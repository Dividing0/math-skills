#!/usr/bin/env python3
"""Compute exact generalized CRT solutions and Bezout witnesses."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {"operation": "crt", "congruences": [[2, 6], [5, 9]]}


def integer(value):
    if type(value) is not int:
        raise TypeError("inputs must be JSON integers")
    return value


def bezout(a, b):
    r, s, t, u, v, w = a, 1, 0, b, 0, 1
    while u:
        q = r // u
        r, s, t, u, v, w = u, v, w, r - q * u, s - q * v, t - q * w
    return (r, s, t) if r >= 0 else (-r, -s, -t)


def compute(data):
    if data["operation"] == "bezout":
        a, b = integer(data["a"]), integer(data["b"])
        g, x, y = bezout(a, b)
        return {"gcd": g, "x": x, "y": y, "identity_verified": a * x + b * y == g}
    if data["operation"] != "crt":
        raise ValueError("operation must be bezout or crt")
    pairs = data["congruences"]
    if not pairs:
        raise ValueError("at least one [residue, positive_modulus] is required")
    residue, modulus = 0, 1
    for pair in pairs:
        if len(pair) != 2:
            raise ValueError("each congruence must have two entries")
        a, m = map(integer, pair)
        if m <= 0:
            raise ValueError("moduli must be positive")
        g = math.gcd(modulus, m)
        if (a - residue) % g:
            return {"consistent": False, "conflict": pair}
        reduced = m // g
        k = (
            0
            if reduced == 1
            else ((a - residue) // g * pow(modulus // g, -1, reduced)) % reduced
        )
        residue += modulus * k
        modulus *= reduced
        residue %= modulus
    return {
        "consistent": True,
        "residue": residue,
        "modulus": modulus,
        "verified": all((residue - a) % m == 0 for a, m in pairs),
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
