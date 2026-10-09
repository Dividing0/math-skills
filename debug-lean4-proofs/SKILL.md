---
name: debug-lean4-proofs
description: "Diagnose and repair Lean 4 mathematical proof failures involving elaboration, coercions, typeclass inference, rewrites, tactics and imports. Use for failing proof code while preserving the intended theorem."
---

# Debug Lean 4 Proofs

## Workflow

1. Reproduce the first relevant diagnostic with `lake env lean Path/To/File.lean` from the pinned project root. Record the command, source location, goal and local context. Resolve earlier parser or import errors before downstream tactic messages.
2. Classify the failure: missing artifact or import, unknown declaration, type mismatch, unresolved implicit argument, missing instance, rewrite mismatch, unsolved mathematical goal or resource exhaustion. Use `setup-lean4-projects` for toolchain and cache failures.
3. Reduce to a scratch declaration retaining the failing binders, imports and relevant instances. Use `#check`, `#print`, local type annotations and `show`/`change` to reveal what Lean expects; use local pretty-print options when hidden casts or universes matter.
4. For mismatched terms, make casts and domains explicit. For instances, inspect the expected class and available assumptions before adding `classical` or an instance. `classical` supplies classical decidability, not arbitrary algebraic structures. For rewrites, inspect occurrence, direction and normal form; `change` requires definitional equality, while `rw` uses a proved equality.
5. For tactic failures, expose intermediate goals and choose a method matching the mathematical obligation. Missing side conditions need proof or a corrected user-approved statement, not a raised heartbeat limit. Increase resource bounds locally only after identifying a legitimate expensive step.
6. Make the smallest relevant fix, rerun the direct checker and the affected build, and remove temporary diagnostics. Preserve theorem domains, hypotheses and conclusion; surface a false statement or missing assumption instead of silently weakening it.
7. Report the cause, change and actual verification result. If unavailable tooling or an unresolved mathematical obligation remains, state it explicitly and provide a bounded next step.

## Resources

Read [debugging playbook](references/debugging-playbook.md) for reproductions and acceptance checks. [MissingHypothesis.lean](assets/MissingHypothesis.lean) and [CoercionFailure.lean](assets/CoercionFailure.lean) are intentional failures; [Fixed.lean](assets/Fixed.lean) illustrates the corrections. Do not include failure assets in a normal build target.

## Host computation

When the `audit-lean4-proofs` skill is installed alongside this skill, run actual Lean file checks or named theorem axiom diagnostics in a pinned project; inspect checker output and verify correspondence to the mathematical claim separately. Use its [check_project.py](../audit-lean4-proofs/scripts/check_project.py) helper and [input/command reference](../audit-lean4-proofs/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
