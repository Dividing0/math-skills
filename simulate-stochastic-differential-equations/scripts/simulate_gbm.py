#!/usr/bin/env python3
"""Compare coupled Euler-Maruyama and Milstein paths against exact scalar GBM."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("numpy",)
EVIDENCE = "seeded-Monte-Carlo-and-discretization-evidence"
EXAMPLE = {
    "initial": 1,
    "drift": 0.2,
    "diffusion": 0.4,
    "duration": 1,
    "steps": 64,
    "paths": 2000,
    "seed": 7,
    "interpretation": "ito",
}


def compute(data):
    import numpy as np

    steps, paths, seed = (
        data.get("steps", 64),
        data.get("paths", 2000),
        data.get("seed", 0),
    )
    if (
        type(steps) is not int
        or steps < 2
        or steps % 2
        or type(paths) is not int
        or paths < 2
        or steps * paths > 2000000
    ):
        raise ValueError(
            "steps must be positive even, paths >=2, and steps*paths <=2000000"
        )
    if type(seed) is not int or not 0 <= seed < 2**64:
        raise ValueError("seed must be an integer in [0,2**64)")
    values = [
        data.get("initial", 1),
        data["drift"],
        data["diffusion"],
        data.get("duration", 1),
    ]
    if any(type(v) not in (int, float) or not math.isfinite(v) for v in values):
        raise ValueError("model values must be finite numbers")
    x0, mu, sigma, duration = map(float, values)
    if duration <= 0 or sigma < 0:
        raise ValueError("duration must be positive and diffusion nonnegative")
    convention = data.get("interpretation", "ito")
    if convention not in {"ito", "stratonovich"}:
        raise ValueError("interpretation must be ito or stratonovich")
    drift = mu + sigma**2 / 2 if convention == "stratonovich" else mu
    rng = np.random.default_rng(seed)
    increments = rng.normal(0, math.sqrt(duration / steps), (steps, paths))
    exact = x0 * np.exp(
        (drift - sigma**2 / 2) * duration + sigma * increments.sum(axis=0)
    )
    diagnostics = []
    for stride in (2, 1):
        count = steps // stride
        dw = increments.reshape(count, stride, paths).sum(axis=1)
        h = duration / count
        euler = np.full(paths, x0)
        milstein = np.full(paths, x0)
        for increment in dw:
            factor = 1 + drift * h + sigma * increment
            euler *= factor
            milstein *= factor + sigma**2 * (increment**2 - h) / 2
        if not all(np.isfinite(v).all() for v in (exact, euler, milstein)):
            raise ValueError("nonfinite trajectory; reduce model scale or horizon")
        diagnostics.append(
            {
                "steps": count,
                "step_size": h,
                "euler_rmse": float(np.sqrt(np.mean((euler - exact) ** 2))),
                "milstein_rmse": float(np.sqrt(np.mean((milstein - exact) ** 2))),
                "euler_terminal_mean": float(euler.mean()),
                "milstein_terminal_mean": float(milstein.mean()),
            }
        )
    orders = {
        method: math.log2(diagnostics[0][method] / diagnostics[1][method])
        if diagnostics[0][method] > 0 and diagnostics[1][method] > 0
        else None
        for method in ("euler_rmse", "milstein_rmse")
    }
    return {
        "interpretation": convention,
        "ito_drift": drift,
        "seed": seed,
        "bit_generator": type(rng.bit_generator).__name__,
        "paths": paths,
        "levels": diagnostics,
        "observed_strong_orders": orders,
        "exact_terminal_mean": x0 * math.exp(drift * duration),
        "sample_exact_mean": float(exact.mean()),
        "sample_exact_standard_error": float(exact.std(ddof=1) / math.sqrt(paths)),
        "scope": "scalar geometric Brownian motion, coupled paths; empirical orders are not convergence proofs",
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
