# Word metrics and coarse statements

## Choose a branch
- Word-length comparison: for finite generating sets S,T of a group, express each generator of one set as a bounded-length word in the other. The maximum lengths give two-sided Lipschitz bounds for the two word metrics. Infinite generating sets need not have such uniform constants.
- Growth computation: fix the generating set and radius convention, then count elements rather than words. Relations cause many words to represent the same element. Growth type can survive finite-generator changes although exact ball counts change.
- Quasi-isometry obstruction: define multiplicative and additive constants and coarse surjectivity. Use an invariant only with its hypotheses, such as finitely generated groups with their proper word metrics. Coarse equivalence does not retain torsion or literal multiplication tables.

## Worked metric comparison
For Z let S={-1,1} and T={-2,-1,1,2}. The S-length of n is |n|, whereas T-length is ceil(|n|/2): each step changes n by at most two and a word with steps of size two plus at most one of size one attains that bound. Thus |n|/2<=length_T(n)<=|n| for n≠0, and both vanish at zero. Exact metric distances differ but the identity gives a quasi-isometry. The S-ball has 2r+1 elements for integer r>=0.

## Tempting inference and counterexample
A group with an infinite generating set can lose its usual coarse geometry. Give Z every nonzero integer as a generator. Then any two distinct elements have distance one, so the entire group is a bounded metric space. With the finite set {-1,1}, distances are unbounded. The preceding finite-generator proof cannot apply: lengths of all new generators in the old metric have no common finite bound.

## Stop or hand off
If a requested hyperbolicity, boundary or growth theorem needs local finiteness or finite generation, state that need before applying it. Hand an algebraic isomorphism problem to algebra; quasi-isometry alone cannot solve it. Deliver presentation, generating sets, relation handling, constants and the exact equivalence level proved. A plotted Cayley graph fragment can suggest growth but does not certify asymptotic behavior.
