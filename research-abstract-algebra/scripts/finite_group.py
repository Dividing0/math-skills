#!/usr/bin/env python3
"""Exhaustively check a finite operation table and report group invariants."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from itertools import product
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {"table": [[0, 1, 2], [1, 2, 0], [2, 0, 1]]}


def compute(data):
    table = data["table"]
    n = len(table)
    if not 1 <= n <= 80 or any(len(row) != n for row in table):
        raise ValueError("table must be square, with 1..80 elements indexed 0..n-1")
    if any(type(x) is not int or not 0 <= x < n for row in table for x in row):
        raise ValueError("entries must be integer element indices")
    for a, b, c in product(range(n), repeat=3):
        if table[table[a][b]][c] != table[a][table[b][c]]:
            return {"is_group": False, "failure": "associativity", "witness": [a, b, c]}
    identities = [
        e for e in range(n) if all(table[e][a] == a == table[a][e] for a in range(n))
    ]
    if not identities:
        return {"is_group": False, "failure": "no two-sided identity"}
    e = identities[0]
    inverses = []
    for a in range(n):
        candidates = [b for b in range(n) if table[a][b] == e == table[b][a]]
        if not candidates:
            return {"is_group": False, "failure": "no inverse", "witness": a}
        inverses.append(candidates[0])
    orders = []
    for a in range(n):
        value = e
        for k in range(1, n + 1):
            value = table[value][a]
            if value == e:
                orders.append(k)
                break
    center = [a for a in range(n) if all(table[a][b] == table[b][a] for b in range(n))]
    classes = {
        tuple(sorted({table[table[g][a]][inverses[g]] for g in range(n)}))
        for a in range(n)
    }
    return {
        "is_group": True,
        "order": n,
        "identity": e,
        "inverses": inverses,
        "element_orders": orders,
        "abelian": len(center) == n,
        "center": center,
        "conjugacy_classes": sorted(classes),
        "triples_checked": n**3,
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
