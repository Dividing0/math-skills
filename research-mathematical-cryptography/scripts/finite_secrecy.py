#!/usr/bin/env python3
"""Exhaustively check perfect secrecy and decryptability of a finite cipher table."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from fractions import Fraction
from pathlib import Path

DEPENDENCIES = ()
EVIDENCE = (
    "exact-finite-information-theoretic-analysis; not computational-security evidence"
)
EXAMPLE = {"encryption_table": [[0, 1], [1, 0]], "key_probabilities": ["1/2", "1/2"]}


def rational(value):
    if type(value) not in (str, int):
        raise TypeError("probabilities must be integers or rational strings")
    return Fraction(value)


def compute(data):
    table = data["encryption_table"]
    if (
        not isinstance(table, list)
        or not 1 <= len(table) <= 128
        or any(not isinstance(row, list) for row in table)
    ):
        raise ValueError("table must contain 1..128 key rows")
    messages = len(table[0])
    if not 1 <= messages <= 128 or any(len(row) != messages for row in table):
        raise ValueError("table must be rectangular with 1..128 message columns")
    if any(type(c) not in (int, str) for row in table for c in row):
        raise TypeError("ciphertext labels must be integers or strings")
    probabilities = [
        rational(v)
        for v in data.get("key_probabilities", [f"1/{len(table)}"] * len(table))
    ]
    if (
        len(probabilities) != len(table)
        or any(p < 0 for p in probabilities)
        or sum(probabilities) != 1
    ):
        raise ValueError("key probabilities must be nonnegative and sum exactly to one")
    alphabet = list(dict.fromkeys(c for row in table for c in row))
    distributions = []
    for message in range(messages):
        distribution = {}
        for row, probability in zip(table, probabilities):
            ciphertext = row[message]
            distribution[ciphertext] = (
                distribution.get(ciphertext, Fraction(0)) + probability
            )
        distributions.append(distribution)
    greatest, witness = Fraction(0), None
    for a in range(messages):
        for b in range(a):
            distance = (
                sum(
                    (
                        abs(distributions[a].get(c, 0) - distributions[b].get(c, 0))
                        for c in distributions[a].keys() | distributions[b].keys()
                    ),
                    Fraction(0),
                )
                / 2
            )
            if distance > greatest:
                greatest, witness = distance, [b, a]
    return {
        "ciphertext_labels": alphabet,
        "conditional_ciphertext_probabilities": [
            [str(row.get(c, 0)) for c in alphabet] for row in distributions
        ],
        "perfect_secrecy": greatest == 0,
        "max_pair_total_variation": str(greatest),
        "distinguishable_messages": witness,
        "decryptable_per_key": all(
            len(set(row)) == messages for row, p in zip(table, probabilities) if p > 0
        ),
        "scope": "single-use key independent of message; all message pairs, positive-probability keys; no computational or reuse security claim",
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
