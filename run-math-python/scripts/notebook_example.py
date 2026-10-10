#!/usr/bin/env python3
"""Execute a notebook through a temporary kernel bound to this interpreter."""

if not __debug__:
    raise RuntimeError(
        "Verification requires Python assertions enabled; do not use -O or PYTHONOPTIMIZE."
    )

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

try:
    import nbformat
    from jupyter_client.kernelspec import KernelSpecManager
    from jupyter_client.manager import KernelManager
    from nbclient import NotebookClient
except ImportError:
    sys.exit("dependency_unavailable: nbformat/nbclient/jupyter-client/ipykernel")


def execute(output=None):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        kernels = root / "kernels"
        folder = kernels / "math-example"
        folder.mkdir(parents=True)
        (folder / "kernel.json").write_text(
            json.dumps(
                {
                    "argv": [
                        sys.executable,
                        "-m",
                        "ipykernel_launcher",
                        "-f",
                        "{connection_file}",
                    ],
                    "display_name": "Temporary mathematical execution",
                    "language": "python",
                }
            ),
            encoding="utf-8",
        )
        specifications = KernelSpecManager(kernel_dirs=[str(kernels)])
        manager = KernelManager(
            kernel_name="math-example",
            kernel_spec_manager=specifications,
            transport="ipc" if os.name == "posix" else "tcp",
            ip=str(root / "kernel") if os.name == "posix" else "127.0.0.1",
        )
        nb = nbformat.v4.new_notebook(
            cells=[
                nbformat.v4.new_code_cell(
                    'import sys,json; print(json.dumps({"executable":sys.executable}))'
                ),
                nbformat.v4.new_code_cell(
                    'import json; print(json.dumps({"value":6*7}))'
                ),
            ]
        )
        client = NotebookClient(
            nb,
            km=manager,
            timeout=20,
            allow_errors=False,
            resources={"metadata": {"path": str(root)}},
        )
        completed = client.execute()
        first = json.loads(completed.cells[0].outputs[0].text)
        last = json.loads(completed.cells[1].outputs[0].text)
        assert Path(first["executable"]).resolve() == Path(
            sys.executable
        ).resolve() and last == {"value": 42}
        assert all(c.execution_count is not None for c in completed.cells)
        if output:
            nbformat.write(completed, output)
        return {
            "status": "pass",
            "value": 42,
            "kernel_executable": first["executable"],
            "classification": "exact_small_integer_computation",
            "checks": [
                "explicit_interpreter_kernel",
                "actual_cell_outputs",
                "execution_counts",
            ],
            "output": str(output) if output else None,
        }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    print(json.dumps(execute(args.output), indent=2))
