# Domain playbook: verify-proof-certificates

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For algebraic identities, parse the exact coefficient domain and verify both sides after expansion or normalization. A certificate of ideal membership is an explicit combination of the original generators, not only a claimed remainder.
- For linear-programming optimality, independently check primal feasibility, dual feasibility and equality of objectives with the correct inequality conventions. A primal solution alone proves an attainable value, not optimality.
- For finite exhaustive certificates, check input identity, coverage, leaf conditions and all pruning rules. A hash binds an artifact to its bytes but does not prove the mathematical checker is sound.

## Worked valid example

For primal min x₁+x₂ with x₁+x₂≥1 and x≥0, the dual is max y with 0≤y≤1. The rational witness x=(1,0), y=1 satisfies both feasibility systems, and both objectives are 1. Weak duality therefore establishes optimum 1. A checker can verify these inequalities and equality using exact rationals; the derivation of the dual convention remains part of the mathematical justification.

## Tempting inference and counterexample

Checking only objective equality is unsound. For the same primal, x=(0,0) and y=0 have equal objectives 0, but x violates x₁+x₂≥1. Such a pair cannot certify optimality; every certificate condition is substantive.

## Stop conditions and handoff

Stop and label unverifiable when checker code, input binding or essential assumptions are unavailable; label invalid when a definite condition fails. Hand off exact artifacts, versions, arithmetic semantics, actual run results if any, and the statement justified conditional on checker soundness.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
