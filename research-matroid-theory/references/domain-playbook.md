# Exchange, representations and greedy claims

## Choose a branch
- Independent-set axioms: for a finite ground set E, verify the empty set belongs to I, heredity, and augmentation: if A,B in I with |A|<|B|, some element of B\A extends A independently. Heredity alone describes a broader independence system.
- Linear representation: specify a field and labeled column vectors. Independence means linear independence of the chosen columns. Elementary field-dependent determinants decide bases; changing the field can change representability.
- Greedy optimization: for a finite matroid and real weights, sorting descending and adding each feasible element finds a maximum-weight basis. For maximum-weight independent sets, skip negative weights, or impose nonnegative weights. Distinguish the basis problem from the unconstrained-cardinality problem.

## Worked rank calculation
Over Q take columns a=(1,0), b=(0,1), c=(1,1). Each singleton is independent, every pair is independent because its determinant is nonzero, and the triple is dependent with c=a+b. This represents the uniform matroid U_(2,3). Its rank function is r(A)=min(|A|,2). With weights w(a)=5,w(c)=4,w(b)=1, descending greedy accepts a,c and rejects b, giving weight 9. Comparing all three bases gives 9,6,5, independently verifying the result.

## Tempting inference and counterexample
Heredity does not suffice for greedy optimality. Let E={a,b,c} and I={empty,{a},{b},{c},{b,c}}. This is hereditary but violates augmentation from {a} to {b,c}. Weights 3,2,2 make descending greedy choose {a}, weight 3, while {b,c} has weight 4. Diagnose the missing exchange axiom rather than adjusting tie-breaking, since there is no tie in the first choice.

## Stop or hand off
If a claimed representation is over an unspecified field, return determinant conditions instead of universal representability. For deletion or contraction, name the element set and rank convention; verify contraction via r_(M/C)(A)=r_M(A union C)-r_M(C) on disjoint A. Hand nonmatroid feasible families to general combinatorial optimization with the failing augmentation witness. Deliver the axiom verification, representation and exact objective class before asserting any greedy guarantee.
