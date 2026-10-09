"""Dense numerical reference, shape guard and singular-case rejection."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse
import json
import sys

try:
    import numpy as np
except ImportError:
    sys.exit("dependency_unavailable: numpy; use the declared Python environment")


def example():
    A = np.array([[3.0, 1.0], [1.0, 2.0]])
    b = np.array([7.0, 5.0])
    x = np.linalg.solve(A, b)
    reference = np.array([9 / 5, 8 / 5])
    error = float(np.linalg.norm(x - reference, np.inf))
    residual = float(np.linalg.norm(A @ x - b, np.inf))
    assert error < 1e-12 and residual < 1e-12
    singular_rejected = False
    try:
        np.linalg.solve(np.array([[1.0, 0.0], [0.0, 0.0]]), np.array([1.0, 0.0]))
    except np.linalg.LinAlgError:
        singular_rejected = True
    assert singular_rejected
    col = np.array([[1.0], [2.0]])
    vector = np.array([3.0, 4.0])
    broadcast_shape = (col + vector).shape
    assert broadcast_shape == (2, 2) and broadcast_shape != col.shape
    rng = np.random.default_rng(17)
    samples = rng.normal(size=8)
    assert np.array_equal(samples, np.random.default_rng(17).normal(size=8))
    return {
        "library": "numpy",
        "version": np.__version__,
        "classification": "approximate_numeric",
        "x": x.tolist(),
        "independent_reference": ["9/5", "8/5"],
        "max_forward_error": error,
        "residual_inf": residual,
        "singular_rejected": singular_rejected,
        "broadcast_shape": list(broadcast_shape),
        "rng_seed": 17,
        "checks": [
            "analytic_linear_solution",
            "residual",
            "singular_rejection",
            "shape_trap",
            "local_rng_repeatability",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.parse_args()
    print(json.dumps(example(), indent=2))
