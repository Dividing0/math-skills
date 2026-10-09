# Domain playbook: research-combinatorics

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. Use a bijection when the objects can be encoded with recoverable information. Specify labeled versus unlabeled objects, prove both injectivity and surjectivity, and include empty-object or zero-size conventions.
2. Use recurrence or generating functions when a canonical first component decomposes objects. Prove disjointness and completeness of the decomposition and derive initial values before extracting coefficients; formal power series need no analytic convergence but analytic asymptotics do.
3. Use orbit counting for symmetries with stabilizers: count fixed objects for every group element and average. Dividing the total by group size is justified only for a free action. For extremal problems combine an upper bound with a construction attaining it; small-case enumeration is a consistency check, not a proof for every size.

## Worked derivation

Binary necklaces of length three under rotation: the identity fixes all eight strings. Each of the two nonidentity rotations fixes only 000 and 111, since all positions must agree. Burnside's average gives (8+2+2)/3=4 orbits. Representatives are 000,111,001,011; reversals have not been included as an additional symmetry.

## Invalid inference and witness

Counting those necklaces as 8/3 is invalid because the action is not free: 000 and 111 have stabilizer size three. The noninteger result reveals overcounting, but even an integer quotient can accidentally agree without proving freeness.

## Stop and handoff

Return the object class, symmetry group and counting derivation with boundary conditions. Hand off asymptotic coefficient extraction when singularity or error-control hypotheses are not available. For claimed optimality require both a bound and a matching construction.
