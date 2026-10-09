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

For an existing implementation, use [improve-lean4-code](../improve-lean4-code/SKILL.md) when refactoring is the task, [analyze-lean4-code](../analyze-lean4-code/SKILL.md) for weakness analysis, or [check-lean4-idiomaticity](../check-lean4-idiomaticity/SKILL.md) for a dedicated style review. Load these neighboring skills only when available and relevant.

## Host computation

When the `audit-lean4-proofs` skill is installed alongside this skill, run actual Lean file checks or named theorem axiom diagnostics in a pinned project; inspect checker output and verify correspondence to the mathematical claim separately. Use its [check_project.py](../audit-lean4-proofs/scripts/check_project.py) helper and [input/command reference](../audit-lean4-proofs/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.

## Related workflow

When reusable proof automation requires a macro, elaborator or tactic extension, use the metaprogramming workflow and check its generated proof terms. Read [metaprogram-lean4](../metaprogram-lean4/SKILL.md) when that specialization is needed and available.
