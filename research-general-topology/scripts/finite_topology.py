#!/usr/bin/env python3
"""Validate a finite topology and compute separation and closure properties."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from itertools import combinations, product
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "exact-finite-computation"
EXAMPLE = {"points": 2, "opens": [[], [0], [0, 1]], "subset": [0]}


def compute(data):
    n = data["points"]
    if type(n) is not int or not 0 <= n <= 12:
        raise ValueError("points must be an integer in 0..12")
    universe = frozenset(range(n))
    opens = set()
    for subset in data["opens"]:
        if any(type(x) is not int or x not in universe for x in subset) or len(
            set(subset)
        ) != len(subset):
            raise ValueError("open sets must contain distinct point indices")
        opens.add(frozenset(subset))
    if len(opens) > 512:
        raise ValueError("at most 512 open sets are supported")
    if frozenset() not in opens or universe not in opens:
        return {"is_topology": False, "failure": "missing empty set or whole space"}
    for a, b in product(opens, repeat=2):
        if a | b not in opens or a & b not in opens:
            return {
                "is_topology": False,
                "failure": "union/intersection closure",
                "witness": [sorted(a), sorted(b)],
            }
    t0 = all(
        any((x in u) != (y in u) for u in opens) for x, y in combinations(range(n), 2)
    )
    t1 = all(universe - {x} in opens for x in range(n))
    hausdorff = all(
        any(x in u and y in v and not u & v for u, v in product(opens, repeat=2))
        for x, y in combinations(range(n), 2)
    )
    result = {
        "is_topology": True,
        "T0": t0,
        "T1": t1,
        "Hausdorff": hausdorff,
        "compact": True,
        "scope": "finite space only",
    }
    if "subset" in data:
        subset = frozenset(data["subset"])
        if not subset <= universe:
            raise ValueError("subset contains unknown points")
        closed = [universe - u for u in opens if subset <= universe - u]
        result["closure"] = sorted(set.intersection(*(set(c) for c in closed)))
        result["interior"] = sorted(set().union(*(u for u in opens if u <= subset)))
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
