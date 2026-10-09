---
name: analyze-systems-with-python-control
description: Build and analyze transfer-function and state-space models using python-control, including feedback, poles, time responses, sampling and LQR. Use for continuous/discrete control models and validate feedback signs, stability, dimensions and response conventions.
---

# Analyze Systems with Python Control

Read [library-playbook.md](references/library-playbook.md) for API locators, worked example, failure analysis and the integration contract. Run `scripts/example.py --self-test` using the task's selected Python interpreter before adapting it. Missing dependencies must be reported explicitly; do not invent executions.

## Workflow

1. Record units, channel order, operating point and explicit timebase. Use `dt=0` for continuous models, positive dt for known discrete sampling; `dt=True` means unspecified discrete time. Do not mix timebases implicitly.
2. Build `tf` or `ss`; check dimensions and physical meaning of A,B,C,D. State input/reference/disturbance channels and sign convention. `feedback(G,H,sign=-1)` is negative feedback; derive the closed-loop equation before connecting systems.
3. Distinguish internal state stability from input-output poles: cancellation can hide unstable states. Continuous asymptotic stability requires Re(lambda)<0; discrete requires |lambda|<1. Boundary cases need separate analysis.
4. Set an explicit time grid and initial state; inspect `TimeResponseData.time`, `.outputs`, `.states` and channel dimensions. Compare SISO responses against an analytic solution or independent matrix exponential. Use the discrete recurrence and sample grid for discrete systems.
5. For LQR use u=-Kx and verify A-BK. Check stabilizability/detectability assumptions, Q symmetric PSD, R symmetric positive definite. Distinguish `lqr` and `dlqr`, report Riccati residual and closed-loop eigenvalues; linearized simulation does not certify nonlinear or robust stability.

## Handoff

Use the existing mathematical skills (research-control-theory, develop-control-state-estimation, analyze-math-stability, research-optimal-control) to establish assumptions and interpret conclusions. Use `run-math-python` for reproducible execution records. Return the actual executed code, versions, inputs, status, diagnostics, oracle checks and artifacts. Label evidence as numerical, exact symbolic, validated enclosure or formal proof; do not upgrade evidence without a checker.
