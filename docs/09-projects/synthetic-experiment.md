# 可运行示例：合成线性回归

这是用于学习科研工作流的**教学实验**，不是新论文复现，也不声称有原创科学结果。所有数据由脚本生成，无须下载数据或使用 GPU。

## 研究问题与预定协议

生成 `y = 2 × x1 − 1.5 × x2 + noise`，比较三种方法的样本外均方误差（MSE 越小越好）：

- **baseline**：只预测训练集 `y` 的均值。
- **消融模型**：使用截距和 `x1` 的线性模型。
- **完整模型**：使用截距、`x1`、`x2` 的线性模型。

固定 5 个种子 `11, 23, 37, 53, 71`；每个种子分别生成 160 个训练样本、80 个测试样本。使用相同的批量梯度下降程序；不使用测试数据选择参数。

## 在仓库根目录运行

```bash
python --version
python -m unittest discover -s tests -v
python examples/synthetic-linear/run.py --out-dir results/synthetic-linear
```

脚本只使用 Python 标准库。输出：

- `runs.csv`：每个种子的三种测试 MSE、训练/测试样本数。
- `summary.json`：多种子均值、样本标准差、固定协议摘要。
- 命令行 JSON 输出：便于在 CI 或终端查看。

代码入口：[examples/synthetic-linear/run.py](https://github.com/RanchoTao/sci-research-wiki/tree/main/examples/synthetic-linear)；配套测试在 `tests/test_synthetic_experiment.py`。默认忽略 `results/`，如需公开科研产物，请单独归档、标注版本与哈希。

## 怎样验收结果

1. 三项单元测试都通过，且脚本生成两个文件。
2. 每个 seed 的三种指标均来自同一 train/test 划分。
3. 检查完整模型平均测试 MSE 是否低于消融模型与均值基线，不能只截取一次。
4. 根据 `runs.csv` 写出一段**明确标注为合成数据**的结果文字。
5. 保留实际运行命令、Python 版本、Git commit 与环境状态。

## 可以进一步做什么

先写下预测，再将生成式中的 `x2` 系数改为 0，观察消融差距；或者增大噪声，观察多种子结果。每次修改须另存配置/版本，不得把探索后的设置冒充原始预定协议。

## 不能得出的结论

这个数据生成机制刻意让第二特征有效，因此结果是机制演示，不代表真实科学问题已经解决；测试集来自相同的人工分布，也不能证明真实世界泛化或原创性。

**下一步**：把这一次实验写成[研究报告](../07-writing/write-a-report.md)与[组会周报](../08-research-life/weekly-research-update.md)。
