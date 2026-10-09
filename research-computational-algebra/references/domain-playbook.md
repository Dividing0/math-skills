# Domain playbook: research-computational-algebra

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For ideal membership over a field, fix a monomial order and obtain a verified Gröbner basis before interpreting division remainders. Division by arbitrary generators can leave a nonzero remainder for an ideal member.
- For elimination, use an elimination order and interpret the eliminated ideal as algebraic constraints on projected solutions. Projection can omit points in its algebraic closure, especially over non-algebraically-closed fields or after inequations.
- For rational-coefficient reconstruction or factorization, verify candidate identities exactly. Modular computations need good-prime and reconstruction arguments; specialization can drop degree or change multiplicities.

## Worked valid example

In Q[x,y] with lex order x>y, let g₁=x-y and g₂=y²-1. Their S-polynomial is y²g₁-xg₂=x-y³; reducing by g₁ yields y-y³ and then by g₂ yields 0. Thus the pair is a Gröbner basis. For h=x²-1, the exact identity h=(x+y)(x-y)+(y²-1) establishes ideal membership independently of the division algorithm.

## Tempting inference and counterexample

Specialization need not preserve algebraic structure. The polynomial ax+1 has degree one for a≠0 but becomes the nonzero constant 1 at a=0 and has no root. A solver dividing by a must retain the branch a=0 rather than announce x=-1/a for every parameter.

## Stop conditions and handoff

Stop when coefficient domain, order or excluded denominators is unspecified. Hand off exact identities, exceptional parameter branches, basis verification obligations and the distinction between variety membership and ideal membership.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
