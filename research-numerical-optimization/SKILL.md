---
name: research-numerical-optimization
description: "Select and audit gradient, Newton, projected or proximal optimization methods. Use when deriving steps and rates, checking oracle accuracy, conditioning and constraints, or separating stagnation, stationarity and global optimality."
---

# Чисельна оптимізація

## Workflow

1. Specify smoothness, convexity, constraints and oracle accuracy.
2. Choose algorithms according to conditioning, scale and available derivatives.
3. Verify derivatives independently and use meaningful stopping conditions.
4. Distinguish objective progress, stationarity, feasibility and global optimality.
5. Separate theorem assumptions from observed convergence and account for inexact linear solves or stochastic gradients.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.

## Host computation

When the `compute-with-scipy` skill is installed alongside this skill, use `linear-program` for an explicitly formulated finite LP; inspect solver status and feasibility, and use exact certificates when a proof is required. Use its [numerical.py](../compute-with-scipy/scripts/numerical.py) helper and [input/command reference](../compute-with-scipy/references/command-line.md). `--example` prints a request to adapt; run the actual task with `--input /absolute/request.json` and retain the returned evidence scope and diagnostics.
