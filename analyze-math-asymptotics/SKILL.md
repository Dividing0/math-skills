---
name: analyze-math-asymptotics
description: "Derive Taylor, dominant-balance and integral asymptotics with explicit parameter regimes, uniformity and remainder estimates. Use when expanding a formula, comparing growth rates or auditing a formal approximation."
---

# Analyze Math Asymptotics

## Workflow

1. State the limiting parameter, direction, domain and whether other parameters remain fixed or vary.
2. Identify dominant balances, scales, boundary layers and singular points; specify a regime before expanding.
3. Derive terms using an appropriate expansion, comparison, perturbation or integral method; track the remainder.
4. Distinguish O, o, asymptotic equivalence, convergent series and formal series. Specify uniformity and constants where needed.
5. Check consistency across regimes and against exact cases; use numerical tests as diagnostics, not as remainder proofs.
6. Return the expansion, regime, justified error estimate and transition limits; label unproved error orders explicitly.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.
