#!/usr/bin/env python3
"""Compute finite orthonormal Haar or discrete Fourier transforms with reconstruction diagnostics."""

import argparse
import hashlib
import importlib.metadata
import json
import platform
import sys
from pathlib import Path

DEPENDENCIES = ("numpy",)
EVIDENCE = "finite-numerical-transform"
EXAMPLE = {"operation": "haar", "signal": [3, 1], "threshold": 2}


def compute(data):
    import numpy as np

    signal = np.asarray(data["signal"], dtype=float)
    if (
        signal.ndim != 1
        or not len(signal)
        or len(signal) > 1048576
        or not np.isfinite(signal).all()
    ):
        raise ValueError("signal must contain 1..1048576 finite real samples")
    op = data["operation"]
    energy = float(signal @ signal)
    if op == "dft":
        coefficients = np.fft.fft(signal, norm="ortho")
        reconstructed = np.fft.ifft(coefficients, norm="ortho")
        dt = float(data.get("sample_interval", 1))
        if not np.isfinite(dt) or dt <= 0:
            raise ValueError("sample_interval must be finite and positive")
        return {
            "coefficients": [[float(v.real), float(v.imag)] for v in coefficients],
            "frequencies": np.fft.fftfreq(len(signal), d=dt).tolist(),
            "normalization": "orthonormal DFT",
            "reconstruction_error": float(max(abs(reconstructed - signal))),
            "parseval_residual": float(sum(abs(coefficients) ** 2) - energy),
            "scope": "sampled periodic DFT, not a continuous Fourier transform",
        }
    if op != "haar" or len(signal) & (len(signal) - 1):
        raise ValueError(
            "Haar requires a power-of-two length; operation must be haar or dft"
        )
    coefficients = signal.copy()
    n = len(signal)
    while n > 1:
        a, b = coefficients[:n:2].copy(), coefficients[1:n:2].copy()
        coefficients[: n // 2], coefficients[n // 2 : n] = (
            (a + b) / np.sqrt(2),
            (a - b) / np.sqrt(2),
        )
        n //= 2
    threshold = float(data.get("threshold", 0))
    if not np.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be finite and nonnegative")
    kept = np.where(abs(coefficients) >= threshold, coefficients, 0)
    reconstructed = kept.copy()
    n = 1
    while n < len(signal):
        a, b = reconstructed[:n].copy(), reconstructed[n : 2 * n].copy()
        reconstructed[: 2 * n : 2], reconstructed[1 : 2 * n : 2] = (
            (a + b) / np.sqrt(2),
            (a - b) / np.sqrt(2),
        )
        n *= 2
    discarded = float(sum((coefficients - kept) ** 2))
    error = float(sum((signal - reconstructed) ** 2))
    return {
        "coefficients": coefficients.tolist(),
        "thresholded_coefficients": kept.tolist(),
        "reconstruction": reconstructed.tolist(),
        "input_energy": energy,
        "parseval_residual": float(coefficients @ coefficients - energy),
        "squared_error": error,
        "discarded_energy": discarded,
        "error_identity_residual": error - discarded,
        "convention": "orthonormal Haar; coarse coefficient then details from coarse to fine; no padding",
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
