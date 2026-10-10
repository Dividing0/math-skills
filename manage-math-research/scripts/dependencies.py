#!/usr/bin/env python3
"""Audit a mathematical dependency ledger for cycles and unresolved prerequisites."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from graphlib import CycleError, TopologicalSorter
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "structural-audit"
EXAMPLE = {
    "claims": [
        {"id": "lemma", "status": "conjecture"},
        {"id": "theorem", "status": "proved", "depends_on": ["lemma"]},
    ]
}


def compute(data):
    entries = data["claims"]
    ids = [row["id"] for row in entries]
    if any(not isinstance(x, str) or not x for x in ids) or len(set(ids)) != len(ids):
        raise ValueError("claim IDs must be unique nonempty strings")
    claims = {row["id"]: row for row in entries}
    graph = {key: set(row.get("depends_on", [])) for key, row in claims.items()}
    missing = sorted(set().union(*graph.values()) - set(ids)) if graph else []
    if missing:
        raise ValueError(f"unknown dependencies: {missing}")
    allowed = {"proved", "assumed", "conjecture", "blocked", "observation"}
    if any(row.get("status") not in allowed for row in entries):
        raise ValueError(f"status must be one of {sorted(allowed)}")
    try:
        order = list(TopologicalSorter(graph).static_order())
    except CycleError as exc:
        return {
            "acyclic": False,
            "cycle": exc.args[1],
            "scope": "ledger consistency only",
        }
    trusted = set()
    unsupported = []
    for key in order:
        state = claims[key]["status"]
        if state == "assumed" or (state == "proved" and graph[key] <= trusted):
            trusted.add(key)
        elif state == "proved":
            unsupported.append(
                {"id": key, "unresolved_dependencies": sorted(graph[key] - trusted)}
            )
    ready = [
        key
        for key in order
        if claims[key]["status"] in {"conjecture", "blocked"} and graph[key] <= trusted
    ]
    return {
        "acyclic": True,
        "order": order,
        "unsupported_proved_claims": unsupported,
        "ready_obligations": ready,
        "assumptions": [key for key in order if claims[key]["status"] == "assumed"],
        "scope": "declared dependencies and statuses; proof content is not verified",
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
