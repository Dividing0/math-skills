---
name: check-lean4-idiomaticity
description: "Review Lean 4 code for idiomatic definitions, proof structure, naming, imports, simplification and local style conventions. Use for style and maintainability reviews or requested cleanup, distinguishing project requirements from optional Mathlib conventions."
---

# Check Lean 4 Idiomaticity

## Workflow

1. Determine the code's audience and conventions from project instructions, nearby maintained modules, pinned Lean/Mathlib revisions and configured linters. Mathlib contribution rules guide Mathlib-style mathematics; they are not universal requirements for a Lean executable or metaprogram.
2. Review public names, namespaces, binder clarity, documentation and imports. Where Mathlib conventions apply, distinguish theorem proofs, predicates/types and data/computational definitions. Check library reuse and caller compatibility before proposing a rename. Do not apply a blind snake_case transformation to all Lean declarations.
3. Read the proof argument before judging its length. Prefer a direct lemma application when it states the intended fact, and structured `have`, `calc` or case splits when they expose reasoning. A shorter term is not automatically clearer; tactic proofs and term proofs can both be idiomatic.
4. Inspect simplification and scope. Choose rewrite direction deliberately, avoid unstable dependence on implementation details, and inspect the normal form before adding `[simp]`. Use `simp only` when controlled dependencies help; ordinary `simp` is often appropriate. Scope `classical`, options, instances and notation to their actual use. Do not treat legitimate classical reasoning or automation as a style failure.
5. For computational code, consider standard containers, pattern matching, `Option`/`Except`, `do` notation, explicit error handling and library combinators where they fit the API. Preserve effects, termination and computation requirements. Style cleanup must not silently change return types, theorem assumptions, public attributes or reduction behavior.
6. Run the project's supported linters and actual file/build checks. Discover commands from pinned configuration or contributing instructions; do not invent a universal `lake lint` command or assume Mathlib's linters are installed. Keep linter diagnostics separate from human recommendations and explain justified exceptions.
7. Report actionable examples with locations, the applicable convention, and an optional replacement. Distinguish required fixes from preferences; avoid an unsupported percentage score. If cleanup was requested, apply focused changes and recheck affected callers. Otherwise return the review without unrelated rewriting.

## Resources

Read the [idiomaticity guide](references/idiomaticity-guide.md) for naming distinctions, acceptance cases and primary sources. [Idioms.lean](assets/Idioms.lean) compares an unnecessarily indirect proof with a direct proof of the identical statement.

When available, use [improve-lean4-code](../improve-lean4-code/SKILL.md) for implementation changes and [analyze-lean4-code](../analyze-lean4-code/SKILL.md) for correctness or design weaknesses. The existing [host checker](../audit-lean4-proofs/scripts/check_project.py), described in its [command reference](../audit-lean4-proofs/references/command-line.md), captures real Lean diagnostics. It is not a style linter; successful compilation is only one part of this review. Without neighboring skills, run `lake env lean Path/To/File.lean` and the project's actual build and lint commands directly.
