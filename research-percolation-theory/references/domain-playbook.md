# Domain playbook: research-percolation-theory

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For finite graph connectivity probabilities under independent bond percolation, enumerate open-edge configurations or use deletion–contraction; retain edge independence when multiplying probabilities.
- For an infinite graph, define the root infinite-cluster event through connections to arbitrarily distant boundaries. Finite-size crossing estimates require a limiting argument to determine an infinite-volume statement.
- For subcritical bounds on a bounded-degree graph, count self-avoiding paths and use a union bound. This yields sufficient nonpercolation ranges, not usually an exact threshold; dependent models need different probability estimates.

## Worked valid example

On a triangle with independent edge-open probability p, vertices a and b are connected either through the direct edge or, when it is closed, through both edges via c. These disjoint cases give P(a↔b)=p+(1-p)p². At p=1/2 the result is 5/8. Independence applies to the two distinct edges in the indirect path, and disjointness applies to the decomposition by the direct edge.

## Tempting inference and counterexample

Marginal probabilities do not determine connectivity. On the same triangle, let all three edges share one Bernoulli(p) state. Every edge still has marginal p, but P(a↔b)=p rather than p+(1-p)p². Applying an independent-bond formula to dependent bonds overstates connectivity.

## Stop conditions and handoff

Stop threshold claims without graph geometry, site/bond convention and dependence assumptions. Hand off boundary events, limiting order and rigorous versus empirical probability estimates. Reference: H. Duminil-Copin, Introduction to Bernoulli percolation, https://www.unige.ch/~duminil/publi/2017percolation.pdf, section 1 model definitions and phase transition.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
