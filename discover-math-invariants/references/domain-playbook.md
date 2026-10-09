# Domain playbook: discover-math-invariants

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For a differentiable autonomous ODE x'=F(x), test a scalar candidate I by ∇I·F=0 throughout the domain. Show solutions remain in that domain; conservation only follows along intervals where the chain rule and solution regularity hold.
2. For a discrete map or group action, compute I(Tx)=I(x) for every allowed generator. Invariance for one generator extends to compositions, but only if all intermediate states are admissible.
3. For PDE or integral invariants, derive the flux balance including boundary terms. Closed boundaries, periodicity or decay can make the flux vanish; open boundaries generally do not. For classification distinguish an invariant from a complete invariant and seek different objects sharing its value.

## Worked derivation

For x'=y and y'=−x, take I=x²+y². Then I'=2xx'+2yy'=2xy−2yx=0, so each trajectory stays on its initial circle. For I>0 this bounds both coordinates and, since the vector field is globally Lipschitz, the solution exists for all time. The calculation does not make x or y separately constant.

## Invalid inference and witness

Equal trace does not classify matrices up to similarity: diag(1,−1) and the zero matrix both have trace zero, but their determinants are −1 and 0. An invariant mismatch rules out equivalence; a match need not establish it.

## Stop and handoff

Report the exact transformation class, admissible state domain and conservation calculation. If numerical drift is observed, separate discretization error from failure of the mathematical invariant. Pass classification claims to additional invariants or a completeness proof.
