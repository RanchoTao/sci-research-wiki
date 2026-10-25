# 如何使用这本科研手册

本 Wiki 的组织方式是 **研究任务优先、工具按需进入**。不要求从头背完 Git 或 PyTorch 才能开始研究。

## 三条路径

| 你现在的情况 | 从这里开始 | 第一个可验收产出 |
| --- | --- | --- |
| 第一次科研，问题也没定 | [一次科研循环](00-getting-started/research-loop.md) | 1 页问题与交付清单 |
| 已有论文和代码，但复现不了 | [Python 环境](01-computing/python-environment.md) → [实验协议](03-ml-engineering/experiment-protocol.md) | 可重跑的 baseline 与环境记录 |
| 在做原创研究，或依赖 AI 自动化 | [文献证据卡](04-literature/read-a-paper.md) → [研究设计](05-research/hypothesis-and-baselines.md) → [核验记录](06-ai-for-research/verification-ledger.md) | 主张—证据—结论的追踪表 |

## 推荐依赖关系

```text
提出可检验的问题
    ├── 文献检索 / 阅读 ─────┐
    └── 计算环境 / Git ──┐ │
                         ↓ ↓
               baseline 和实验协议
                         ↓
             对照 / 消融 / 误差分析
                         ↓
             可复现的记录和报告
                         ↓
                  同行反馈 / 下一轮
```

AI 可以参与每个节点，但不能替代版本核验、数据检验或独立判断。

## 读完一篇文章的完成标准

1. 可以用自己的话说清楚它解决了哪个真实问题。
2. 按文中步骤完成一个输出，而不只是“看懂”。
3. 保留命令、环境、版本、原始记录和失败信息。
4. 能解释输出证明了什么、**没有证明**什么。
5. 知道下一篇要学什么，也知道什么时候应该停止继续补工具。

第一次练习直接选 [合成回归实验](09-projects/synthetic-experiment.md)：不需要 GPU，也不需要下载数据。
