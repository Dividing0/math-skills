---
name: perform-symbolic-computation
description: "Transform and solve symbolic expressions while preserving exact coefficients, domains and branches. Use for factoring, rational equations, radicals, logarithms, elimination or antiderivative verification."
---

# Perform Symbolic Computation

## Workflow

1. State the variable domains, parameter assumptions and branch conventions before using a computer algebra system.
2. Keep exact integers and rationals exact; do not introduce floats unless an approximation is requested.
3. Select factoring, elimination, differentiation, integration or solving to match the requested output; record substitutions and exceptional parameter values.
4. Check transformations for equivalence: cancellation, squaring, logarithms and division may lose restrictions or introduce roots.
5. Substitute candidate solutions into the original expression; verify antiderivatives by differentiation on their stated domains.
6. Report the expression, conditions, excluded cases and exact versus numerical status. Record tool and version for executed calculations.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) before selecting a domain method or declaring its decisive conclusion; it gives exact hypotheses, a worked derivation, a counterexample and handoff requirements.
