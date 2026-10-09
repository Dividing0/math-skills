# Domain playbook: research-time-series-analysis

Read this when selecting a technique, checking a decisive hypothesis, or preparing a mathematical conclusion. The family-level method guide is an orientation aid; the explicit gates below govern this skill. Examples are training material and must not be used as independent evaluation evidence.

## Method branches and applicability

1. For a stationary linear model specify an innovation sequence and its independence or uncorrelatedness assumptions. For centered AR(1) with white-noise innovations of common variance 0<σ²<∞, a causal stationary finite-variance solution requires |φ|<1; derive moments from the infinite moving-average representation. Treat σ²=0 separately: X_t≡0 is stationary and causal for any φ. For |φ|>1 a stationary solution depending on future innovations may exist, but it is not the causal innovation model.
2. For forecasting condition on information available at the prediction origin. Use rolling or expanding temporal splits and refit preprocessing inside each training window. Forecast uncertainty must account for horizon and, when material, parameter estimation rather than merely in-sample residual variance.
3. For stationarity and ergodicity distinguish marginal invariance from learnability by time averages. Trend, seasonal structure or regime shifts require explicit treatment. Residual diagnostics can reveal model failures but absence of sample autocorrelation is not a proof of independence or causality.

## Worked derivation

Let X_t=φX_(t−1)+ε_t, |φ|<1, with independent mean-zero innovations of variance σ² and the causal stationary solution. Then X_t=Σ_(j≥0)φ^j ε_(t−j) in L², so Var X_t=σ²/(1−φ²) and Cov(X_t,X_(t−k))=φ^kσ²/(1−φ²) for k≥0. Conditional on X_t, the one-step mean forecast is φX_t and its innovation error variance is σ² when φ is known.

## Invalid inference and witness

Let X_t=Z for every t where Z is a random Bernoulli(1/2) variable. The process is stationary, but its time average is Z, not the ensemble mean 1/2 almost surely. Thus stationarity alone does not justify replacing expectation by one long-series average.

## Stop and handoff

Return index, horizon, information set, stationarity and validation design. Stop before causal or calibrated-coverage claims when identification or dependence assumptions are absent. Hand off missing sampling dates, exogenous availability and regime information explicitly.
