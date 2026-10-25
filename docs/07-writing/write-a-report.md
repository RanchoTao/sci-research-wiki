# 把实验写成可审查的报告

## 目标

报告不是把成功日志翻译成漂亮文字。它要能让读者区分：研究问题、方法、原始事实、解释、局限和下一步。

## 一页实验报告结构

```markdown
# 研究标题
## 问题与背景
要验证的主张；重要的相关工作和精确来源。

## 协议
数据来源/划分、baseline、对照、指标、种子、环境和代码版本。

## 结果
原始结果表位置；聚合方式；失败试验与异常。

## 解释
结果支持哪些主张？替代解释是什么？

## 局限
规模、数据分布、计算预算、尚未执行的独立复核。

## 复现
具体命令、commit、环境和产物位置。

## 下一步
最有信息价值的一项实验或一条理论检查。
```

## 图表自检

每张图应该有明确的横纵轴、单位、图例、数据区间及试验单位。只要有多次实验，说明误差条到底是标准差、标准误还是某个明确构造的置信区间。不要用被挑选的最优 seed 伪装平均性能。

在本文的教学实验里，我们报告多种子测试 MSE 均值与样本标准差；**不能由这些数值直接推导真实数据上的性能**。

## 练习

运行[完整教学实验](../09-projects/synthetic-experiment.md)后，只使用产生的 `runs.csv` 和 `summary.json` 写 150–300 字结果段落；每个数字都应能找到原始来源。

- [Overleaf：Learn LaTeX](https://www.overleaf.com/learn)
- [ACM：Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current)

**下一步**：[每周研究汇报](../08-research-life/weekly-research-update.md)。
