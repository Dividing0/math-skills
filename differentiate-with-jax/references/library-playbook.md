# Library playbook

## Primary documentation

Retrieved/checked 2026-10-08. Recheck documentation against installed versions before adapting API calls.

- https://docs.jax.dev/en/latest/notebooks/Common_Gotchas_in_JAX.html
- https://docs.jax.dev/en/latest/benchmarking.html

The workflow names the relevant API locators; use the actual installed signatures and recorded version, especially for release/development discrepancies.

## Worked calculation

For f(x)=sum(x^2)+sin(x[0]), compare AD gradient and Hessian at (0.3,-0.7) against analytic formulas; synchronize a warmed JIT invocation and compare directional finite differences.

Execute `../scripts/example.py --self-test`. The script emits JSON and fails its assertions if the independent oracle disagrees. An unavailable dependency emits a dependency-unavailable status and exits 2; that is not a passed numerical check. Assertions run in ordinary Python, so do not launch with `-O`.

## False inference

JAX returns a derivative at abs(0), therefore the mathematical derivative exists. Library conventions at nonsmooth points do not establish differentiability.

## Integration contract

Receive a precise mathematical statement, assumptions, units, dimensions, data provenance, desired error/accuracy, available interpreter and runtime constraints from the mathematical skill. Return the exact implementation, dependency versions, executed inputs, raw outcomes, failure/status information, and independent checks. Keep numerical tolerance separate from mathematical guarantees. If an assumption or dependency is missing, return the missing item and any valid partial analysis rather than a fabricated computed result.

## Scope and escalation

Hand back to analyze-model-sensitivity, develop-mathematical-optimization, research-numerical-analysis when the issue concerns mathematical assumptions or justification rather than an API. Prefer the smaller supported calculation to an unvalidated large model. Preserve input data and task-local outputs; avoid modifying environments or external services without the task's authorization.

## API locators and selection

- Sharp Bits: pure functions, tracing, immutability, dynamic shapes and RNG conventions.
- Benchmarking: `.block_until_ready()` after warmup; report backend and transfers.
- Transformations: `jax.grad` for scalar output, `jax.jacfwd`/`jax.jacrev` for vector maps, `jax.hessian`, `jax.vmap`, `jax.jit`. Check `jax.config.update("jax_enable_x64", True)` before constructing inputs.
- Gradient oracle is (2*x0+cos(x0),2*x1); Hessian is diag(2-sin(x0),2). Finite differences are an additional cross-check rather than their own proof.
- Example execution checked JAX 0.11.2 on CPU, float64. A single warmed timing is illustrative and must not be called a benchmark.
