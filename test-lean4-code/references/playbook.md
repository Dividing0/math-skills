# Test Lean 4 Code: playbook

## Selecting test evidence

[Positive.lean](../assets/Positive.lean) checks pure boundary behavior and a universal reversal identity. [Negative.lean](../assets/Negative.lean) is an intentional type mismatch and belongs outside a normal build target. Copy them into a scratch project's `Tests/` directory to run the helper example.

Use `#guard_msgs` when the pinned project's conventions require exact diagnostics, and inspect actual messages before writing expectations. Expected-error substrings in the helper are less sensitive to formatting changes but must identify the intended failure. An empty expectation is rejected.

The runner checks `lake env lean --version` before individual cases. Each file is checked directly, using argument arrays and a project-contained path. It never invokes a shell command from JSON. Imported modules must already be built; Elan may provision a selected toolchain when Lake runs, so confirm available pins first when working offline.

## Acceptance cases

- A negative fixture has the right error text and a nonzero checker exit: pass that regression case, not the mathematical claim.
- A negative fixture unexpectedly compiles: fail the case.
- Timeout or unavailable Lean: fail coverage; do not count it as the expected type error.
- A positive fixture compiles with a sorry warning: fail the case.
- Examples pass but a public consumer no longer elaborates: record an API regression.
- A property of an IO program is requested: pure checker acceptance alone is insufficient runtime coverage.

## Primary sources

[Lean interacting commands](https://lean-lang.org/doc/reference/latest/Interacting-with-Lean/) and [Lean evaluation](https://lean-lang.org/doc/reference/latest/Run-Time-Code/). Check project-specific runtime testing conventions locally.
