# Domain playbook: research-branching-processes

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For a single-type Galton–Watson process, require independent identically distributed nonnegative integer offspring and a finite initial population. Write the probability generating function f(s); extinction from one ancestor is the smallest fixed point of f on [0,1], obtained by iterating from zero.
2. For mean growth, if m=Eξ is finite, conditioning yields E[Z_(n+1)|Z_n]=mZ_n and E Z_n=Z_0m^n. This is an expectation identity, not a sample-path growth or survival theorem.
3. At criticality inspect the degenerate offspring law ξ=1 almost surely separately. Multi-type, environment-dependent or dependent offspring models require their own conditions; a scalar mean from the single-type model does not automatically decide their extinction behavior.

## Worked derivation

Take offspring probabilities P(ξ=0)=1/4 and P(ξ=2)=3/4. Then f(s)=1/4+3s²/4 and m=3/2. Solving f(s)=s gives 3s²−4s+1=0, with roots 1/3 and 1. Iteration from zero selects q=1/3, so survival from one ancestor is 2/3. From two independent ancestors, both lines must die for extinction, yielding q²=1/9.

## Invalid inference and witness

Expected growth does not guarantee certain survival: this same supercritical process has E Z_n=(3/2)^n but extinction probability 1/3. Conversely, deterministic one-offspring reproduction has mean one and never becomes extinct from a positive initial population.

## Stop and handoff

Return the offspring law, independence structure, generating function, fixed-point selection and starting-population convention. Stop before applying martingale limit or conditioned-survival claims when moment or nondegeneracy assumptions have not been verified.
