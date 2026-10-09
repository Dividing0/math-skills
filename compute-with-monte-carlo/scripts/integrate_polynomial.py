#!/usr/bin/env python3
"""Estimate a polynomial integral with IID, antithetic or fixed-control samples."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("numpy",)
EVIDENCE = "Monte-Carlo-estimate-with-approximate-normal-interval"
EXAMPLE = {
    "coefficients": [0, 0, 1],
    "lower": 0,
    "upper": 1,
    "samples": 10000,
    "seed": 7,
    "method": "antithetic",
}


def compute(data):
    import numpy as np

    coefficients = np.asarray(data["coefficients"], dtype=float)
    if (
        coefficients.ndim != 1
        or not 1 <= len(coefficients) <= 30
        or not np.isfinite(coefficients).all()
    ):
        raise ValueError(
            "coefficients must contain 1..30 finite polynomial coefficients, ascending order"
        )
    n, seed = data.get("samples", 10000), data.get("seed", 0)
    if (
        type(n) is not int
        or not 2 <= n <= 1000000
        or type(seed) is not int
        or not 0 <= seed < 2**64
    ):
        raise ValueError("samples must be 2..1000000 and seed an integer in [0,2**64)")
    lower, upper = data.get("lower", 0), data.get("upper", 1)
    if (
        any(type(v) not in (int, float) or not math.isfinite(v) for v in (lower, upper))
        or lower >= upper
    ):
        raise ValueError("finite bounds must satisfy lower < upper")
    method = data.get("method", "plain")
    if method not in {"plain", "antithetic", "control-variate"}:
        raise ValueError("unknown method")
    rng = np.random.default_rng(seed)
    x = rng.uniform(lower, upper, n)
    y = np.polynomial.polynomial.polyval(x, coefficients)
    if method == "antithetic":
        y = (y + np.polynomial.polynomial.polyval(lower + upper - x, coefficients)) / 2
    elif method == "control-variate":
        beta = data["control_coefficient"]
        if type(beta) not in (int, float) or not math.isfinite(beta):
            raise ValueError(
                "control_coefficient must be fixed independently of these samples and finite"
            )
        y = y - beta * (x - (lower + upper) / 2)
    y *= upper - lower
    if not np.isfinite(y).all():
        raise ValueError("nonfinite integrand values")
    estimate = float(y.mean())
    error = float(y.std(ddof=1) / math.sqrt(n))
    analytic = sum(
        float(c) * (upper ** (k + 1) - lower ** (k + 1)) / (k + 1)
        for k, c in enumerate(coefficients)
    )
    return {
        "estimate": estimate,
        "standard_error": error,
        "approximate_95_percent_interval": [
            estimate - 1.95996398454 * error,
            estimate + 1.95996398454 * error,
        ],
        "analytic_integral": analytic,
        "absolute_error": abs(estimate - analytic),
        "independent_units": n,
        "function_evaluations": n * (2 if method == "antithetic" else 1),
        "method": method,
        "seed": seed,
        "bit_generator": type(rng.bit_generator).__name__,
        "scope": "fixed sample count; antithetic pairs are single independent units; interval is asymptotic, not certified",
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
