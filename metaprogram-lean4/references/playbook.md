# Metaprogram Lean 4: playbook

## Choosing the mechanism

A macro rewrites syntax before type-directed elaboration. An elaborator can inspect expected types and construct expressions. A tactic elaborator manipulates proof goals. Match the mechanism to the information needed; a macro is not a reliable place to decide a typeclass-dependent mathematical fact.

[Extensions.lean](../assets/Extensions.lean) contains a hygienic term macro and a small tactic elaborator. Its shadowing example checks that a generated local binder does not capture a caller's variable. The tactic delegates to an existing checked tactic rather than constructing a trusted assertion.

## Verification

Copy the asset to a scratch module in a pinned project and run `lake env lean Extensions.lean`. Build imports before tests. Use `#check`, goal inspection, and a temporary `#print axioms` for generated declarations; distinguish a meta-program crash, elaboration failure and an unproved mathematical claim. For repeatable expected-success/error cases, use the neighboring [test runner](../../test-lean4-code/scripts/run_cases.py) when installed, following its [command reference](../../test-lean4-code/references/command-line.md).

## Acceptance cases

- A generated binder shadows `x` at the call site: preserve the caller's meaning with hygienic quotations.
- A tactic leaves a metavariable: fail the completion claim even if the metaprogram itself returned.
- A search branch modifies the goal before failing: restore state before trying the alternative.
- New syntax depends on inferred types: use an elaborator instead of guessing from token text.
- Toolchain unavailable: return an unchecked extension and the exact verification gap.

## Primary sources

[Lean macros and elaborators](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/). Confirm API names in the pinned Lean sources; latest documentation can describe newer APIs.
