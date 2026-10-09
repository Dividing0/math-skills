---
name: review-math-proofs
description: "Use for checking submitted proofs, theorem applications, logical gaps, circularity and the distinction between a correct claim and a valid argument."
---

# Review Math Proofs

## Workflow

1. Restate the claim and definitions before auditing. Preserve the submitted argument and assign locations to substantive steps.
2. Build a dependency ledger of hypotheses, lemmas and cited results. Check every inference and theorem application, including quantifier scopes and variable dependencies.
3. Test vulnerable steps using edge cases or counterexamples. Audit induction bases, uniformity, limit exchanges, representative choices and existence assumptions as relevant.
4. Classify findings as fatal contradiction, missing justification, missing hypothesis, fixable presentation issue or verified step; give evidence and a concrete repair where possible.
5. Keep validity of the statement separate from validity of the proof. Do not silently replace the argument and then endorse the original.
6. Return a scoped verdict, findings with locations, remaining obligations and any corrected proof clearly marked. Claim formal verification only if an actual checker completed successfully with stated axioms and no unresolved placeholders.

## Evidence and output discipline

Maintain a ledger separating given facts, verified external results, proved claims, conjectures and computational observations. State assumptions and unresolved obligations explicitly. Cite external mathematical results with a verifiable source and precise locator when available; do not invent references. Read supplied papers before relying on their contents. Use tools only when they improve verification and state which checks actually ran. Respect the user’s language.

Read [acceptance-cases.md](references/acceptance-cases.md) to check the intended boundary behavior before completing a task. Hand off downstream work with the exact statement, assumptions, evidence and remaining obligations; load other skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Host computation

When the `manage-math-research` skill is installed alongside this skill, check the declared claim dependency ledger for cycles and unresolved prerequisites; proof content and theorem application hypotheses still require mathematical review. Use its [dependencies.py](../manage-math-research/scripts/dependencies.py) helper and [input/command reference](../manage-math-research/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
