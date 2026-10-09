#!/usr/bin/env python3
"""Enumerate a small linear code over a prime field and find its minimum distance."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from itertools import product
from math import isqrt
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {"prime": 2, "generator": [[1, 1, 1, 1, 1]]}


def compute(data):
    p = data["prime"]
    if (
        type(p) is not int
        or not 2 <= p <= 251
        or any(p % d == 0 for d in range(2, isqrt(p) + 1))
    ):
        raise ValueError(
            "prime must be a prime integer between 2 and 251; extension fields are unsupported"
        )
    G = data["generator"]
    if not G or not G[0] or any(len(row) != len(G[0]) for row in G):
        raise ValueError("generator must be nonempty and rectangular")
    k, n = len(G), len(G[0])
    if p**k > 100000 or n > 1000 or p**k * n * k > 5000000:
        raise ValueError(
            "enumeration budget exceeded; use a specialized code algorithm"
        )
    if any(type(x) is not int or not 0 <= x < p for row in G for x in row):
        raise ValueError("generator entries must be integers in 0..prime-1")
    words = {
        tuple(sum(u[i] * G[i][j] for i in range(k)) % p for j in range(n))
        for u in product(range(p), repeat=k)
    }
    dimension, size = 0, len(words)
    while size > 1:
        dimension += 1
        size //= p
    nonzero = [w for w in words if any(w)]
    witness = (
        min(nonzero, key=lambda w: (sum(x != 0 for x in w), w)) if nonzero else None
    )
    distance = sum(x != 0 for x in witness) if witness else None
    return {
        "length": n,
        "dimension": dimension,
        "codewords": len(words),
        "minimum_distance": distance,
        "minimum_weight_witness": witness,
        "unique_error_radius": (distance - 1) // 2 if distance is not None else None,
        "zero_code_convention": "minimum nonzero weight undefined for the zero code",
        "messages_enumerated": p**k,
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
