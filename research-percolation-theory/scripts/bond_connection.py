#!/usr/bin/env python3
"""Enumerate exact two-terminal connection probabilities in a small independent bond-percolation graph."""

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
    "vertices": 3,
    "edges": [[0, 1], [1, 2], [0, 2]],
    "source": 0,
    "target": 2,
    "probability": "1/2",
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


def compute(data):
    n = data["vertices"]
    edges = data["edges"]
    source, target = data["source"], data["target"]
    if type(n) is not int or not 1 <= n <= 30 or len(edges) > 18:
        raise ValueError("require 1..30 vertices and at most 18 edges")
    if any(type(v) is not int or not 0 <= v < n for v in (source, target)):
        raise ValueError("source and target must be vertex indices")
    seen = set()
    for edge in edges:
        if (
            len(edge) != 2
            or any(type(v) is not int or not 0 <= v < n for v in edge)
            or edge[0] == edge[1]
        ):
            raise ValueError("edges must have distinct valid endpoints")
        key = tuple(sorted(edge))
        if key in seen:
            raise ValueError("parallel edges are not supported")
        seen.add(key)
    p = rational(data["probability"])
    if not 0 <= p <= 1:
        raise ValueError("bond probability must lie in [0,1]")
    m = len(edges)
    connected_counts = [0] * (m + 1)
    for mask in range(1 << m):
        adjacency = [[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            if mask & (1 << i):
                adjacency[u].append(v)
                adjacency[v].append(u)
        reached, queue = {source}, [source]
        while queue:
            for v in adjacency[queue.pop()]:
                if v not in reached:
                    reached.add(v)
                    queue.append(v)
        if target in reached:
            connected_counts[mask.bit_count()] += 1
    probability = sum(
        count * p**k * (1 - p) ** (m - k) for k, count in enumerate(connected_counts)
    )
    return {
        "connection_probability": str(probability),
        "connected_subsets_by_edge_count": connected_counts,
        "configurations_checked": 1 << m,
        "scope": "finite undirected graph with independent identically distributed bonds; no infinite-cluster threshold claim",
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
