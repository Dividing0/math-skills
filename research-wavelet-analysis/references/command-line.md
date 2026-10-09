# Command reference

Compute finite orthonormal Haar or discrete Fourier transforms with reconstruction diagnostics.

## Run

From the collection root (or replace the script path with its installed absolute path):

```sh
python research-wavelet-analysis/scripts/signal_transforms.py --example > /tmp/research-wavelet-analysis-input.json
uv run --with numpy python research-wavelet-analysis/scripts/signal_transforms.py --input /tmp/research-wavelet-analysis-input.json
```

Edit the example for the actual task. Use an existing interpreter with the required packages when available; the optional `uv run --with` command provides an isolated dependency environment. Package requirements: numpy. No helper installs dependencies itself. Paths in JSON are interpreted from the command's working directory; prefer absolute paths.

`--input -` reads JSON from stdin. Output is JSON with `status`, `evidence`, `result`, `versions` and `input_sha256`. Exit 0 means the requested calculation completed; inspect mathematical fields such as `valid`, `success`, `is_group` or `checker_success`, which may be false. Invalid input/execution failures exit 1; missing imported packages exit 3. Dependency failures are reported, not simulated.

## Inputs and interpretation

Supply finite real `signal`. `operation: "haar"` requires a power-of-two length, uses the orthonormal pair transform, stores the coarsest coefficient followed by details coarse-to-fine, and applies optional nonnegative hard `threshold`. Returns coefficients, reconstruction, Parseval residual and agreement between discarded energy and squared reconstruction error. `operation: "dft"` uses orthonormal NumPy FFT, optional positive `sample_interval`, complex coefficients encoded [real,imaginary], frequencies and reconstruction diagnostics. These finite transforms imply no continuous wavelet completeness or Fourier inversion theorem.
