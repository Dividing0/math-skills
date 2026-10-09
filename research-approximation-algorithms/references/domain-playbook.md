# Domain playbook: research-approximation-algorithms

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For minimization with nonnegative optimum, establish feasibility and cost ALG≤ρ OPT using a lower bound on OPT. Handle OPT=0 explicitly rather than dividing by it.
- For LP rounding, first prove the relaxation contains every integral feasible solution, then show the rounding remains feasible and bound its cost inflation. Fractional feasibility alone does not provide a valid discrete output.
- For random algorithms, specify whether the guarantee is in expectation, with a stated probability, or for every seed. A conditional expectation argument can derandomize only when its conditional objective is computable efficiently.

## Worked valid example

In unweighted vertex cover, take a maximal matching M and output all its endpoints C. Any uncovered edge would have neither endpoint in C, so it could be added to M, contradicting maximality. Thus C is feasible. Every cover needs at least one endpoint of each disjoint matching edge, hence OPT≥|M|, while |C|=2|M|≤2 OPT. Maximality, not a maximum matching computation, is sufficient.

## Tempting inference and counterexample

The same endpoint rule has no factor-two guarantee for weighted cover. A single edge with endpoint weights 1 and 100 gives algorithm cost 101 and optimal cost 1. The unweighted cardinality proof cannot be reused with weights.

## Stop conditions and handoff

Stop a ratio claim if feasibility, input restrictions, objective sign or the comparison to OPT is missing. Hand off a worst-case family, polynomial-time argument, randomness interpretation and verified bound to algorithm implementation.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
