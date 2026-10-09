# Domain playbook: generalize-math-results

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. To weaken a hypothesis, annotate the original proof step by step and locate its use. Replace that step with a new lemma under the proposed weaker condition; preserving the conclusion without a repaired proof is a conjecture.
2. To enlarge a space or domain, test compactness, completeness and finiteness properties independently. In infinite dimensions distinguish strong and weak topologies, sequential arguments and the additional lower-semicontinuity needed by variational proofs.
3. To sharpen a bound or extend a parameter range, construct extremal or limiting examples first. Show the old theorem follows from the new statement through an explicit embedding or parameter specialization, and check endpoint or equality cases separately.

## Worked derivation

The estimate |f(x)−f(y)|≤M|x−y| for differentiable f on an interval with |f'|≤M follows from the mean-value theorem. It extends to absolutely continuous f whose derivative satisfies |f'|≤M almost everywhere: f(x)−f(y)=∫_y^x f'(t)dt, hence the same bound. Absolute continuity supplies the integral representation; merely assuming an almost-everywhere derivative is insufficient.

## Invalid inference and witness

The Cantor function is continuous, has derivative zero almost everywhere, and increases from 0 to 1. Therefore replacing absolute continuity by continuity plus derivative zero almost everywhere would falsely imply that it is constant. The failed extension identifies precisely the lost integral-representation step.

## Stop and handoff

Separate proved extension, failed extension and conditional extension. Return a hypothesis-to-proof dependency map and the original-as-special-case argument. Transfer literature or sharpness claims only with verified sources or matching lower bounds.
