# Domain playbook: review-mathematical-manuscripts

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For correctness, build a dependency graph of main results and audit the first unsupported decisive lemma. State whether a failed proof disproves the theorem or merely leaves it unproved.
- For contribution, compare exact quantifiers, domains and assumptions with accessible primary prior work. A weaker hypothesis or sharper constant can matter even when titles sound identical; an incomplete search does not establish novelty.
- For computational claims, request the actual inputs, versioned code and checker logs. Distinguish successful reruns from source inspection and finite experiments from a theorem over an infinite input class.

## Worked valid example

A manuscript proves that a continuous f:[0,1]→R has a maximum. Its argument takes a maximizing sequence x_n, extracts a convergent subsequence by compactness, and uses continuity to obtain f(x*)=sup f. Each obligation is satisfied: f is bounded on the compact interval, x* stays in the interval, and continuity passes values to the limit. A constructive review can accept this argument while separately assessing originality and exposition.

## Tempting inference and counterexample

The same proof fails on (0,1): f(x)=x is continuous and bounded, but the maximizing sequence 1-1/n (n≥2) converges outside the domain. No maximum exists. This is a false statement under the changed hypotheses, not merely an incomplete citation or stylistic issue.

## Stop conditions and handoff

Stop an overall endorsement when a necessary appendix or theorem dependency is inaccessible. Hand off findings with exact proposition locations, severity, witness or repair and the review scope. Do not infer execution, novelty or referee consensus from missing evidence.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
