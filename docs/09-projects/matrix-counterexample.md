# 完整练习：用精确矩阵反例否定全称命题

本教学案例展示 **错误命题 → 反例 → 修正条件 → 一般证明** 的数学流程。它是经典基础事实，不是独创研究或新反例。

## 命题登记

- 研究对象：同阶实方阵。
- 错误主张：任意 A、B 都有 `(A+B)^2=A^2+2AB+B^2`。
- 否定证据：存在精确整数矩阵使 `AB≠BA`。
- 修正后的条件：在 `AB=BA` 时结论成立（事实上也是必要条件）。
- 已知领域：初等线性代数；原创性：**无**。

## 运行

从仓库根目录：

```bash
python -m unittest discover -s tests -v
python examples/matrix-counterexample/check.py
```

所有矩阵运算在 2×2 整数上精确进行。脚本打印 `A`、`B`、`AB`、`BA`、原等式两边与反例标记。无需 PyTorch、GPU 或网络。

源代码：[examples/matrix-counterexample](https://github.com/RanchoTao/sci-research-wiki/tree/main/examples/matrix-counterexample)。

## 你应该区分的三类证据

1. **精确计算**：这里的明确实例足够推翻原全称命题。
2. **一般性证明**：分配律推导纠正后的恒等式，不能只以脚本通过证明。
3. **原创性检索**：即便发现了真实反例，仍需检查前人是否早已发现；本例明确不是新发现。

## 交付练习

写一页 Markdown：列出原命题及量词、精确反例的两个矩阵、四项展开的代数证明，以及是否存在未核验或未解决的部分。

继续阅读：[数学命题与精确反例](../05-research/mathematical-proof-and-counterexample.md)。
