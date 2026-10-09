# Research Statistical Learning Theory: playbook

## Finite-class calculation

For a fixed class of M hypotheses with IID zero-one losses on n examples, Hoeffding plus a union bound gives simultaneous deviations at most `sqrt(log(2M/delta)/(2n))` with probability at least `1-delta`. Thus an empirical minimizer over the supplied candidates has excess risk at most twice this radius relative to the best supplied candidate, on the same event.

If only part of a larger predeclared class is evaluated, use its full cardinality M for the simultaneous bound, but do not call the selected candidate an ERM over unevaluated hypotheses. The helper names its comparator accordingly. Clip risk intervals to [0,1] and explicitly identify bounds that cover the whole possible range.

## Acceptance cases

- Repeatedly tuned models on the same sample: a fixed-class assumption needs justification.
- Correlated observations: the IID bound is unavailable without a suitable replacement theorem.
- Class cardinality exceeds supplied candidates: retain the larger union bound and restricted comparator.
- Radius is larger than one: report a vacuous bound rather than a successful guarantee of useful accuracy.
- Low training loss: do not equate it with low population risk.

## Primary sources

[Shalev-Shwartz and Ben-David, Understanding Machine Learning](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/) for learning-theory definitions and guarantees.
