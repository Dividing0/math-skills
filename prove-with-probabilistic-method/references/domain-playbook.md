# Domain playbook

## Select the method

1. For expectation arguments, define an integrable random count. If its expectation is positive, some outcome has positive count; if expected defects are below one and the count is a nonnegative integer, some outcome has zero defects.
2. For union bounds, enumerate the bad events and sum their probabilities. Independence is unnecessary for this bound, but each probability still needs justification. A sum strictly below one proves positive probability of avoiding all events.
3. For alteration, first sample an object, then remove or repair defects and bound the expected retained objective. For conditional-expectation derandomization, require efficiently computable conditional expectations and a sequence of choices that preserves the relevant bound.

## Worked check

Independently two-color vertices of K4. Each of its four triples is monochromatic with probability 2/8=1/4, so the expected number of monochromatic triples is one. This alone does not prove zero defects. An explicit coloring with two vertices of each color does have zero monochromatic triples, demonstrating why strict thresholds and the exact conclusion matter.

## Invalid inference and witness

A bound at one is insufficient: on a space where a nonnegative integer variable X is identically one, E[X]=1 yet P(X=0)=0. Likewise existence of a good random outcome says nothing about how quickly rejection sampling finds it unless the success probability is bounded below.

## Completion and handoff

Return the probability space, event dependencies, exact inequality and existential conclusion. Stop when a required dependency bound is unproved; do not invoke a local lemma by name alone. Hand algorithm design a success-probability bound, sampling access and certification test if a constructive method is requested; distinguish those obligations from the existence proof.
