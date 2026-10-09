---
name: contribute-to-mathlib
description: "Prepare mathematically appropriate Mathlib contributions with library discovery, declaration placement, compatible APIs, local lint/build checks and review-ready evidence. Use for upstream preparation, not generic Lean style cleanup."
---

# Prepare Mathlib Contributions

## Workflow

1. Read the current Mathlib contribution policy, target revision and nearby modules. Establish the mathematical result, whether it fits the library, and whether the task is preparation or an explicitly authorized external submission.
2. Search for an existing result by signature and statement shape. Compare generality, namespaces and imports; a new name for an existing theorem is not necessarily a useful addition.
3. Choose the lowest appropriate module in the import hierarchy and an API consistent with related declarations. Prefer justified generality without inventing unused abstractions; avoid a new import cycle or a heavy dependency for a basic lemma.
4. Write a focused patch with precise statements and supporting lemmas. Apply the target repository naming, documentation, simp and contributor requirements. Review AI-assisted contribution requirements and respect required human involvement; a prepared patch does not itself authorize posting messages.
5. Run the target repository documented lint and build checks, including edited modules and representative consumers. Inspect admitted obligations and named axiom dependencies. Do not invent a universal Mathlib lint command or call all automation unacceptable.
6. Prepare a concise contribution description stating the mathematical addition, placement choice, relevant reuse and actual verification. Separate unresolved review questions from completed checks; avoid unrelated cosmetic changes or assertions that acceptance is guaranteed.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.
