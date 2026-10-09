# Domain playbook: design-computer-assisted-proofs

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For finite enumeration, prove that the generator covers every admissible object, and verify each witness with exact integer or rational arithmetic. A symmetry reduction needs a proof that every orbit has a representative.
- For continuous domains, subdivide with outward-rounded interval arithmetic and verify every box or supply an analytic remainder bound. Coverage, singular boxes and boundary points are proof obligations, not implementation details.
- For algebraic certificates, make the generator untrusted and verify polynomial identities, sign restrictions or dual constraints with a smaller checker. A certificate proves the encoded statement only after equivalence to the original claim is justified.

## Worked valid example

To prove x²-2 has exactly one root in [1,2], first establish f(1)=-1 and f(2)=2 and continuity, giving existence. On this interval f'=2x≥2, giving uniqueness. Exact rational evaluations at 7/5 and 3/2 give -1/25 and 1/4, tightening the enclosure. Computation can check these rational identities, while the analytic monotonicity argument covers every real input between them.

## Tempting inference and counterexample

Floating-point cancellation can misclassify a sign. In binary64, forming (10^16+1)-10^16 typically returns 0 although the exact integer expression is 1. A program accepting nonpositivity from that result cannot certify the corresponding exact inequality.

## Stop conditions and handoff

Stop if interval coverage, arithmetic semantics, termination or input encoding is unproved. Hand off a list of analytic lemmas, exhaustive computational obligations, certificate formats and the explicitly trusted components to certificate verification.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
