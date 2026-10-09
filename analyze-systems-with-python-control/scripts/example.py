#!/usr/bin/env python3
"""Small executable independent-oracle check; ordinary Python required."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse, json, sys

parser = argparse.ArgumentParser()
parser.add_argument("--self-test", action="store_true")
args = parser.parse_args()
try:
    import numpy as np
    import control as ct

    G = ct.tf([1.0], [1.0, 1.0], dt=0)
    T = ct.feedback(G, 1, sign=-1)
    poles = ct.poles(T)
    np.testing.assert_allclose(poles, [-2.0])
    time = np.linspace(0, 3, 61)
    response = ct.step_response(T, timepts=time)
    y = np.asarray(response.outputs)
    oracle = 0.5 * (1 - np.exp(-2 * time))
    np.testing.assert_allclose(y, oracle, rtol=1e-10, atol=1e-12)
    discrete = ct.ss([[0.5]], [[1.0]], [[1.0]], [[0.0]], dt=0.1)
    td = np.arange(11) * 0.1
    rd = ct.step_response(discrete, timepts=td)
    # x[0]=0; x[k+1]=.5*x[k]+1, hence x[k]=2*(1-.5**k).
    expected = 2 * (1 - 0.5 ** np.arange(11))
    np.testing.assert_allclose(np.asarray(rd.outputs), expected, atol=1e-12)
    result = {
        "control": ct.__version__,
        "continuous_poles_real": poles.real.tolist(),
        "continuous_step_max_error": float(np.max(np.abs(y - oracle))),
        "discrete_dt": 0.1,
        "discrete_step_max_error": float(
            np.max(np.abs(np.asarray(rd.outputs) - expected))
        ),
        "evidence": "independent analytic continuous response and discrete recurrence",
    }
except ModuleNotFoundError as exc:
    print(json.dumps({"status": "dependency-unavailable", "dependency": exc.name}))
    sys.exit(2)
print(
    json.dumps(
        {"status": "passed", "self_test": args.self_test, **result}, allow_nan=False
    )
)
