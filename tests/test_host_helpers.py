"""Behavioral checks for parameterized skill commands and mathematical boundary cases."""

import importlib.util
import json
import math
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True


def load(skill, filename):
    path = ROOT / skill / "scripts" / filename
    spec = importlib.util.spec_from_file_location(skill, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ExactCalculations(unittest.TestCase):
    def test_crt_and_bezout(self):
        tool = load("research-number-theory", "integer_tools.py")
        self.assertEqual(tool.compute(tool.EXAMPLE)["residue"], 14)
        self.assertFalse(
            tool.compute({"operation": "crt", "congruences": [[0, 2], [1, 4]]})[
                "consistent"
            ]
        )
        for a, b in [(0, 0), (-12, 18), (10, -6), (-9, -12)]:
            r = tool.compute({"operation": "bezout", "a": a, "b": b})
            self.assertEqual(a * r["x"] + b * r["y"], math.gcd(a, b))
        with self.assertRaises(ValueError):
            tool.compute({"operation": "crt", "congruences": [[0, 0]]})

    def test_certificate_checks_feasibility_not_only_gap(self):
        tool = load("verify-proof-certificates", "check_certificate.py")
        self.assertTrue(tool.compute(tool.EXAMPLE)["valid"])
        bad = dict(tool.EXAMPLE, x=[0, 0], y=[0])
        self.assertEqual(tool.compute(bad)["gap"], "0")
        self.assertFalse(tool.compute(bad)["valid"])
        self.assertFalse(tool.compute(dict(tool.EXAMPLE, x=[1, 1], y=[1]))["valid"])
        with self.assertRaises(TypeError):
            tool.compute(dict(tool.EXAMPLE, x=[1.0, 0]))
        with self.assertRaises(ValueError):
            tool.compute(dict(tool.EXAMPLE, x=[1]))

    def test_group_and_failed_axiom(self):
        tool = load("research-abstract-algebra", "finite_group.py")
        self.assertEqual(tool.compute(tool.EXAMPLE)["element_orders"], [1, 3, 3])
        self.assertTrue(tool.compute({"table": [[0]]})["is_group"])
        self.assertFalse(tool.compute({"table": [[0, 0], [0, 1]]})["is_group"])
        # S3 multiplication from composition of permutations: nonabelian, center trivial.
        from itertools import permutations

        elements = list(permutations(range(3)))
        table = [
            [elements.index(tuple(a[b[i]] for i in range(3))) for b in elements]
            for a in elements
        ]
        result = tool.compute({"table": table})
        self.assertFalse(result["abelian"])
        self.assertEqual(sorted(map(len, result["conjugacy_classes"])), [1, 2, 3])

    def test_design_pair_counts(self):
        tool = load("research-combinatorial-designs", "check_design.py")
        self.assertTrue(tool.compute(tool.EXAMPLE)["valid"])
        bad = {
            "v": 4,
            "k": 2,
            "lambda": 1,
            "allow_repeated_blocks": True,
            "blocks": [[0, 1], [0, 1], [2, 3], [2, 3]],
        }
        result = tool.compute(bad)
        self.assertEqual(result["point_counts"], [2] * 4)
        self.assertFalse(result["valid"])
        with self.assertRaises(ValueError):
            tool.compute(dict(bad, allow_repeated_blocks=False))

    def test_code_rank_and_zero_code(self):
        tool = load("research-coding-theory", "linear_code.py")
        self.assertEqual(tool.compute(tool.EXAMPLE)["minimum_distance"], 5)
        result = tool.compute({"prime": 2, "generator": [[1, 1, 1], [1, 1, 1]]})
        self.assertEqual((result["dimension"], result["minimum_distance"]), (1, 3))
        self.assertIsNone(
            tool.compute({"prime": 2, "generator": [[0, 0]]})["minimum_distance"]
        )
        with self.assertRaises(ValueError):
            tool.compute({"prime": 4, "generator": [[1, 1]]})

    def test_homology_filled_and_unfilled(self):
        tool = load("research-algebraic-topology", "simplicial_homology.py")
        for prime in (2, 3, 5):
            self.assertEqual(
                tool.compute(dict(tool.EXAMPLE, prime=prime))["betti"], [1, 1]
            )
            self.assertEqual(
                tool.compute({"prime": prime, "simplices": [[0, 1, 2]]})["betti"],
                [1, 0, 0],
            )
            sphere = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
            self.assertEqual(
                tool.compute({"prime": prime, "simplices": sphere})["betti"], [1, 0, 1]
            )
        self.assertEqual(tool.compute({"simplices": [[0], [1]]})["betti"], [2])
        with self.assertRaises(ValueError):
            tool.compute({"prime": 4, "simplices": [[0, 1]]})

    def test_finite_topology_boundary(self):
        tool = load("research-general-topology", "finite_topology.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(result["closure"], [0, 1])
        self.assertTrue(result["T0"])
        self.assertFalse(result["Hausdorff"])
        self.assertFalse(
            tool.compute({"points": 3, "opens": [[], [0], [1], [0, 1, 2]]})[
                "is_topology"
            ]
        )
        empty = tool.compute({"points": 0, "opens": [[]], "subset": []})
        self.assertEqual(empty["closure"], [])
        self.assertTrue(empty["Hausdorff"])

    def test_truth_table_countermodel(self):
        tool = load("research-mathematical-logic", "truth_table.py")
        self.assertTrue(tool.compute(tool.EXAMPLE)["valid"])
        result = tool.compute({"formula": ["implies", ["or", "P", "Q"], "P"]})
        self.assertEqual(result["countermodel"], {"P": False, "Q": True})
        self.assertEqual(result["satisfying_valuations"], 3)
        self.assertFalse(tool.compute({"formula": False})["satisfiable"])
        with self.assertRaises(ValueError):
            tool.compute({"formula": ["forall", "P"]})

    def test_exact_geometry(self):
        tool = load("research-computational-geometry", "planar_geometry.py")
        self.assertEqual(tool.compute(tool.EXAMPLE)["area"], "1")
        narrow = {
            "operation": "orientation",
            "points": [[0, 0], [1, 1], [2, "2.00000000000000000000001"]],
        }
        self.assertEqual(tool.compute(narrow)["orientation"], 1)
        result = tool.compute(
            {"operation": "convex-hull", "points": [[0, 0], [1, 1], [2, 2], [1, 1]]}
        )
        self.assertEqual(result["area"], "0")
        self.assertEqual(len(result["hull"]), 2)

    def test_finite_dependence(self):
        tool = load("research-probability-theory", "finite_probability.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(result["covariance"], "0")
        self.assertFalse(result["independent"])
        independent = {
            "outcomes": [{"x": x, "y": y, "p": "1/4"} for x in (0, 1) for y in (0, 1)]
        }
        result = tool.compute(independent)
        self.assertTrue(result["independent"])
        self.assertAlmostEqual(result["mutual_information_bits"], 0)
        with self.assertRaises(ValueError):
            tool.compute({"outcomes": [{"x": 0, "y": 0, "p": "1/2"}]})

    def test_game_deviations(self):
        tool = load("research-game-theory", "check_game.py")
        self.assertTrue(tool.compute(tool.EXAMPLE)["mixed_equilibrium"])
        self.assertFalse(
            tool.compute(dict(tool.EXAMPLE, row_strategy=[1, 0]))["mixed_equilibrium"]
        )
        prisoner = {"row_payoffs": [[3, 0], [5, 1]], "column_payoffs": [[3, 5], [0, 1]]}
        self.assertEqual(tool.compute(prisoner)["pure_equilibria"], [[1, 1]])


class SymbolicCalculations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tool = load("compute-with-sympy", "calculate.py")

    def test_domains_and_parser(self):
        self.assertEqual(self.tool.compute(self.tool.EXAMPLE)["value"], "EmptySet")
        self.assertEqual(
            self.tool.compute({"operation": "simplify", "expression": "sqrt(x**2)"})[
                "value"
            ],
            "Abs(x)",
        )
        self.assertEqual(
            self.tool.compute(
                {"operation": "factor", "symbols": {}, "expression": "0.1+0.2"}
            )["value"],
            "3/10",
        )
        for expression in [
            '__import__("os").system("true")',
            "x.__class__",
            "1/0",
            "0**(-1)",
        ]:
            with self.subTest(expression=expression), self.assertRaises(ValueError):
                self.tool.compute({"operation": "simplify", "expression": expression})

    def test_solver_honors_declared_assumptions(self):
        result = self.tool.compute(
            {
                "operation": "solve",
                "symbols": {"x": {"positive": True}},
                "expression": "x**2-1",
            }
        )
        self.assertEqual(result["value"], "{1}")
        result = self.tool.compute(
            {
                "operation": "solve",
                "symbols": {"x": {"integer": True}},
                "expression": "2*x-1",
            }
        )
        self.assertEqual(result["value"], "EmptySet")
        result = self.tool.compute(
            {
                "operation": "solve",
                "symbols": {"x": {"real": False}},
                "domain": "complex",
                "expression": "x**2+1",
            }
        )
        self.assertEqual(result["value"], "{-I, I}")

    def test_calculus(self):
        self.assertEqual(
            self.tool.compute({"operation": "differentiate", "expression": "sin(x)"})[
                "value"
            ],
            "cos(x)",
        )
        self.assertEqual(
            self.tool.compute({"operation": "integrate", "expression": "2*x"})[
                "derivative_residual"
            ],
            "0",
        )
        self.assertIn(
            "O(x**4)",
            self.tool.compute(
                {"operation": "series", "expression": "exp(x)", "order": 4}
            )["value"],
        )
        self.assertEqual(
            self.tool.compute(
                {"operation": "residue", "expression": "1/x", "point": 0}
            )["value"],
            "1",
        )

    def test_linear_algebra_and_ideal(self):
        result = self.tool.compute(
            {
                "operation": "matrix",
                "symbols": {},
                "matrix": [[1, 2], [2, 4]],
                "rhs": [1, 2],
            }
        )
        self.assertEqual(result["rank"], 1)
        self.assertEqual(result["nullspace_residuals"], [[["0"], ["0"]]])
        result = self.tool.compute(
            {
                "operation": "groebner",
                "symbols": {"x": {}, "y": {}},
                "variables": ["x", "y"],
                "polynomials": ["x*y-1", "y**2-1"],
                "query": "x**2-1",
            }
        )
        self.assertTrue(result["member"])
        self.assertEqual(result["reconstruction_residual"], "0")

    def test_dynamics_and_metric(self):
        result = self.tool.compute(
            {
                "operation": "dynamics",
                "symbols": {"x": {"real": True}, "y": {"real": True}},
                "variables": ["x", "y"],
                "field": ["y", "-x"],
                "point": [0, 0],
                "invariant": "x**2+y**2",
            }
        )
        self.assertTrue(result["formal_invariant"])
        self.assertTrue(result["equilibrium_verified"])
        sphere = self.tool.compute(
            {
                "operation": "metric",
                "symbols": {"theta": {"real": True}, "phi": {"real": True}},
                "coordinates": ["theta", "phi"],
                "metric": [[1, 0], [0, "sin(theta)**2"]],
            }
        )
        self.assertEqual(sphere["scalar_curvature"], "2")
        flat = self.tool.compute(
            {
                "operation": "metric",
                "symbols": {"x": {"real": True}},
                "coordinates": ["x"],
                "metric": [[4]],
            }
        )
        self.assertEqual(flat["scalar_curvature"], "0")

    def test_stationarity_not_mixing(self):
        tool = load("research-stochastic-processes", "markov_chain.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(result["stationary_distribution"], ["1/2", "1/2"])
        self.assertEqual(result["distribution_after_steps"], ["0", "1"])
        self.assertFalse(tool.compute({"transition": [[1, 0], [0, 1]]})["unique"])
        with self.assertRaises(ValueError):
            tool.compute({"transition": [["1/2", 0], [0, 1]]})

    def test_dimensionless_groups(self):
        tool = load("nondimensionalize-models", "dimensionless_groups.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(
            result["groups"][0]["exponents"], {"length": -1, "time": 1, "speed": 1}
        )
        self.assertEqual(result["groups"][0]["dimension_residual"], ["0", "0"])
        self.assertEqual(
            tool.compute({"quantities": ["x"], "dimensions": [[0]]})[
                "independent_groups"
            ],
            1,
        )


class NumericalCalculations(unittest.TestCase):
    def test_matrix_residual_and_regularization(self):
        tool = load("compute-with-numpy", "analyze.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertLess(result["stationarity_norm_2"], 1e-12)
        result = tool.compute(
            {"operation": "least-squares", "matrix": [[1, 1]], "rhs": [2]}
        )
        self.assertFalse(result["unique_unregularized_solution"])
        self.assertAlmostEqual(result["solution"][0], 1)
        result = tool.compute(
            {
                "operation": "tikhonov",
                "matrix": [[1, 0], [0, 1]],
                "rhs": [2, 4],
                "regularization": 1,
            }
        )
        self.assertAlmostEqual(result["solution"][0], 1)
        self.assertAlmostEqual(result["solution"][1], 2)
        self.assertLess(result["stationarity_norm_2"], 1e-12)

    def test_stability_boundary_and_covariance(self):
        tool = load("compute-with-numpy", "analyze.py")
        for value, label in [
            (-1, "asymptotically-stable"),
            (0, "boundary-or-numerically-unresolved"),
            (1, "unstable"),
        ]:
            self.assertEqual(
                tool.compute({"operation": "stability", "matrix": [[value]]})[
                    "classification"
                ],
                label,
            )
        self.assertEqual(
            tool.compute(
                {"operation": "stability", "matrix": [[-1]], "timebase": "discrete"}
            )["classification"],
            "boundary-or-numerically-unresolved",
        )
        self.assertEqual(
            tool.compute(
                {
                    "operation": "propagate-covariance",
                    "matrix": [[2]],
                    "covariance": [[3]],
                }
            )["output_covariance"],
            [[12]],
        )
        with self.assertRaises(ValueError):
            tool.compute(
                {
                    "operation": "propagate-covariance",
                    "matrix": [[1]],
                    "covariance": [[-1]],
                }
            )

    def test_ode_and_lp(self):
        tool = load("compute-with-scipy", "numerical.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertTrue(result["success"])
        self.assertAlmostEqual(result["states"][-1][0], math.exp(-2), places=8)
        result = tool.compute(
            {
                "operation": "linear-program",
                "c": [1, 1],
                "A_ub": [[-1, -1]],
                "b_ub": [-1],
            }
        )
        self.assertTrue(result["success"])
        self.assertAlmostEqual(result["objective"], 1)
        result = tool.compute(
            {
                "operation": "linear-program",
                "c": [1],
                "A_ub": [[1], [-1]],
                "b_ub": [0, -1],
            }
        )
        self.assertFalse(result["success"])
        self.assertNotIn("solution", result)
        result = tool.compute(
            {
                "operation": "transport",
                "cost": [[0, 1], [1, 0]],
                "source": [0.5, 0.5],
                "target": [0.25, 0.75],
            }
        )
        self.assertAlmostEqual(result["objective"], 0.25)
        self.assertLess(result["max_equality_residual"], 1e-12)

    def test_graph_paths_and_flow(self):
        tool = load("analyze-graphs-with-networkx", "graph_report.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(result["distance"], 5)
        self.assertEqual(result["recomputed_cost"], 5)
        self.assertEqual(
            tool.compute(dict(tool.EXAMPLE, target="isolated"))["path_status"],
            "unreachable",
        )
        edges = [
            {"source": "s", "target": "a", "weight": -2},
            {"source": "a", "target": "t", "weight": 1},
        ]
        self.assertEqual(tool.compute(dict(tool.EXAMPLE, edges=edges))["distance"], -1)
        result = tool.compute(dict(tool.EXAMPLE, operation="max-flow"))
        self.assertEqual(result["flow_value"], 2)
        self.assertEqual(result["max_conservation_residual"], 0)
        with self.assertRaises(ValueError):
            tool.compute(dict(tool.EXAMPLE, edges=tool.EXAMPLE["edges"] * 2))

    def test_ols_matches_centered_formula(self):
        tool = load("analyze-data-with-statsmodels", "fit_ols.py")
        result = tool.compute(tool.EXAMPLE)
        xs = [row[0] for row in tool.EXAMPLE["design"]]
        ys = tool.EXAMPLE["response"]
        xb, yb = sum(xs) / len(xs), sum(ys) / len(ys)
        slope = sum((x - xb) * (y - yb) for x, y in zip(xs, ys)) / sum(
            (x - xb) ** 2 for x in xs
        )
        self.assertAlmostEqual(result["coefficients"][1], slope)
        self.assertAlmostEqual(result["coefficients"][0], yb - slope * xb)
        with self.assertRaises(ValueError):
            tool.compute(dict(tool.EXAMPLE, design=[[1]] * len(ys)))

    def test_transforms_and_refinement(self):
        tool = load("research-wavelet-analysis", "signal_transforms.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertAlmostEqual(result["squared_error"], 2)
        self.assertAlmostEqual(result["discarded_energy"], 2)
        for op in ("haar", "dft"):
            result = tool.compute({"operation": op, "signal": [1, -2, 3, 7]})
            self.assertLess(abs(result["parseval_residual"]), 1e-12)
        with self.assertRaises(ValueError):
            tool.compute({"operation": "haar", "signal": [1, 2, 3]})
        refinement = load("research-numerical-analysis", "refinement.py")
        self.assertEqual(
            refinement.compute(refinement.EXAMPLE)["observed_orders"], [2, 2]
        )
        with self.assertRaises(ValueError):
            refinement.compute({"steps": [1, 0.5], "errors": [1, 0]})

    def test_plot_deliverable_and_log_guard(self):
        tool = load("visualize-math-results", "plot_data.py")
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "figure.png"
            tool.compute(dict(tool.EXAMPLE, output=str(output)))
            self.assertTrue(output.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))
            self.assertGreater(output.stat().st_size, 1000)
            with self.assertRaises(ValueError):
                tool.compute(
                    dict(tool.EXAMPLE, output=str(output), y=[1, 0, 1], yscale="log")
                )


class WorkflowTools(unittest.TestCase):
    def test_ledger_cycle_and_observation(self):
        tool = load("manage-math-research", "dependencies.py")
        self.assertEqual(
            tool.compute(tool.EXAMPLE)["unsupported_proved_claims"][0]["id"], "theorem"
        )
        result = tool.compute(
            {
                "claims": [
                    {"id": "a", "status": "proved", "depends_on": ["b"]},
                    {"id": "b", "status": "proved", "depends_on": ["a"]},
                ]
            }
        )
        self.assertFalse(result["acyclic"])
        result = tool.compute(
            {
                "claims": [
                    {"id": "a", "status": "observation"},
                    {"id": "b", "status": "proved", "depends_on": ["a"]},
                ]
            }
        )
        self.assertEqual(result["unsupported_proved_claims"][0]["id"], "b")

    def test_dataset_leakage_and_missing_scores(self):
        tool = load("build-math-evaluation-sets", "audit_dataset.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(result["duplicate_prompt_ids"], [["a", "b"]])
        self.assertEqual(result["families_crossing_splits"], {"p": ["test", "train"]})
        self.assertEqual(result["missing_score_ids"], ["a"])
        with self.assertRaises(ValueError):
            tool.compute(dict(tool.EXAMPLE, scores=[{"id": "unknown", "score": 1}]))

    def test_host_inventory_and_source_search(self):
        tool = load("run-math-python", "host_capabilities.py")
        result = tool.compute(
            {
                "packages": ["package-that-does-not-exist-387"],
                "executables": ["tool-that-does-not-exist-387"],
            }
        )
        self.assertIsNone(result["packages"]["package-that-does-not-exist-387"])
        self.assertIsNone(result["executables"]["tool-that-does-not-exist-387"])
        search = load("search-mathlib", "search_local.py")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Main.lean").write_text(
                "theorem one : True := True.intro\ntheorem two : True := True.intro\n"
            )
            result = search.compute(
                {"project": directory, "query": "theorem", "limit": 1}
            )
            self.assertTrue(result["truncated"])
            self.assertEqual(result["matches"][0]["line"], 1)

    @unittest.skipUnless(
        shutil.which("lake") and shutil.which("elan"), "Lake/Elan is unavailable"
    )
    def test_actual_lean_checker(self):
        tool = load("audit-lean4-proofs", "check_project.py")
        # Use an already installed toolchain; never provision a toolchain in tests.
        listing = subprocess.run(
            ["elan", "toolchain", "list"], text=True, capture_output=True, check=True
        )
        pins = [
            line.split()[0]
            for line in listing.stdout.splitlines()
            if line.startswith("leanprover/lean4:")
        ]
        if not pins:
            self.skipTest("No Lean 4 toolchain installed")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "lean-toolchain").write_text(pins[0] + "\n")
            (root / "lakefile.toml").write_text(
                'name = "helper_tests"\n[[lean_lib]]\nname = "Main"\n'
            )
            (root / "Main.lean").write_text(
                "theorem clean : True := True.intro\ntheorem admitted : False := by sorry\n"
            )
            subprocess.run(
                ["lake", "build", "Main"],
                cwd=root,
                capture_output=True,
                text=True,
                check=True,
                timeout=60,
            )
            result = tool.compute(
                {
                    "project": directory,
                    "modules": ["Main"],
                    "theorems": ["clean", "admitted"],
                }
            )
            self.assertTrue(result["checker_success"])
            self.assertTrue(result["sorry_marker_detected"])
            self.assertIn("sorryAx", result["checks"][0]["stdout"])
            (root / "Bad.lean").write_text("example : False := by exact True.intro\n")
            self.assertFalse(
                tool.compute({"project": directory, "files": ["Bad.lean"]})[
                    "checker_success"
                ]
            )
            self.assertEqual(list(root.glob("SkillAudit*")), [])

    def test_cli_json_errors_and_missing_dependencies(self):
        path = ROOT / "research-number-theory/scripts/integer_tools.py"
        result = subprocess.run(
            [sys.executable, str(path)],
            input='{"operation":"bezout","a":12,"b":18}',
            text=True,
            capture_output=True,
            check=True,
        )
        payload = json.loads(result.stdout)
        self.assertEqual(payload["result"]["gcd"], 6)
        self.assertEqual(len(payload["input_sha256"]), 64)
        for source in ("[]", '{"a": NaN}', "not json"):
            result = subprocess.run(
                [sys.executable, str(path)],
                input=source,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(json.loads(result.stdout)["status"], "failed")
        symbolic = ROOT / "compute-with-sympy/scripts/calculate.py"
        result = subprocess.run(
            [sys.executable, "-S", str(symbolic)],
            input='{"operation":"simplify","expression":"x"}',
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 3)
        self.assertEqual(json.loads(result.stdout)["status"], "dependency_missing")


if __name__ == "__main__":
    unittest.main()
