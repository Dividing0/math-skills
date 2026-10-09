# Domain playbook

## Select the method

1. For mechanistic validation, check units, conservation, positivity and known limiting regimes before fitting errors. A solvable equation is not evidence that its assumptions describe the intended system.
2. For predictive validation, freeze preprocessing and parameters before using independent observations. Respect group, spatial or temporal dependence; compare an appropriate baseline and specify loss, tolerance and operational domain.
3. For uncertainty-aware validation, separate measurement noise, numerical error, parameter uncertainty and model discrepancy. A confidence or coverage statement requires a defined sampling mechanism and evaluation design; residual magnitudes alone do not identify these components.

## Worked check

Suppose frozen predictions are (2,4,6), independent observations (2.2,3.7,6.1), and the prespecified absolute-error threshold is 0.5. Residuals observation minus prediction are (0.2,-0.3,0.1), all within tolerance; MAE=(0.2+0.3+0.1)/3=0.2. This supports only the three tested conditions, not all operating ranges or a calibrated probabilistic interval.

## Invalid inference and witness

A perfect training fit can give arbitrarily bad extrapolation. On observations at x=0 and x=1, models f(x)=x and g(x)=x+100x(x-1) agree exactly. At x=2 they predict 2 and 202. The shared calibration error cannot decide validity outside the observed range.

## Completion and handoff

Return intended use, validation split and independence, frozen model version, baselines, losses, tolerances, uncertainty components and failed regimes. Stop before a global validity claim if operating ranges or observations are missing. Hand modeling explicit discrepancies and candidate revisions; hand experiment design the untested regimes, while preserving the validation set for future unbiased assessment.

Before reporting success, recheck the selected branch against the exact requested conclusion. Record which premises came from the user and which were derived. A missing premise must remain an explicit obligation, with a concrete description of the additional input or proof needed to continue.

Keep each case’s supplied calibration and validation facts separate. Record a proposed independent dataset or threshold as a next step, never as data already available; do not copy assumptions from another case.
