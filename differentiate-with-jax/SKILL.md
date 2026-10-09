---
name: differentiate-with-jax
description: Execute pure numerical JAX functions using grad, Jacobian/Hessian transformations, vmap and jit; inspect precision, tracing restrictions and derivative validity. Use for differentiable models, sensitivity, batched calculations and synchronized performance measurements.
---

# Differentiate with JAX

Read [library-playbook.md](references/library-playbook.md) for API locators, worked example, failure analysis and the integration contract. Run `scripts/example.py --self-test` using the task's selected Python interpreter before adapting it. Missing dependencies must be reported explicitly; do not invent executions.

## Workflow

1. Record JAX/jaxlib versions, backend/devices, dtype and shapes. Enable `jax_enable_x64` before array creation when float64 is required, then inspect actual dtypes. Do not assume accelerators exist.
2. Express a pure function using `jax.numpy`; avoid mutable global state, ordinary NumPy on tracers and data-dependent Python branching under `jit`. Use `lax.cond`/`lax.scan` where appropriate; distinguish static metadata from traced values.
3. Require scalar real output for ordinary `grad`; use `jacfwd`/`jacrev` for vectors and explicit complex derivative conventions. Check domain, nondifferentiable points and branch behavior. Differentiating the implemented algorithm is not automatically differentiating an exact mathematical solution.
4. Validate with analytic derivatives or directional finite differences at multiple step sizes away from singularities. Check shapes and finite outputs; use `vmap` for independent batching and keep PRNG keys explicit and split correctly.
5. Warm up `jit`, synchronize outputs with `block_until_ready()`, and separate compilation, device transfer and steady-state time. Do not compare asynchronous launch time to synchronized CPU computation. Return numerical derivatives and diagnostics; do not infer global optimality or mathematical smoothness from AD.

## Handoff

Use the existing mathematical skills (analyze-model-sensitivity, develop-mathematical-optimization, research-numerical-analysis) to establish assumptions and interpret conclusions. Use `run-math-python` for reproducible execution records. Return the actual executed code, versions, inputs, status, diagnostics, oracle checks and artifacts. Label evidence as numerical, exact symbolic, validated enclosure or formal proof; do not upgrade evidence without a checker.
