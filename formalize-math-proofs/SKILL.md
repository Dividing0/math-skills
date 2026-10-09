---
name: formalize-math-proofs
description: "Translate exact mathematical statements and proofs into a project proof assistant. Use for Lean, Rocq or Isabelle formalization, library reuse, theorem correspondence, placeholder audits and actual checker verification."
---

# Formalize Math Proofs

## Lean 4 specializations

For Lean 4, load only the specialization relevant to the current obstacle:

- [Set up Lean 4 projects](../setup-lean4-projects/SKILL.md) for pinned toolchains, Lake, Mathlib dependencies and caches.
- [Prove with Lean 4](../prove-with-lean4/SKILL.md) for statement translation and incremental proof construction.
- [Search Mathlib](../search-mathlib/SKILL.md) for candidate declarations, signatures and imports.
- [Debug Lean 4 proofs](../debug-lean4-proofs/SKILL.md) for elaboration, coercion, instance and tactic failures.
- [Audit Lean 4 proofs](../audit-lean4-proofs/SKILL.md) for statement correspondence, checker coverage and transitive axiom checks.

These specialize the workflow below; Rocq and Isabelle tasks retain the general guidance.

## Workflow

1. Choose the assistant from the user request or existing project; inspect pinned versions, dependencies and established notation.
2. Translate the exact mathematical statement first, including quantifiers, coercions, universes and assumptions. Compare it with the informal claim.
3. Search the existing library before rebuilding results; use official documentation for version-dependent commands.
4. Build definitions and lemmas incrementally; run the real checker after changes and retain commands and results.
5. Audit placeholders, sorry, admitted, axioms, unsafe bypasses and opaque imported assumptions. Inspect theorem dependencies with the assistant’s supported facilities.
6. Report statement correspondence, checker status and admitted assumptions separately. If tooling is unavailable, label the output an unchecked formalization draft.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.
