#!/usr/bin/env python3
"""Capture or compare Lean pins and source hashes without changing a project."""

import argparse
import hashlib
import importlib.metadata
import json
import os
import platform
import sys
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = (
    "filesystem-snapshot; build and semantic compatibility require separate checks"
)
EXAMPLE = {"operation": "snapshot", "project": "."}


def compute(data):
    operation = data.get("operation", "snapshot")
    if operation == "compare":
        before, after = data["before"], data["after"]
        if not isinstance(before, dict) or not isinstance(after, dict):
            raise TypeError("before and after must be snapshot result objects")
        changes = {}
        for section in ("configuration", "sources"):
            a, b = before[section], after[section]
            if not isinstance(a, dict) or not isinstance(b, dict):
                raise TypeError("snapshot sections must be mappings")
            changes[section] = {
                "added": sorted(b.keys() - a.keys()),
                "removed": sorted(a.keys() - b.keys()),
                "changed": sorted(k for k in a.keys() & b.keys() if a[k] != b[k]),
            }
        return {
            "toolchain_before": before["toolchain"],
            "toolchain_after": after["toolchain"],
            "changes": changes,
            "scope": "content hashes only; no compatibility or build claim",
        }
    if operation != "snapshot":
        raise ValueError("operation must be snapshot or compare")
    root = Path(data["project"]).resolve()
    pin = root / "lean-toolchain"
    if not pin.is_file() or pin.is_symlink():
        raise ValueError("project must contain a regular lean-toolchain file")
    configuration = {}
    for name in (
        "lean-toolchain",
        "lakefile.toml",
        "lakefile.lean",
        "lake-manifest.json",
    ):
        path = root / name
        if path.is_file() and not path.is_symlink():
            configuration[name] = hashlib.sha256(path.read_bytes()).hexdigest()
    sources = {}

    for parent, directories, files in os.walk(root, followlinks=False):
        directories[:] = sorted(
            d
            for d in directories
            if not d.startswith(".")
            and d not in {"build", "node_modules", "venv"}
            and not (Path(parent) / d).is_symlink()
        )
        for name in sorted(files):
            path = Path(parent) / name
            if path.suffix == ".lean" and not path.is_symlink():
                if len(sources) >= 10000:
                    raise ValueError("at most 10000 Lean sources per snapshot")
                sources[path.relative_to(root).as_posix()] = hashlib.sha256(
                    path.read_bytes()
                ).hexdigest()
    return {
        "toolchain": pin.read_text(encoding="utf-8").strip(),
        "configuration": configuration,
        "sources": sources,
        "scope": "read-only snapshot; generated/dependency trees and symlinks excluded",
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
