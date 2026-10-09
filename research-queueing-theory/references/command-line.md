# Command reference

Evaluate exact stationary M/M/1 queue formulas with an explicit stability check.

## Run

From the collection root, or use an installed absolute script path:

```sh
python research-queueing-theory/scripts/mm1.py --example > /tmp/research-queueing-theory-input.json
python research-queueing-theory/scripts/mm1.py --input /tmp/research-queueing-theory-input.json
```

Only the Python standard library is required. Edit the example for the actual task. `--input -` reads stdin. JSON output records `status`, `evidence`, `result`, dependency/Python versions and `input_sha256`. Exit 0 means the calculation completed; inspect `is_matroid`, `stationary` and other result fields before interpreting the result. Invalid input exits 1. Use the `run-math-python` execution runner to bound expensive tasks and retain logs.

## Inputs and interpretation

Supply nonnegative rational `arrival_rate` and positive rational `service_rate` in common inverse-time units. Optional `population` is an integer 0–10000. When rho=arrival/service is below one, return exact L, Lq, W, Wq and the probability of that population, plus a Little-law residual. When rho>=1, return `stationary: false` and no stationary performance values. These formulas assume independent Poisson arrivals, exponential service, one server and an infinite waiting room. At zero arrival rate, W is interpreted for a hypothetical tagged arrival. No inference about empirical arrival/service distributions is made.
