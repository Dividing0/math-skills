#!/usr/bin/env python3
"""Compute unreduced homology dimensions of a finite simplicial complex over F_p."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from itertools import combinations
from math import isqrt
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {"prime": 2, "simplices": [[0, 1], [1, 2], [0, 2]]}


def rank_mod(matrix, columns, p):
    a = [row[:] for row in matrix]
    rank = 0
    for j in range(columns):
        pivot = next((i for i in range(rank, len(a)) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][j], -1, p)
        a[rank] = [x * inv % p for x in a[rank]]
        for i in range(rank + 1, len(a)):
            scale = a[i][j]
            a[i] = [(x - scale * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def compute(data):
    p = data.get("prime", 2)
    if (
        type(p) is not int
        or not 2 <= p <= 251
        or any(p % d == 0 for d in range(2, isqrt(p) + 1))
    ):
        raise ValueError("prime must be a prime integer in 2..251")
    faces = set()
    for simplex in data["simplices"]:
        if (
            not simplex
            or len(simplex) > 10
            or any(type(x) is not int for x in simplex)
            or len(set(simplex)) != len(simplex)
        ):
            raise ValueError("simplices need 1..10 distinct integer vertex labels")
        for k in range(1, len(simplex) + 1):
            faces.update(combinations(sorted(simplex), k))
        if len(faces) > 2000:
            raise ValueError("face budget exceeded")
    if not faces:
        return {"prime": p, "betti": [], "euler_characteristic": 0, "reduced": False}
    dim = max(map(len, faces)) - 1
    levels = [sorted(s for s in faces if len(s) == k + 1) for k in range(dim + 1)]
    boundaries, ranks = {}, [0]
    for k in range(1, dim + 1):
        rows = {face: i for i, face in enumerate(levels[k - 1])}
        boundary = [[0] * len(levels[k]) for _ in rows]
        for j, simplex in enumerate(levels[k]):
            for i in range(k + 1):
                boundary[rows[simplex[:i] + simplex[i + 1 :]]][j] = (-1) ** i % p
        boundaries[k] = boundary
        ranks.append(rank_mod(boundary, len(levels[k]), p))
        if k > 1:
            previous = boundaries[k - 1]
            for row in previous:
                for j in range(len(levels[k])):
                    if sum(row[i] * boundary[i][j] for i in range(len(boundary))) % p:
                        raise ArithmeticError("boundary composition was nonzero")
    betti = [
        len(levels[k]) - ranks[k] - (ranks[k + 1] if k < dim else 0)
        for k in range(dim + 1)
    ]
    euler = sum((-1) ** k * len(level) for k, level in enumerate(levels))
    if euler != sum((-1) ** k * b for k, b in enumerate(betti)):
        raise ArithmeticError("Euler characteristic check failed")
    return {
        "prime": p,
        "betti": betti,
        "simplex_counts": list(map(len, levels)),
        "boundary_ranks": ranks,
        "euler_characteristic": euler,
        "reduced": False,
        "boundary_squared_zero": True,
        "scope": "homology over F_p; integer torsion is not computed",
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
