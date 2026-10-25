# 实验协议与数据划分

## 为什么需要协议

即使代码能跑、loss 在下降，也可能因为数据泄漏、测试集调参或对照不公平而没有研究价值。**先确定如何比较，再运行实验**。

## 三种数据角色

| 数据 | 用途 | 不该做什么 |
| --- | --- | --- |
| Train | 更新模型参数、拟合预处理器 | 混入未来测试样本 |
| Validation | 选择超参数、调试策略 | 报成未参与开发的最终测试 |
| Test | 在选择完成后做独立评估 | 反复据此调参直到好看 |

一次性固定切分适合入门示例；时间序列、分组样本、患者/用户多条记录等需要按时间或实体隔离。标准化、特征选择、缺失值填充通常应在训练折拟合后应用到其他折。

## 一个合格的 baseline

先试最简单且可解释的办法，比如训练集均值预测。再增加模型复杂度，并保持训练/测试数据、度量、预算可比较。消融试验仅改变一项因素。

**典型协议卡：**

```yaml
question: 第二个特征是否改善样本外 MSE
data: 人工生成，不代表真实世界
train_size: 160
test_size: 80
seeds: [11, 23, 37, 53, 71]
metric: test_mse
comparisons: [train_mean, one_feature, two_features]
tuning_on_test: false
```

同一训练流程多种子运行后，应保留每个种子的原始值、均值与离散程度。不要只展示最优一次；样本量、随机性和置信区间的解释必须与实验设计相符。

## 操作练习

运行[合成实验](../09-projects/synthetic-experiment.md)并回答：

1. 哪些字段在各模型之间相同？
2. 为什么只输出训练损失不能回答研究问题？
3. 如果看了 test 结果后改超参数，应该怎样补充独立评估？
4. 为什么多种子标准差不等于对真实世界分布的普遍保证？

- [scikit-learn：Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html)
- [PyTorch：Datasets & DataLoaders](https://pytorch.org/tutorials/beginner/basics/data_tutorial.html)

**下一步**：[从论文到证据卡](../04-literature/read-a-paper.md)。
