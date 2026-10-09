# Domain playbook: research-approximation-theory

Read this when selecting a method, checking a decisive hypothesis, or reporting a completed result.

## Method branches

For uniform approximation in C(K) with compact K, a finite-dimensional linear subspace is closed; a minimizing sequence can be bounded in that subspace, so a best approximation exists. Uniqueness needs a separate property such as a Haar space in the relevant interval setting. For L² approximation onto a closed subspace of a Hilbert space, use orthogonal projection and its norm identity. For interpolation error, require sufficiently many derivatives and distinct nodes before applying a remainder formula. For convergence rates, state the regularity class and constants rather than inferring rates from one smooth target.

## Worked valid example

Approximate f(x)=x by constants on [0,1] in the uniform norm. For a constant c, endpoint errors give ||x-c||∞≥max(|c|,|1-c|)≥1/2, since 1≤|c|+|1-c|. Choosing c=1/2 gives |x-1/2|≤1/2 throughout the interval. Therefore c=1/2 is optimal. Equality in the endpoint requirements forces c=1/2, so this example has a unique best constant approximation.

## Tempting invalid inference

A best approximant need not exist in a nonclosed family. Approximate f=0 on [0,1] by positive constants c>0: the infimum error is zero as c↓0, but no admissible constant attains it. Existence and numerical search are different questions.

## Stop and handoff

Return norm, admissible family, attainment proof and whether uniqueness was established. If a target has insufficient regularity for a quoted rate, fall back to a weaker statement or a counterexample; transfer discrete conditioning and node selection to numerical analysis.

## Application discipline

Begin by rewriting the requested conclusion with its variables, admissible inputs and exact meaning. Choose the branch whose assumptions actually hold; when several branches apply, prefer the one that produces the clearest checkable evidence. Preserve exceptional cases instead of discarding them for convenience. End with the proved result and its scope, then the specific remaining obligation if the task is only partially resolved. The worked example illustrates one branch, rather than establishing a general performance guarantee for this skill.
