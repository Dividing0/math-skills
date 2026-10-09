---
name: research-real-analysis
description: "Analyze limits, continuity, differentiation and integration over real domains. Use for uniform-versus-pointwise convergence, compactness hypotheses, limit exchanges, derivative control and endpoint counterexamples."
---

# Research Real Analysis

## Workflow

1. State domains and pointwise, uniform, almost-everywhere or norm convergence explicitly.
2. Track completeness, compactness and continuity requirements at each theorem application.
3. Check endpoint behavior and local versus global conclusions.
4. Justify limit exchanges and differentiation using precise hypotheses and counterexamples.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.

## Host computation

When the `compute-with-sympy` skill is installed alongside this skill, use `simplify`, `factor`, `differentiate`, `integrate` or `solve` on specified expressions; retain denominator exclusions and branch assumptions. Use its [calculate.py](../compute-with-sympy/scripts/calculate.py) helper and [input/command reference](../compute-with-sympy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
