# Domain playbook: research-algebraic-number-theory

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For quadratic fields Q(√d) with squarefree d, determine the maximal order before calculating ideals: use Z[(1+√d)/2] when d≡1 mod 4 and Z[√d] otherwise. An arbitrary defining order can have a different discriminant and conductor.
2. For prime splitting, factor a minimal polynomial modulo p only after checking whether p divides the index of the chosen order in the ring of integers. Without this index condition the naive factorization-to-ideal correspondence can fail. Handle ramified primes separately through the field discriminant.
3. For factorization claims distinguish units, irreducibles, primes and ideals. The maximal order has unique factorization of nonzero ideals; unique factorization of elements requires the class-group obstruction to vanish. Use exact norms to rule out small factors, not floating-point embeddings.

## Worked derivation

For K=Q(√2), O_K=Z[√2]. Reducing t²−2 modulo 7 gives (t−3)(t+3), with distinct roots since 3²≡2 mod 7. The index is one, so 7O_K splits as (7,√2−3)(7,√2+3). Each quotient is F₇ by sending √2 to the indicated root, hence each ideal has norm 7; their product has norm 49 as does 7O_K.

## Invalid inference and witness

In Z[√−5], 6=2·3=(1+√−5)(1−√−5). The norm a²+5b² has no value 2 or 3, so the norm constraints establish these factors' irreducibility; they are not related by units. Unique ideal factorization therefore must not be replaced by unique element factorization.

## Stop and handoff

Report the field, maximal order, basis, discriminant and index checks with every splitting computation. If class-group or maximal-order computations are absent, stop at conditional claims and hand off the exact arithmetic obligations.
