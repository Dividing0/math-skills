# Domain playbook: research-noncommutative-algebra

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For multiplication identities, expand in the actual order of factors. Commutator terms measure the failure of commutative simplifications; scalar coefficients may commute even when algebra elements do not.
- For quotient algebras, verify a two-sided ideal so products of representatives are well-defined. A left ideal supports a left-module quotient, which is a weaker construction.
- For module decompositions or structure theorems, specify the base field, dimension and semisimplicity assumptions. A matrix algebra can be simple as an algebra without every element being invertible; simplicity concerns ideals, not units.

## Worked valid example

In M₂(Q), set A=E₁₂ and B=E₂₁. Then A²=B²=0, AB=E₁₁ and BA=E₂₂. Expanding gives (A+B)²=AB+BA=I. The commutator [A,B]=E₁₁-E₂₂ is nonzero. This concrete example separates ring operations, nilpotence of individual elements and the behavior of their sum without relying on a commutative binomial rule.

## Tempting inference and counterexample

A nonzero element in a simple algebra need not be a unit. M₂(Q) is simple, but E₁₁ is singular and cannot have an inverse, since E₁₁E₂₂=0 with E₂₂≠0. Algebra simplicity does not make the algebra a division ring.

## Stop conditions and handoff

Stop a transferred commutative theorem until multiplication order, side conventions and structural assumptions are checked. Hand off exact relations, ideal type and module action; for localization retain the separate denominator and compatibility obligations.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
