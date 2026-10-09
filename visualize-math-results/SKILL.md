---
name: visualize-math-results
description: Create mathematically faithful plots with Matplotlib from actual analytic,
  numerical or statistical data. Use for convergence, errors, trajectories, geometry
  or uncertainty plots with explicit scales, units, sampling and export artifacts.
---

# Visualize Math Results

## Workflow

1. Receive the mathematical quantity, data provenance, units, domain, sampling/discretization, uncertainty meaning and target format. Plot data generated or supplied for this task; do not invent experimental measurements or treat a sketch as computed output.
2. Select plot type and scale matching the quantity. Specify axes and units, coordinate conventions and whether points are interpolated. Logarithmic axes need positive data; explain zero/negative values rather than silently dropping them. Error bars need stated coverage or dispersion meaning.
3. Compute derived plotted quantities explicitly. For convergence studies separate discretization parameter, reference error and timing; show enough samples to support an empirical slope. Break curves at singularities/discontinuities and avoid interpolation across excluded domains.
4. Use a headless backend for file-only runs, object-oriented figures and reproducible styling where useful. Export PNG for preview and SVG/PDF where supported for vector figures; include metadata in a accompanying result record. Close figures after saving.
5. Read [library-playbook.md](references/library-playbook.md); run scripts/example.py --self-test, then use --output for a deliverable. Check actual file creation, shape/finite-value checks and that labels/scales reflect the data. Inspect the rendered figure when judging visual clarity or misleading display.
6. Return figure files, plotted data or generator code, versions, units, sampling and limitations. A plot visualizes evidence; it cannot establish arbitrary-domain positivity, equality, sharpness or convergence alone. Handoff mathematical claims to the relevant proof/numerical/statistical skill.

## Completion

Preserve exact assumptions and distinguish planned code from an actual run. Do not invent solver outputs or dependency availability. Use the user’s language. Read the linked playbook for detailed gates and report which result checks actually ran.

## Runnable helper

Use [plot_data.py](scripts/plot_data.py) to render supplied finite data to a labeled PNG, SVG or PDF using a headless backend. It accepts task-specific JSON through `--input` (or stdin) and prints results, evidence scope, versions and an input hash. `--example` prints a sample request. Read [the command reference](references/command-line.md) for inputs, commands and limitations; inspect the result fields before making mathematical claims.
