# Domain playbook: research-queueing-theory

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For an M/M/1 queue require independent Poisson arrivals of rate λ, independent exponential service of rate μ, one server, infinite waiting capacity and the stated discipline. A stationary geometric occupancy distribution exists only for ρ=λ/μ<1.
2. For broader queues use sample-path flow accounting and Little's relation L=λ_eff W under a stable regime with well-defined averages. Specify whether quantities include service, whether λ_eff excludes rejected arrivals and whether the measured population is consistent with its time measure.
3. For M/G/1 mean waiting use the Pollaczek–Khinchine formula only with Poisson arrivals, independent service, FCFS and finite required moments. Mean service alone does not determine mean delay; heavy-tailed service can give finite utilization but infinite expected waiting.

## Worked derivation

For M/M/1 with λ=2 and μ=3, ρ=2/3. Balance gives π_(n+1)=ρπ_n and normalization π_0=1−ρ, so π_n=(1/3)(2/3)^n. The geometric mean occupancy is L=ρ/(1−ρ)=2. Little's relation gives total mean time W=L/λ=1; service takes mean 1/μ=1/3, leaving W_q=2/3 and L_q=4/3.

## Invalid inference and witness

Using M/M/1 delay for every service law with the same mean is false. For M/D/1, λ=1/2 and service time one, the mean queue wait is λE[S²]/(2(1−ρ))=1/2; M/M/1 with μ=1 instead gives W_q=1. Equal utilization does not fix variability.

## Stop and handoff

Return arrival and service laws, effective rates, stability and whether time includes service. Stop before stationary formulas when λ≥μ or observation windows are transient. Transfer tail and moment assumptions explicitly rather than silently replacing distributions.
