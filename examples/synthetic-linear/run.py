"""Reproducible toy experiment. No external packages or real-world dataset."""
import argparse
import csv
import json
import random
import statistics
from pathlib import Path

SEEDS = (11, 23, 37, 53, 71)


def make_dataset(seed, n_train=160, n_test=80):
    rng = random.Random(seed)
    rows = []
    for _ in range(n_train + n_test):
        x1, x2 = rng.gauss(0, 1), rng.gauss(0, 1)
        y = 2.0 * x1 - 1.5 * x2 + rng.gauss(0, 0.3)
        rows.append((x1, x2, y))
    return rows[:n_train], rows[n_train:]


def fit(train, feature_count, steps=1200, lr=0.08):
    weights = [0.0] * (feature_count + 1)
    for _ in range(steps):
        gradients = [0.0] * len(weights)
        for x1, x2, y in train:
            xs = [1.0, x1, x2][:feature_count + 1]
            residual = sum(w * x for w, x in zip(weights, xs)) - y
            for j, x in enumerate(xs):
                gradients[j] += 2.0 * residual * x / len(train)
        weights = [w - lr * g for w, g in zip(weights, gradients)]
    return weights


def mse(test, predictor):
    return sum((predictor(x1, x2) - y) ** 2 for x1, x2, y in test) / len(test)


def run_once(seed):
    train, test = make_dataset(seed)
    mean_train = statistics.mean(y for _, _, y in train)
    full = fit(train, feature_count=2)
    ablation = fit(train, feature_count=1)
    return {
        "seed": seed,
        "n_train": len(train),
        "n_test": len(test),
        "mean_baseline_mse": mse(test, lambda x1, x2: mean_train),
        "full_model_mse": mse(test, lambda x1, x2: full[0] + full[1] * x1 + full[2] * x2),
        "ablation_mse": mse(test, lambda x1, x2: ablation[0] + ablation[1] * x1),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default="results", help="Where to write receipts")
    args = parser.parse_args()
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    rows = [run_once(seed) for seed in SEEDS]
    with (out / "runs.csv").open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    metrics = ("mean_baseline_mse", "full_model_mse", "ablation_mse")
    summary = {
        "dataset": "synthetic linear model; no external data",
        "protocol": "fixed seed; disjoint train/test; no test-set tuning",
        "seeds": list(SEEDS),
        "mean_test_mse": {k: statistics.mean(row[k] for row in rows) for k in metrics},
        "sample_std_test_mse": {k: statistics.stdev(row[k] for row in rows) for k in metrics},
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
