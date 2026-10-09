# Domain playbook: research-knot-theory

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For diagram equivalence, use a finite sequence of permitted Reidemeister moves and preserve orientation or framing when required. Ordinary Reidemeister I changes blackboard framing, so framed equivalence is a separate convention.
- For obstruction by invariants, compute them under a fixed normalization and prove invariance for the relevant equivalence. Different invariant values obstruct equivalence; equal values only justify equality of that invariant.
- For Fox colorings, assign residues to arcs and require 2b=a+c at a crossing, where b is the over-arc. Solve the linear system over the specified finite ring or field; do not confuse an arc-coloring count with a complete knot classification.

## Worked valid example

The standard trefoil diagram has three arc colors a,b,c in F₃ with 2a=b+c, 2b=a+c and 2c=a+b. In F₃ these equations all reduce to a+b+c=0. There are 3²=9 solutions, of which 3 are constant, leaving 6 nonconstant colorings. An unknot diagram has one arc and 3 constant colorings. Reidemeister-invariance of the count therefore distinguishes these knots. The invariant argument needs the diagram convention, not just a picture.

## Tempting inference and counterexample

Crossing count in a chosen diagram is not minimal crossing number. A Reidemeister-I curl produces a one-crossing diagram of the unknot, although the unknot has a zero-crossing diagram. Diagram complexity cannot be promoted to a knot invariant without minimization.

## Stop conditions and handoff

Stop a classification claim from a single matching invariant. Hand off diagram encoding, equivalence convention and verified obstruction or explicit move sequence. Reference: J. H. Przytycki, 3-coloring and other elementary invariants of knots, https://arxiv.org/abs/math/0608172, introductory Fox-coloring discussion.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
