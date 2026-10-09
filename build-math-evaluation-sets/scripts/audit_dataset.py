#!/usr/bin/env python3
"""Audit task IDs, duplicate prompts, split leakage and evaluation score coverage."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from collections import Counter, defaultdict
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = "dataset-audit-not-capability-proof"
EXAMPLE = {
    "tasks": [
        {
            "id": "a",
            "prompt": "Prove P.",
            "split": "train",
            "family": "p",
            "category": "proof",
        },
        {
            "id": "b",
            "prompt": "Prove  P.",
            "split": "test",
            "family": "p",
            "category": "proof",
        },
    ],
    "scores": [{"id": "b", "score": 1}],
}


def compute(data):
    tasks = data["tasks"]
    if not tasks:
        raise ValueError("tasks must not be empty")
    by_id = {}
    prompts, groups = defaultdict(list), defaultdict(set)
    for row in tasks:
        key, prompt, split = row["id"], row["prompt"], row["split"]
        if (
            any(not isinstance(v, str) or not v.strip() for v in (key, prompt, split))
            or key in by_id
        ):
            raise ValueError(
                "IDs must be unique; id, prompt and split must be nonempty strings"
            )
        by_id[key] = row
        prompts[" ".join(prompt.split()).casefold()].append(key)
        if "family" in row:
            groups[row["family"]].add(split)
    result = {
        "tasks": len(tasks),
        "split_counts": dict(Counter(row["split"] for row in tasks)),
        "duplicate_prompt_ids": [ids for ids in prompts.values() if len(ids) > 1],
        "families_crossing_splits": {
            key: sorted(values) for key, values in groups.items() if len(values) > 1
        },
        "scope": "lexical duplicates and declared families; semantic equivalence and rubric correctness need review",
    }
    if "scores" in data:
        scores = {}
        categories = defaultdict(list)
        for row in data["scores"]:
            key, value = row["id"], row["score"]
            if (
                key not in by_id
                or key in scores
                or type(value) not in (int, float)
                or not math.isfinite(value)
                or not 0 <= value <= 1
            ):
                raise ValueError(
                    "scores need unique known IDs and finite values in [0,1]"
                )
            scores[key] = value
            categories[by_id[key].get("category", "uncategorized")].append(value)
        result["missing_score_ids"] = sorted(set(by_id) - set(scores))
        result["mean_score"] = sum(scores.values()) / len(scores) if scores else None
        result["category_scores"] = {
            key: {"n": len(values), "mean": sum(values) / len(values)}
            for key, values in categories.items()
        }
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
