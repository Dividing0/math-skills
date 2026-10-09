# Domain playbook

## Select the method

1. For induction over natural numbers, state the initial index, verify the base, and prove P(n) implies P(n+1) using only permitted hypotheses. Strong induction may use earlier indices but cannot presuppose the target case.
2. For contrapositive, convert every quantified statement carefully. Proving not Q implies not P establishes P implies Q; showing one failed P is irrelevant to a universal implication.
3. For existence via compactness, specify the topology, obtain an actually convergent subnet or subsequence under the appropriate theorem, and verify closedness and continuity at the limit. For uniqueness, compare arbitrary candidates with a separate inequality or structural argument.

## Worked check

For n>=1, prove 1+...+n=n(n+1)/2. At n=1 both sides are one. Assuming the formula at n, addition of n+1 gives n(n+1)/2+(n+1)=(n+1)(n+2)/2. The induction hypothesis and algebra discharge the successor step, so the claim holds for every integer n>=1.

## Invalid inference and witness

A true statement can still have a circular proof. “Every even integer is divisible by two because every even integer has the required divisibility” merely repeats the conclusion unless evenness was explicitly defined that way. More sharply, cancelling a in ab=ac without a!=0 is invalid: a=0,b=1,c=2 satisfies the equation and violates b=c.

## Completion and handoff

Return the exact theorem and proof dependencies, not an unlabelled sketch. If a lemma is unresolved, name its statement and the precise use site. Hand counterexample search the full hypotheses when validity is doubtful; hand formalization a complete informal argument and the chosen axioms, while keeping checker execution status separate.
