#!/usr/bin/env python3
"""Render supplied finite data to a labeled PNG, SVG or PDF using a headless backend."""

import argparse
import hashlib
import importlib.metadata
import json
import math
import platform
import sys
from itertools import pairwise
from pathlib import Path

DEPENDENCIES = ("matplotlib",)
EVIDENCE = "data-visualization"
EXAMPLE = {
    "x": [0, 1, 2],
    "y": [1, 0.5, 0.25],
    "xlabel": "Time (s)",
    "ylabel": "Amplitude",
    "kind": "line",
    "output": "/tmp/math-skill-plot.png",
}


def compute(data):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    x, y = list(map(float, data["x"])), list(map(float, data["y"]))
    if not x or len(x) != len(y) or any(not math.isfinite(v) for v in x + y):
        raise ValueError("x and y must be nonempty aligned finite data")
    output = Path(data["output"]).resolve()
    if output.suffix.lower() not in {".png", ".svg", ".pdf"}:
        raise ValueError("output must be PNG, SVG or PDF")
    xscale, yscale = data.get("xscale", "linear"), data.get("yscale", "linear")
    if xscale not in {"linear", "log"} or yscale not in {"linear", "log"}:
        raise ValueError("scales must be linear or log")
    if (xscale == "log" and min(x) <= 0) or (yscale == "log" and min(y) <= 0):
        raise ValueError("log scales require strictly positive data")
    kind = data.get("kind", "scatter")
    if kind not in {"scatter", "line"}:
        raise ValueError("kind must be scatter or line")
    if kind == "line" and any(a >= b for a, b in pairwise(x)):
        raise ValueError(
            "line plots require strictly increasing x; split discontinuities into separate runs"
        )
    xlabel, ylabel = data["xlabel"], data["ylabel"]
    if (
        not isinstance(xlabel, str)
        or not isinstance(ylabel, str)
        or not xlabel
        or not ylabel
    ):
        raise ValueError(
            "nonempty axis labels are required; include units when applicable"
        )
    errors = data.get("yerr")
    if errors is not None:
        errors = list(map(float, errors))
        if (
            len(errors) != len(y)
            or any(not math.isfinite(v) or v < 0 for v in errors)
            or not data.get("uncertainty_label")
        ):
            raise ValueError(
                "yerr needs matching nonnegative finite values and uncertainty_label"
            )
        if yscale == "log" and any(v - e <= 0 for v, e in zip(y, errors)):
            raise ValueError("log error bars must remain positive")
    fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
    try:
        if errors is not None:
            ax.errorbar(
                x,
                y,
                yerr=errors,
                fmt="o-" if kind == "line" else "o",
                label=data["uncertainty_label"],
            )
            ax.legend()
        elif kind == "line":
            ax.plot(x, y)
        else:
            ax.scatter(x, y)
        ax.set(
            xlabel=xlabel,
            ylabel=ylabel,
            title=data.get("title", ""),
            xscale=xscale,
            yscale=yscale,
        )
        ax.grid(True, alpha=0.25)
        output.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output, dpi=150)
    finally:
        plt.close(fig)
    return {
        "output": str(output),
        "bytes": output.stat().st_size,
        "points": len(x),
        "xscale": xscale,
        "yscale": yscale,
        "scope": "visualization of supplied data; uncertainty meaning is supplied by the caller",
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
