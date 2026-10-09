---
name: prove-with-lean4
description: "Formalize mathematical definitions and theorems in Lean 4 and Mathlib. Use for exact statement translation, incremental term or tactic proofs, lemma reuse and checker-verified mathematical results."
---

# Prove with Lean 4

## Workflow

1. Inspect the project's Lean and Mathlib pins, imports, namespaces and proof style. State the intended domains, quantifier order, hypotheses and conclusion before writing the declaration. A checked theorem with extra hypotheses or a changed domain does not establish the requested claim.
2. Encode the statement explicitly where inference could change meaning: annotate numeric types, casts, binder types and universe parameters. Check natural-number subtraction, division, interval endpoints, and finite versus infinite sums against the informal claim.
3. Search existing project lemmas and Mathlib before rebuilding results. Confirm candidate signatures in the pinned environment; use `search-mathlib` when discovery is the main obstacle.
4. Build a proof in small steps. Use `intro`, `constructor`, `cases`, `obtain`, `have`, `calc` and explicit witnesses to expose the mathematical structure. Choose `exact` or `apply` for matching lemmas, `rw` for deliberate equalities and `simp` for normalization. Make the relevant hypotheses available to automation.
5. Match automation to the goal: `ring` for polynomial identities, `norm_num` for numerical facts, `linarith` for linear ordered arithmetic, and `omega` for supported natural/integer arithmetic. Verify tactic availability in the pinned imports. Division cancellation needs nonzero hypotheses; polynomial normalization alone does not establish inequalities.
6. Run `lake env lean Path/To/File.lean` after coherent edits and `lake build` for the affected target. Resolve all obligations before calling the result proved. Temporary `sorry` is an explicit draft marker, never evidence of completion.
7. Report the final encoded statement and its correspondence to the requested claim, checker commands and results, and remaining assumptions. Use `audit-lean4-proofs` for a dedicated dependency audit. If the checker cannot run, return a labeled unchecked draft.

## Resources

Read [proof playbook](references/proof-playbook.md) for examples, tactic choices and acceptance checks. [CoreProof.lean](assets/CoreProof.lean) demonstrates an explicit witness without Mathlib; [MathlibProof.lean](assets/MathlibProof.lean) uses polynomial normalization. Use `debug-lean4-proofs` for elaboration or tactic failures without weakening the theorem.
