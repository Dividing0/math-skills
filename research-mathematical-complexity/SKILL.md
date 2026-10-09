---
name: research-mathematical-complexity
description: "Prove complexity upper bounds, verifier claims and reduction-based hardness for decision, search or counting problems; audit bit encoding, reduction direction and resource cost."
---

# Теорія складності обчислень

## Workflow

1. Specify decision, search or counting problem and input encoding.
2. Define computational model, resource measure and uniformity.
3. Verify reduction direction, correctness and resource cost.
4. Distinguish hardness, completeness, undecidability and practical runtime.
5. State conditional separations and randomized or approximation variants precisely.

## Evidence and output discipline

State exact domains, quantifiers and assumptions. Separate proved claims, external results, conjectures and observations. Check theorem hypotheses at every application; cite primary sources with precise locators when available and never invent references. Label conditional results and unresolved obligations explicitly. Use computation for discovery or validation without promoting finite samples to proof. Report actual checker and tool outcomes only when executed.

Use the user’s language. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion. Combine this specialization with the existing proof, counterexample, literature or implementation skills only as the task requires. Pass explicit assumptions and remaining obligations to downstream work.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a method, checking a proof or interpreting a boundary case in this skill; it gives exact prerequisites, a worked derivation, a counterexample and handoff obligations.
