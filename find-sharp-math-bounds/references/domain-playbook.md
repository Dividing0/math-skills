# Domain playbook: find-sharp-math-bounds

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For a homogeneous inequality, normalize a nonzero scale first and minimize or maximize over the normalized admissible class. Check the zero case separately and retain dimensional dependence in the original variables.
- For equality-based sharpness, prove the universal inequality and exhibit an admissible equality case. Equality equations must satisfy all original constraints, not just one intermediate inequality.
- For unattained constants, construct an admissible sequence and compute its limiting ratio. A supremum need not be a maximum; distinguish a best constant from existence of an extremizer.

## Worked valid example

For real a,b, (a-b)²≥0 implies 2ab≤a²+b². Therefore (a+b)²=a²+2ab+b²≤2(a²+b²). Equality holds exactly when a=b. Taking a=b=1 gives ratio (a+b)²/(a²+b²)=2, so any smaller universal coefficient fails. The zero vector causes no difficulty because both sides vanish; sharpness uses a nonzero witness.

## Tempting inference and counterexample

A sharp bound may not be attained. For x∈(0,1), x<1 and sup x=1 because x_n=1-1/n (n≥2) approaches 1, but no admissible x equals 1. Calling x=1 an extremizer changes the admissible domain.

## Stop conditions and handoff

Stop a claim of optimality until a matching witness or sequence is proved. Hand off normalization, equality conditions, compactness questions and any gap between lower and upper constants to optimization or proof construction.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
