#!/usr/bin/env python3
"""Check every point and pair in a finite block design."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {
    "v": 4,
    "k": 2,
    "lambda": 1,
    "blocks": [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]],
}


def compute(data):
    v, k, lam = data["v"], data["k"], data["lambda"]
    if (
        any(type(x) is not int for x in (v, k, lam))
        or not 2 <= k <= v <= 1000
        or lam < 1
    ):
        raise ValueError("require integers 2<=k<=v<=1000 and lambda>=1")
    blocks = data["blocks"]
    counts = Counter()
    point_counts = [0] * v
    seen = set()
    for block in blocks:
        if (
            len(block) != k
            or any(type(p) is not int or not 0 <= p < v for p in block)
            or len(set(block)) != k
        ):
            raise ValueError("blocks must contain k distinct point indices in 0..v-1")
        key = tuple(sorted(block))
        if key in seen and not data.get("allow_repeated_blocks", False):
            raise ValueError("repeated block without allow_repeated_blocks")
        seen.add(key)
        counts.update(combinations(key, 2))
        for p in block:
            point_counts[p] += 1
    failures = [
        {"pair": [a, b], "count": counts[a, b]}
        for a, b in combinations(range(v), 2)
        if counts[a, b] != lam
    ]
    return {
        "valid": not failures,
        "blocks": len(blocks),
        "point_counts": point_counts,
        "pairs_checked": v * (v - 1) // 2,
        "failing_pairs": failures,
        "necessary_integrality": (lam * (v - 1)) % (k - 1) == 0
        and (lam * v * (v - 1)) % (k * (k - 1)) == 0,
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
