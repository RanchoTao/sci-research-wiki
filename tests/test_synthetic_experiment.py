"""Tests for the toy research workflow."""
import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "examples" / "synthetic-linear" / "run.py"
spec = importlib.util.spec_from_file_location("synthetic_experiment", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ExperimentTests(unittest.TestCase):
    def test_deterministic_seed(self):
        self.assertEqual(module.run_once(11), module.run_once(11))

    def test_dataset_disjoint_lengths(self):
        train, test = module.make_dataset(11)
        self.assertEqual((len(train), len(test)), (160, 80))

    def test_full_model_beats_ablation_in_synthetic_case(self):
        for seed in module.SEEDS:
            row = module.run_once(seed)
            self.assertLess(row["full_model_mse"], row["ablation_mse"])
            self.assertLess(row["full_model_mse"], row["mean_baseline_mse"])


if __name__ == "__main__":
    unittest.main()
