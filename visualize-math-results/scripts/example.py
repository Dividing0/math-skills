"""Headless analytic curve, explicit sampling and log-domain guards."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse
import json
import math
import sys
import tempfile
from pathlib import Path

try:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    sys.exit("dependency_unavailable: numpy/matplotlib")


def render(output):
    output = Path(output)
    if output.suffix.lower() not in {".png", ".svg", ".pdf"}:
        raise ValueError("supported output extensions: .png, .svg, .pdf")
    t = np.linspace(0, 2, 101)
    y = np.exp(-2 * t)
    if t.shape != y.shape or not np.all(np.isfinite(y)):
        raise ValueError("invalid data")
    if np.any(y <= 0):
        raise ValueError("logarithmic y axis requires positive values")
    fig, axes = plt.subplots(1, 2, figsize=(8, 3), layout="constrained")
    axes[0].plot(t, y, label="Analytic exp(-2t)")
    axes[0].set(xlabel="Time (s)", ylabel="Amplitude", title="Linear scale")
    axes[1].semilogy(t, y, label="Analytic exp(-2t)")
    axes[1].set(xlabel="Time (s)", ylabel="Amplitude", title="Logarithmic scale")
    for ax in axes:
        ax.legend()
        ax.grid(True, alpha=0.3)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=120)
    plt.close(fig)
    content = output.read_bytes()
    kind = output.suffix.lower()
    valid = (
        content.startswith(b"\x89PNG\r\n\x1a\n")
        if kind == ".png"
        else (
            b"<svg" in content[:1000]
            if kind == ".svg"
            else content.startswith(b"%PDF-")
        )
    )
    assert valid and output.stat().st_size > 1000
    assert abs(float(y[0]) - 1) < 1e-15 and abs(float(y[-1]) - math.exp(-4)) < 1e-15
    return {
        "library": "matplotlib",
        "version": matplotlib.__version__,
        "classification": "visualization_of_analytic_samples",
        "output": str(output),
        "samples": len(t),
        "domain": [0, 2],
        "sampling_step": float(t[1] - t[0]),
        "source_formula": "exp(-2t)",
        "plot_is_proof": False,
        "checks": [
            "headless_render",
            kind[1:] + "_signature",
            "endpoint_values",
            "closed_figure",
            "positive_log_data",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    if args.self_test:
        with tempfile.TemporaryDirectory() as tmp:
            result = render(Path(tmp) / "check.png")
            result["output"] = "temporary_check_png_removed"
    elif args.output:
        result = render(args.output)
    else:
        parser.error("--output is required unless --self-test is used")
    print(json.dumps(result, indent=2))
