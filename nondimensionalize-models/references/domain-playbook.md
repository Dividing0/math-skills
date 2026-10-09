# Domain playbook: nondimensionalize-models

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For a balance equation, select positive reference scales for time, states and forcing, substitute into every derivative, and divide by one coefficient with stated units. Carry initial and boundary conditions through the same substitution.
- For dimensional analysis, assemble the exponent matrix of base units and compute its nullspace. A dimensionless group describes possible dependence; it does not prove a constitutive law or uniqueness of the chosen scaling.
- For an asymptotic regime, identify a dimensionless small parameter and the time or space range on which a neglected term stays small. Near initial layers, boundaries or resonances, a globally small coefficient can multiply a large derivative.

## Worked valid example

For m x''+c x'+k x=0 with m,k>0, choose τ=t√(k/m) and x=L X, L>0. Then x'=L√(k/m)X_τ and x''=L(k/m)X_ττ. Division by kL gives X_ττ+γ X_τ+X=0, γ=c/√(mk). An initial velocity v₀ becomes X_τ(0)=v₀√(m/k)/L. γ is dimensionless; changing length units does not alter it.

## Tempting inference and counterexample

Setting ε=0 can destroy an initial condition. In εy'+y=0, y(0)=1 and ε>0, the exact solution is e^(-t/ε). The reduced equation y=0 cannot meet y(0)=1 and only approximates the solution after the initial layer.

## Stop conditions and handoff

Stop if a reference scale is zero or lacks a defined regime. Hand off transformed data, dimensionless groups, layer widths and an error-estimation obligation before declaring a reduced model valid.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
