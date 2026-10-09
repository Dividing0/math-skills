---
name: research-approximation-algorithms
description: "Analyze feasible solutions, relaxations and performance guarantees for approximation algorithms. Use when proving ratios against optimum, auditing rounding, or distinguishing expected from worst-case guarantees."
---

# Апроксимаційні алгоритми

## Workflow

1. Specify feasible solutions, objective direction and input restrictions.
2. Define multiplicative or additive approximation, including zero or negative optima.
3. Construct and validate feasible outputs separately from performance bounds.
4. Prove comparison with the true optimum through lower or upper bounds.
5. Track randomized expectation, high-probability and worst-case guarantees distinctly.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing methods or checking decisive claims; it supplies specialization-specific hypotheses, a worked derivation, counterexamples and handoff conditions.
