---
name: research-numerical-analysis
description: "Analyze numerical error, conditioning, stability, consistency and convergence; relate residuals to returned-solution error and distinguish empirical refinement from rigorous certification."
---

# Research Numerical Analysis

## Workflow

1. Specify the exact problem, conditioning, error targets and arithmetic.
2. Separate truncation, iteration, rounding and input errors.
3. Check consistency, stability and convergence under the appropriate theorem hypotheses.
4. Use independent reference cases and refinement studies; distinguish empirical convergence rate from a proved guarantee.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Separate residual, solution error, iteration error and rounding. Verify the iterate to which an a posteriori bound applies; a float64 evaluation of an exact-arithmetic bound is not a certified enclosure.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a domain-specific method, checking applicability hypotheses, or needing a worked derivation and a failure witness. Its explicit gates refine the family-level guide.
