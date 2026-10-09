---
name: prove-with-fixed-points
description: "Prove fixed-point statements using Banach, Brouwer or Schauder arguments. Use when checking completeness, invariance, contraction or compactness, separating existence from iteration convergence, or deriving stopping bounds."
---

# Доведення через нерухомі точки

## Workflow

1. Choose a complete metric space or appropriate compact convex domain.
2. Verify that the proposed map preserves that domain.
3. Choose contraction, compactness or another theorem and verify every hypothesis.
4. Derive existence, uniqueness and iteration convergence separately.
5. For contraction obtain a posteriori error bounds and distinguish exact arithmetic from rounded computation.

## Evidence discipline

State exact hypotheses and domains; separate proof, conjecture, observation and conditional result. Verify external theorem assumptions and source locators. Do not invent citations, novelty or tool outcomes. Use the user’s language. Read the decision guide and acceptance cases before completing work; load neighboring skills only when needed.

## Deepening

Read [decision-guide.md](references/decision-guide.md) for method-selection checkpoints, additional behavioral cases and the output contract. Read [acceptance-cases.md](references/acceptance-cases.md) for the domain-specific boundary case. Treat these cases as acceptance checks, not evidence of generalization.

Read [method-selection.md](references/method-selection.md) for candidate techniques, their selection conditions and failure alternatives. Use it together with this specialization’s exact workflow.

Read [domain-playbook.md](references/domain-playbook.md) when choosing a theorem, deriving a result or auditing a conclusion in this skill; it supplies specialized branches, worked derivations and failure witnesses.
