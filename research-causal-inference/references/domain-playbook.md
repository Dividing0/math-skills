# Domain playbook: research-causal-inference

Read this playbook when selecting a proof technique, choosing a model, or auditing a decisive claim in this specialization. Start with the actual input and the conclusion requested; record any assumptions introduced during the analysis.

## Method branches and hypotheses

- For randomized treatment, identify the intention-to-treat estimand with assignment effects under the specified randomization, consistency and observation assumptions. Noncompliance does not automatically identify the treatment-received effect.
- For back-door adjustment, state a causal DAG, select pre-treatment covariates that block every back-door path, and require positivity and consistency. The adjustment formula identifies an estimand only under those assumptions, not from regression fit alone.
- For instrumental variables, check relevance, exclusion and independence; interpreting a binary-treatment effect as a complier effect additionally requires monotonicity and the associated population definition. These assumptions are substantive, not tests of significance.

## Worked valid example

Suppose binary Z is pre-treatment with P(Z=0)=P(Z=1)=1/2 and sufficient for exchangeability. Conditional mean outcomes are E[Y|T=1,Z=0]=4, E[Y|T=0,Z=0]=1, E[Y|T=1,Z=1]=8 and E[Y|T=0,Z=1]=3, with both treatments possible in both strata. Adjustment gives E[Y(1)-Y(0)]=(4-1)/2+(8-3)/2=4. This is causal only conditional on the stated identification assumptions.

## Tempting inference and counterexample

Perfect prediction does not repair absent overlap. If T=Z deterministically, the cells T=1,Z=0 and T=0,Z=1 are never observed. Their potential outcome means can vary arbitrarily while observed data remain identical, so unrestricted stratum adjustment cannot identify the population effect.

## Stop conditions and handoff

Stop identification when the intervention, population, graph or overlap is undefined. Hand off the exact estimand, observed law, identifying assumptions and nonidentification or sensitivity result before selecting an estimator.

Preserve the distinction between an exact mathematical conclusion and an implementation outcome. A symbolic calculation below can explain what a checker should verify, but does not mean that software was executed. When a required hypothesis is absent, identify the particular step that depends on it and return a conditional result, counterexample, or unresolved obligation. Pass downstream the original statement, domain conventions, the evidence actually obtained, and the remaining question rather than only the proposed answer.
