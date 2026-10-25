"""Exact-arithmetic checks for the elementary matrix example."""
import importlib.util
import unittest
from pathlib import Path

PATH = Path(__file__).resolve().parents[1] / "examples" / "matrix-counterexample" / "check.py"
spec = importlib.util.spec_from_file_location("matrix_example", PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class MatrixCounterexampleTests(unittest.TestCase):
    def test_concrete_counterexample(self):
        lhs, rhs = module.false_identity_sides(module.A, module.B)
        self.assertEqual(lhs, ((1, 0), (0, 1)))
        self.assertEqual(rhs, ((2, 0), (0, 0)))
        self.assertNotEqual(lhs, rhs)

    def test_correct_expansion(self):
        self.assertTrue(module.corrected_identity_holds(module.A, module.B))

    def test_commuting_diagonal_case(self):
        a, b = ((1, 0), (0, 2)), ((3, 0), (0, 4))
        lhs, rhs = module.false_identity_sides(a, b)
        self.assertEqual(lhs, rhs)


if __name__ == "__main__":
    unittest.main()
