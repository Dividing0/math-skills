# Domain playbook: analyze-perturbations

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. Use a regular expansion only when the limiting problem preserves constraints and the linearized equation for correction terms is invertible in the stated norm. An implicit-function argument needs a bounded inverse, not only a formal derivative.
2. When the highest derivative disappears or boundary conditions cannot be satisfied by the reduced equation, introduce an inner scale by balancing terms. Solve outer and inner problems, match their overlap and subtract their common part in a composite approximation.
3. For long-time oscillatory problems, inspect secular terms and resonances. Multiple scales or averaging requires a specified time horizon; a small remainder at fixed time need not remain small at times proportional to the inverse small parameter.

## Worked derivation

For εy'+y=1, y(0)=0, ε>0, direct integration gives y(t)=1−exp(−t/ε). The outer equation y=1 misses the initial value. With τ=t/ε, the inner problem Y'+Y=1, Y(0)=0 gives Y=1−e^(−τ); it matches the outer value 1. On t≥δ>0 the outer error is at most e^(−δ/ε), whereas on [0,T] its supremum is 1.

## Invalid inference and witness

Uniformly replacing y by 1 on [0,T] because the exponential tends to zero for every t>0 is invalid: at t=0 the error stays 1. Pointwise convergence away from a layer does not imply uniform convergence across it.

## Stop and handoff

Return the small-parameter range, observation norm and time interval with every remainder. If only a formal series is known, hand off the remainder estimate and solvability conditions rather than claiming asymptotic validity.
