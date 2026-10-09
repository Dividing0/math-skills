# Domain playbook

## Select the method

1. For logical audits, label each substantive step and its dependencies. Check arbitrary-variable choices, quantifier scope and whether a claimed witness depends on data that should be fixed independently.
2. For theorem applications, compare the exact hypotheses with the current objects at the use site. Compactness, invertibility, independence and uniformity are common missing premises; an appropriate theorem name alone is not evidence.
3. For repair, separate a locally fixable inference from a false statement. Preserve the original verdict, then present any corrected proof under explicit changed assumptions. Formal checking requires actual successful execution and a declared axiom/placeholder audit.

## Worked check

Audit: “If n² is even, write n²=2k, divide by n, and get n=2(k/n), hence n is even.” The conclusion is true, but the proof is invalid because k/n need not be an integer and n may be zero. Repair by contrapositive: n=2m+1 implies n²=2(2m²+2m)+1, odd. This verifies the theorem without endorsing the submitted argument.

## Invalid inference and witness

A plausible induction can fail at its overlap. The all-horses-same-color argument compares two overlapping groups of size n inside a group of n+1. For n=1 the groups do not overlap, so no common horse equates the colors. Two differently colored horses refute the conclusion and locate the first broken step.

## Completion and handoff

Return a scoped verdict, step locations, severity, counterevidence and repairs. Do not call an unexamined long proof verified because a sampled section is correct. Hand construction the exact gap and available assumptions; hand formalization a repaired complete statement and proof while marking the original proof's status separately.
