---
name: research-probability-theory
description: "Analyze probability laws, dependence, conditional expectations and convergence modes. Use when auditing limit theorems, exchanging expectations/limits or distinguishing stationary Markov laws from mixing."
---

# Research Probability Theory

## Workflow

1. Specify the probability space, random variables and dependence assumptions.
2. Distinguish independence, conditional independence and uncorrelatedness.
3. State the mode of convergence and verify moments or tail assumptions of limit theorems.
4. Check conditional distributions and null-event subtleties before interpreting probabilities.

## Evidence and completion rules

Keep a ledger distinguishing supplied facts, externally verified results, proved claims, conjectures and computational observations. State domains, quantifiers, assumptions and unresolved obligations. Verify external theorem hypotheses at their application site and cite a precise primary-source locator when available; never invent references. Read supplied source material before relying on it. Report actual commands and checker outcomes only when tools ran. Treat finite examples and plots as evidence rather than unrestricted proofs.

Use the user’s language. Load only relevant adjacent skills: use proof review for auditing, counterexample search for falsification, and existing algorithm or numerical implementation skills for software work. Pass the exact statement, assumptions and unresolved obligations to subsequent work. Read [acceptance-cases.md](references/acceptance-cases.md) before declaring completion.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

For finite Markov chains, check stochasticity, support, irreducibility and periodicity separately. Distinguish stationary-distribution uniqueness, positivity and convergence of iterates.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when selecting concrete methods, deriving a worked result or checking a boundary inference; it records domain-specific hypotheses and handoff obligations.
