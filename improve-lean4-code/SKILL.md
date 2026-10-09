---
name: improve-lean4-code
description: "Improve existing Lean 4 definitions, executable code and proofs through focused refactoring, library reuse and measured performance work. Use when asked to enhance or simplify code while preserving its public API, mathematical statements and runtime behavior."
---

# Improve Lean 4 Code

## Workflow

1. Read the affected code, callers, project instructions, `lean-toolchain`, Lake configuration and dependency pins. Identify the requested improvement: readability, reuse, proof robustness, elaboration time or runtime performance. Establish the existing build/test result before attributing failures to an edit.
2. Record what must survive the change: declaration names, binder order and implicitness, typeclass assumptions, theorem statements, computability, error behavior and public imports. For definitions, consider downstream reduction and `rfl` proofs as well as extensional equality. A propositionally equivalent implementation can still break clients.
3. Search project and library APIs before extracting a helper or rewriting an algorithm. Prefer a standard definition or lemma when its semantics and dependencies fit. Keep a compatibility wrapper when replacing a public name; do not generalize signatures or upgrade dependencies merely to shorten a proof.
4. Make a focused change. Remove redundant steps, expose useful intermediate facts, and use scoped notation, instances and options. Replace exploratory automation with a checked suggestion when it improves clarity or stability; ordinary `simp` and domain automation can remain appropriate. Preserve termination arguments and avoid introducing `sorry`, axioms or unchecked implementations to make a refactor pass.
5. For executable code, check empty/boundary inputs, failure paths and observable effects. Prove an equivalence lemma where practical and retain representative caller tests. If performance is the goal, measure the same workload before and after; separate elaboration/build time from compiled runtime and cached builds from fresh work.
6. Run `lake env lean Path/To/File.lean` from the pinned project, build the affected targets and check relevant callers. Run the project's tests and linters where available. Inspect warnings and changed theorem dependencies when proof structure changes; checker success alone does not prove a runtime optimization correct.
7. Report the concrete improvement, preserved contracts, actual verification and measurements, and any remaining compatibility risk. If execution is unavailable, label the patch unchecked rather than claiming a verified improvement.

## Resources

Read the [refactoring playbook](references/refactoring-playbook.md) for reduction-sensitive changes, performance evidence and acceptance cases. [Refactor.lean](assets/Refactor.lean) demonstrates replacing a recursive implementation with a library definition and proving pointwise equivalence.

When available alongside this skill, use [search-mathlib](../search-mathlib/SKILL.md) for library discovery, [debug-lean4-proofs](../debug-lean4-proofs/SKILL.md) for a failing proof, and [check-lean4-idiomaticity](../check-lean4-idiomaticity/SKILL.md) for a dedicated style review. Use the existing [host checker](../audit-lean4-proofs/scripts/check_project.py) with its [command reference](../audit-lean4-proofs/references/command-line.md) to capture file checks and named axiom diagnostics; it does not run builds, tests or benchmarks for you. The direct Lake workflow above also works without neighboring skills.

## Related workflow

For repeated regression and consumer checks after a refactor, use the testing workflow with positive cases and explicit expected diagnostics. Read [test-lean4-code](../test-lean4-code/SKILL.md) when that specialization is needed and available.
