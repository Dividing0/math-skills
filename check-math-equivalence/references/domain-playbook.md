# Equivalence as two maps with preserved domains

## Method branches
1. For algebraic rewriting, list the original domain before factoring, cancellation, logarithms or reciprocals. Multiplication by a nonzero function is reversible only on the set where that function does not vanish; division can erase entire solution components.
2. For changes of variables, construct an inverse or describe fibers. A bijective substitution preserves solutions exactly. A many-to-one substitution can still support existence statements, but uniqueness and multiplicity require separate accounting.
3. For differential equations, differentiate an integral formulation only with enough regularity and retain initial conditions. Integrating a differential equation introduces constants and needs boundary data to recover the intended solution set.
4. For optimization formulations, distinguish equal feasible sets, equal optimal values and a bijection between optimizers. An epigraph reformulation may introduce extra feasible points while preserving the objective minimum under explicitly checked conditions.

## Worked calculation
Over real x, log(x)=2 is equivalent to x=exp(2). The original domain requires x>0. Exponentiation gives x=exp(2), which satisfies that requirement. Conversely, the real logarithm of exp(2) is 2, establishing both directions. This argument uses injectivity and inverse relations on the positive-real domain, not a formal symbol cancellation.

## Tempting inference and counterexample
The equations x(x-1)=0 and x-1=0 are not equivalent over the reals: x=0 solves the first and not the second. Cancelling x is legitimate only after splitting off the x=0 branch or restricting the domain to x≠0. State which restriction changes the problem.

## Stop and handoff
Stop at a one-way implication if no inverse transformation has been proved. Return a table of domain restrictions, forward maps, backward maps and exceptional branches. Pass unresolved regularity or branch-choice obligations to proof construction. Numerical agreement of two formulations is useful for debugging but cannot establish exact equivalence over their full domains; attach the precise examples tested rather than generalizing their agreement.
