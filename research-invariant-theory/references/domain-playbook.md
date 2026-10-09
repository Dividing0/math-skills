# Domain playbook

## Select the method

1. For finite groups over a field whose characteristic does not divide the group order, averaging f over the action produces an invariant polynomial. Record the division by |G|; in modular characteristic that averaging formula is unavailable.
2. For explicit invariant rings, apply the action to each monomial or generator, prove every proposed generator invariant, and prove generation separately. Finding several invariants is not a proof that all invariants are their polynomials.
3. For orbit separation, distinguish actual orbits from closed-orbit or orbit-closure statements. Specify the field and action, and check any reductivity hypotheses before using a quotient theorem.

## Worked check

Let the two-element group act on R[x] by x->-x. Write f=sum a_j x^j. The equality f(-x)=f(x) forces a_j=0 for every odd j, because characteristic is zero. Thus the invariant ring is R[x²]. Conversely every polynomial in x² is fixed, proving both inclusion directions rather than only invariance of one generator.

## Invalid inference and witness

Invariant equality can fail to distinguish orbits. For R* acting on R by multiplication, every invariant polynomial is constant: invariance under x->2x forces every positive-degree coefficient to vanish. Nevertheless {0} and R minus {0} are different orbits, so identical invariant values do not imply orbit equality.

## Completion and handoff

Return the group, coefficient field, action on points and functions, invariant generators, relations and separation claim. Stop if generation or quotient hypotheses are unproved. Hand computational algebra exact action equations and coefficient domain; hand geometry orbit-closure questions while preserving the difference between invariant evaluation and actual orbit membership.
