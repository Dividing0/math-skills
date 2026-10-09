# Domain playbook: compare-math-theorems

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For the same conclusion C, compare hypothesis classes H_A and H_B by explicit set inclusion. H_B⇒H_A means theorem A applies at least as broadly; record strictness with an admissible object in H_A outside H_B.
2. For different conclusions, build two arrows separately: implication between hypotheses and implication between conclusions under a common domain. Stronger conclusions under stronger assumptions can be useful without dominating the other theorem.
3. For bounds, normalize norms, constants, parameter intervals and asymptotic quantifiers before comparing numbers. A smaller rate with an uncontrolled constant may not improve a finite-range estimate. For purported equivalence provide translations both ways, including exceptional objects.

## Worked derivation

Compare two sufficient conditions for invertibility of a real n×n matrix: A is positive definite, and det A≠0. Positive definiteness implies invertibility because Ax=0 would give xᵀAx=0, contradicting positivity for x≠0. The determinant condition applies more broadly: diag(1,−1) has nonzero determinant but is not positive definite. This is a strict comparison of sufficient hypotheses for the same conclusion, not a claim that positivity itself is weak.

## Invalid inference and witness

“Continuity on [0,1] implies boundedness” and “differentiability on (0,1) implies continuity there” cannot be ranked just by counting assumptions: their domains and conclusions differ. The differentiable function 1/x on (0,1) is unbounded, so silently deleting endpoint assumptions breaks the comparison.

## Stop and handoff

If a theorem is available only as an abstract or paraphrase, mark the affected arrows unchecked. Hand off a table of exact statements, translations, proved inclusions and separating witnesses; do not label a hierarchy on wording alone.
