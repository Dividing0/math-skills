---
name: research-statistical-learning-theory
description: "Analyze generalization, PAC learning, finite hypothesis classes, VC/Rademacher complexity and learning guarantees. Use for risk bounds, sample complexity and data-dependent selection assumptions rather than routine model fitting."
---

# Research Statistical Learning Theory

## Workflow

1. Define the data distribution, sample dependence, hypothesis class, loss, population risk and learning algorithm. Specify realizable versus agnostic, supervised versus other settings, and the probability over which a guarantee is claimed.
2. Decompose estimation, approximation and optimization error. An optimizer finding low empirical loss does not establish generalization; express what risk comparator is actually controlled.
3. Select a bound matching the loss and class: finite-class concentration, VC/growth-function, Rademacher or another justified complexity measure. Include constants, confidence level and all regularity/measurability assumptions needed by the chosen statement.
4. Account for model selection and reuse of data. A finite class chosen after inspecting the same labels is not automatically covered by a fixed-class union bound; use an independent evaluation set or an appropriate data-dependent theorem.
5. Compute bounds and check whether they are informative. The helper evaluates a simultaneous Hoeffding bound for a predeclared finite class and IID binary losses; it cannot infer independence or certify that a class was fixed in advance.
6. Report the theorem, comparator, assumptions, probability qualifier, numerical bound and any vacuity. Keep empirical performance, theoretical upper bounds and claims about deployment distribution distinct.

## Resources

Read the [domain playbook](references/playbook.md) for method choices, worked cases and acceptance checks.

Use [finite_class_bound.py](scripts/finite_class_bound.py) for its explicitly supported task family. It accepts JSON via `--input` or stdin; `--example` prints a request to adapt. Read the [command reference](references/command-line.md) before interpreting results. Host output is evidence only within the returned scope.
