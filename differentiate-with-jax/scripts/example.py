#!/usr/bin/env python3
"""Small executable independent-oracle check; ordinary Python required."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--self-test", action="store_true")
args = parser.parse_args()
try:
    import time

    import jax
    import numpy as np

    jax.config.update("jax_enable_x64", True)
    import jax.numpy as jnp

    x = jnp.array([0.3, -0.7], dtype=jnp.float64)
    assert x.dtype == jnp.float64
    f = lambda z: jnp.sum(z * z) + jnp.sin(z[0])
    g = jax.jit(jax.grad(f))
    h = jax.hessian(f)
    got = np.asarray(g(x).block_until_ready())
    hes = np.asarray(h(x))
    expected = np.array([2 * 0.3 + np.cos(0.3), 2 * (-0.7)])
    expected_h = np.diag([2 - np.sin(0.3), 2])
    np.testing.assert_allclose(got, expected, rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(hes, expected_h, rtol=1e-12, atol=1e-12)
    v = np.array([0.6, 0.8])
    steps = [1e-4, 1e-5, 1e-6]
    fd_values = [float((f(x + eps * v) - f(x - eps * v)) / (2 * eps)) for eps in steps]
    assert all(abs(fd - float(got @ v)) < 1e-8 for fd in fd_values)
    g(x).block_until_ready()
    t = time.perf_counter()
    g(x).block_until_ready()
    elapsed = time.perf_counter() - t
    import jaxlib

    result = {
        "jax": jax.__version__,
        "jaxlib": jaxlib.__version__,
        "devices": [str(d) for d in jax.devices()],
        "dtype": str(x.dtype),
        "backend": jax.default_backend(),
        "gradient": got.tolist(),
        "hessian": hes.tolist(),
        "directional_fd": fd_values,
        "fd_steps": steps,
        "warmed_synchronized_seconds": elapsed,
        "evidence": "analytic derivative and finite-difference crosscheck; timing is illustrative single call",
    }
except ModuleNotFoundError as exc:
    print(json.dumps({"status": "dependency-unavailable", "dependency": exc.name}))
    sys.exit(2)
print(
    json.dumps(
        {"status": "passed", "self_test": args.self_test, **result}, allow_nan=False
    )
)
