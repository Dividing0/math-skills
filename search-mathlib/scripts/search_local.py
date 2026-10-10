#!/usr/bin/env python3
"""Search local Lean source for a literal query and return bounded file/line matches."""

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "local-source-search"
EXAMPLE = {"project": ".", "query": "theorem", "limit": 5}


def compute(data):
    project = Path(data["project"]).resolve()
    query = data["query"]
    limit = data.get("limit", 50)
    if (
        not project.is_dir()
        or not isinstance(query, str)
        or not query
        or type(limit) is not int
        or not 1 <= limit <= 1000
    ):
        raise ValueError(
            "project must exist; query must be nonempty; limit must be 1..1000"
        )
    roots = [project]
    mathlib = project / ".lake/packages/mathlib/Mathlib"
    if mathlib.is_dir():
        roots.append(mathlib)
    hits = []
    scanned = 0
    truncated = False
    for root in roots:
        for directory, dirs, files in os.walk(root):
            dirs[:] = sorted(
                d
                for d in dirs
                if not d.startswith(".")
                and d not in {"build", "venv", "node_modules", "__pycache__"}
            )
            for name in sorted(files):
                if not name.endswith(".lean"):
                    continue
                path = Path(directory) / name
                if path.is_symlink():
                    continue
                scanned += 1
                for line, text in enumerate(
                    path.read_text(encoding="utf-8", errors="replace").splitlines(), 1
                ):
                    if query in text:
                        if len(hits) == limit:
                            truncated = True
                            break
                        hits.append({"file": str(path), "line": line, "text": text})
                if truncated:
                    break
            if truncated:
                break
        if truncated:
            break
    return {
        "matches": hits,
        "files_scanned": scanned,
        "truncated": truncated,
        "scope": "literal source matches, including comments; candidates require local #check",
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
