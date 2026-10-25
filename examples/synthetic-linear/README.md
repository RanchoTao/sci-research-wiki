# Synthetic Linear Experiment

一个不依赖第三方包的可重复科研流程教学案例。所有数据人为生成，不构成真实世界发现。

从仓库根目录运行：

```bash
python -m unittest discover -s tests -v
python examples/synthetic-linear/run.py --out-dir results/synthetic-linear
```

固定 5 个种子；每个种子用 160 个训练样本拟合并在 80 个独立测试样本上比较 mean baseline、单特征消融和双特征模型。

`runs.csv` 保留每个种子的原始测试指标，`summary.json` 保留均值和样本标准差。结果目录被 Git 忽略，正式归档时需保存代码 commit、运行命令和环境信息。

详见 [教学章节](../../docs/09-projects/synthetic-experiment.md)。
