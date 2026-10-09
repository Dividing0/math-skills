---
name: research-measure-theory
description: "Analyze measurable functions, almost-everywhere classes, integration, convergence theorems and product measures; audit domination, monotonicity and Fubini or Tonelli hypotheses."
---

# Research Measure Theory

## Workflow

1. Specify the sigma-algebra, measure, completeness and relevant finiteness conditions.
2. Check measurability and distinguish pointwise identities from almost-everywhere equivalence.
3. Verify domination, monotonicity, integrability or nonnegativity before convergence and Fubini-type theorems.
4. Treat signed and complex integration separately and track null sets.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.

## Host computation

When the `research-probability-theory` skill is installed alongside this skill, compute a specified finite joint law, including exact marginals/dependence and numerical base-2 entropies; no continuous or asymptotic conclusion follows. Use its [finite_probability.py](../research-probability-theory/scripts/finite_probability.py) helper and [input/command reference](../research-probability-theory/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
