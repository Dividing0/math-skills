# Library playbook

## Primary documentation

Retrieved/checked 2026-10-08. Recheck documentation against installed versions before adapting API calls.

- https://python-control.readthedocs.io/en/latest/generated/control.feedback.html
- https://python-control.readthedocs.io/en/latest/generated/control.step_response.html
- https://python-control.readthedocs.io/en/latest/generated/control.lqr.html

The workflow names the relevant API locators; use the actual installed signatures and recorded version, especially for release/development discrepancies.

## Worked calculation

Negative unity feedback around G=1/(s+1) gives T=1/(s+2), with unit-step output (1-exp(-2t))/2. Independently verify continuous poles and step response; also simulate x[k+1]=0.5x[k]+u[k] with dt=0.1 against its recurrence.

Execute `../scripts/example.py --self-test`. The script emits JSON and fails its assertions if the independent oracle disagrees. An unavailable dependency emits a dependency-unavailable status and exits 2; that is not a passed numerical check. Assertions run in ordinary Python, so do not launch with `-O`.

## False inference

All transfer-function poles after cancellation are stable, therefore every internal state is stable. An unobservable unstable mode can be hidden.

## Integration contract

Receive a precise mathematical statement, assumptions, units, dimensions, data provenance, desired error/accuracy, available interpreter and runtime constraints from the mathematical skill. Return the exact implementation, dependency versions, executed inputs, raw outcomes, failure/status information, and independent checks. Keep numerical tolerance separate from mathematical guarantees. If an assumption or dependency is missing, return the missing item and any valid partial analysis rather than a fabricated computed result.

## Scope and escalation

Hand back to research-control-theory, develop-control-state-estimation, analyze-math-stability, research-optimal-control when the issue concerns mathematical assumptions or justification rather than an API. Prefer the smaller supported calculation to an unvalidated large model. Preserve input data and task-local outputs; avoid modifying environments or external services without the task's authorization.

## API locators and conventions

- Feedback reference: `control.feedback(sys1, sys2=1, sign=-1)`; explicitly set sign. LQR reference: `control.lqr(A,B,Q,R)` returns K,S,E and uses u=-Kx; use `control.dlqr` for a known discrete state model.
- Step reference: `control.step_response(..., timepts=...)` returns `TimeResponseData`; inspect `.time` and `.outputs` instead of relying on implicit tuple squeezing.
- For continuous G=1/(s+1), negative unity feedback gives G/(1+G)=1/(s+2), poles -2 and step response (1-exp(-2t))/2. For discrete A=.5,B=C=1,D=0, the independent recurrence gives y[k]=2*(1-.5**k).
- Example execution checked python-control 0.10.2. Retrieved latest documentation describes an additional development revision; match installed signatures on adaptation.
