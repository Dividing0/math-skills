# Domain playbook

## Select the method

1. For monotone convergence, require measurable nonnegative functions increasing almost everywhere. No integrable dominator is necessary, but the resulting integral may be infinite; signed sequences require a different justification.
2. For dominated convergence, identify a single integrable bound independent of the index and almost-everywhere convergence. Pointwise convergence or uniformly bounded integrals alone is insufficient.
3. For iterated integration, use Tonelli for nonnegative measurable functions on the stated product spaces, and Fubini for absolute integrability under the appropriate sigma-finiteness hypotheses. For signed integrands check positive and negative parts before subtracting infinities.

## Worked check

On (0,1) with Lebesgue measure, f_n(x)=min(n,x^(-1/2)) increases to x^(-1/2). Monotone convergence applies, and integral_0^1 x^(-1/2) dx=2. Alternatively the same limit is integrable and dominates every f_n, so dominated convergence also gives convergence of their integrals. The hypotheses are checked, not inferred from the answer.

## Invalid inference and witness

A null-set statement does not determine pointwise values. The indicators of {0} and the empty set on R agree almost everywhere and have identical integrals, but differ at zero. An Lp class cannot be evaluated at a specified point without selecting a suitable representative and proving that operation meaningful.

## Completion and handoff

Return the measurable spaces, measures, completion conventions, convergence mode and exact theorem assumptions. Stop when positive and negative parts both have infinite integral or no dominator has been verified. Hand probability the normalized measure and event definitions; hand functional analysis equivalence classes rather than arbitrary pointwise representatives.

Before reporting success, recheck the selected branch against the exact requested conclusion. Record which premises came from the user and which were derived. A missing premise must remain an explicit obligation, with a concrete description of the additional input or proof needed to continue.
