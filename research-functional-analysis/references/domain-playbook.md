# Domain playbook: research-functional-analysis

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For bounded linear maps between Banach spaces, use the open mapping or bounded inverse theorem only with completeness and surjectivity or bijectivity respectively. Establish linearity and the relevant domain first.
- For variational existence, use weak compactness and weak lower semicontinuity, often with reflexivity and coercivity. Boundedness of a sequence is insufficient for norm compactness in an infinite-dimensional space.
- For duality, distinguish weak convergence in X from weak-star convergence in X*. Identify the pairing and topology before using compactness; a dual ball may be compact without being sequentially compact in unrestricted settings.

## Worked valid example

Let H be a Hilbert space and y∈H. Minimize J(x)=||x||²-2 Re⟨x,y⟩. Completing the square gives J(x)=||x-y||²-||y||². Hence the unique minimizer is x=y and the minimum is -||y||². This direct proof needs no compactness claim and works in infinite dimension. Uniqueness follows because equality requires ||x-y||=0.

## Tempting inference and counterexample

A bounded invertible linear map can have an unbounded inverse if the target is incomplete. The identity from (C[0,1],||·||∞) to the same vector space with ||·||₁ is bounded and bijective, but narrow triangular spikes have sup norm 1 and integral tending to 0. Thus the inverse is not continuous; the target with integral norm is not Banach.

## Stop conditions and handoff

Stop theorem application until completeness, topology and all operator domains are established. Hand off the sequence, convergence notion, dual pairing and exact compactness or semicontinuity obligation.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
