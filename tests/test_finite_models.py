"""Exact finite-model checks with analytic answers and failed hypotheses."""

import unittest
from fractions import Fraction

from test_host_helpers import load


class FiniteModels(unittest.TestCase):
    def test_branching_extinction_and_degenerate_critical_case(self):
        tool = load("research-branching-processes", "extinction.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertLessEqual(Fraction(result["extinction_lower"]), Fraction(1, 3))
        self.assertGreaterEqual(Fraction(result["extinction_upper"]), Fraction(1, 3))
        self.assertLessEqual(Fraction(result["interval_width"]), Fraction(1, 2**80))
        for probabilities, extinction in [
            ([0, 1], "0"),
            ([1], "1"),
            (["1/2", 0, "1/2"], "1"),
            ([0, 0, 1], "0"),
        ]:
            with self.subTest(probabilities=probabilities):
                result = tool.compute({"offspring_probabilities": probabilities})
                self.assertEqual(result["extinction_lower"], extinction)
                self.assertEqual(result["extinction_upper"], extinction)
        with self.assertRaises(ValueError):
            tool.compute({"offspring_probabilities": ["1/3", "1/3"]})

    def test_finite_bond_connection(self):
        tool = load("research-percolation-theory", "bond_connection.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(result["connection_probability"], "5/8")
        self.assertEqual(result["configurations_checked"], 8)
        self.assertEqual(
            tool.compute(dict(tool.EXAMPLE, probability=0))["connection_probability"],
            "0",
        )
        self.assertEqual(
            tool.compute(dict(tool.EXAMPLE, probability=1))["connection_probability"],
            "1",
        )
        self.assertEqual(
            tool.compute(dict(tool.EXAMPLE, edges=[], source=0, target=0))[
                "connection_probability"
            ],
            "1",
        )
        self.assertEqual(
            tool.compute(dict(tool.EXAMPLE, edges=[]))["connection_probability"], "0"
        )

    def test_matroid_exchange_and_greedy(self):
        tool = load("research-matroid-theory", "check_matroid.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertTrue(result["is_matroid"])
        self.assertEqual(result["rank"], 2)
        self.assertEqual(result["greedy_weight"], "5")
        self.assertTrue(result["greedy_verified"])
        bad = {"elements": 3, "independent_sets": [[], [0], [1], [2], [0, 1]]}
        self.assertEqual(tool.compute(bad)["failure"], "exchange axiom")
        self.assertEqual(
            tool.compute(dict(tool.EXAMPLE, weights=[-3, -2, -1]))["greedy_weight"], "0"
        )
        self.assertTrue(
            tool.compute({"elements": 0, "independent_sets": [[]]})["is_matroid"]
        )

    def test_mm1_stability_and_little_law(self):
        tool = load("research-queueing-theory", "mm1.py")
        result = tool.compute(tool.EXAMPLE)
        self.assertEqual(
            (result["L"], result["W"], result["population_probability"]),
            ("2", "1", "4/27"),
        )
        self.assertEqual(result["little_law_residual"], "0")
        self.assertFalse(
            tool.compute({"arrival_rate": 3, "service_rate": 3})["stationary"]
        )
        self.assertEqual(
            tool.compute({"arrival_rate": 0, "service_rate": 3})[
                "population_probability"
            ],
            "1",
        )
        with self.assertRaises(ValueError):
            tool.compute({"arrival_rate": 1, "service_rate": 0})


if __name__ == "__main__":
    unittest.main()
