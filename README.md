# 科研基础 Wiki | Sci Research Wiki

面向本科生与科研初学者的科研基础知识库。

目标不是把 Linux、PyTorch、Git、论文写作分别做成彼此孤立的教程，而是回答一个更实际的问题：

> **一个人从第一次进入实验室，到能够独立完成一次科研循环，中间到底需要会什么？**

本仓库目前处于 **框架搭建阶段**。内容会逐步补全，也欢迎通过 Issue / Pull Request 共同维护。

---

## 科研路线图

```text
第一次做科研
    ↓
计算环境
Linux → SSH → Python 环境 → VS Code → Git
    ↓
跑实验
Data → PyTorch → Train → Eval → Debug
    ↓
进入研究
读论文 → 找论文 → Related Work → 找问题
    ↓
验证问题
Hypothesis → Baseline → Experiment → Statistics
    ↓
形成成果
Figures → Paper → GitHub → Presentation
    ↓
完整科研循环
```

---

## 目录

### 00. Getting Started
- [科研学习路线](00-getting-started/README.md)
- 第一次科研项目应该怎么开始
- 如何使用本 Wiki

### 01. Computing
- [计算环境与服务器](01-computing/README.md)
- Linux / SSH / 文件传输 / 后台任务
- Conda / venv / pip / requirements
- CUDA / PyTorch 版本
- VS Code Remote SSH
- Docker
- Slurm / 集群

### 02. Git
- [Git 与科研协作](02-git/README.md)
- clone / commit / push / pull
- branch / merge / PR
- 冲突处理与多人协作

### 03. ML Engineering
- [机器学习实验与科研工程](03-ml-engineering/README.md)
- PyTorch
- NumPy / Pandas
- Jupyter
- Debug
- 实验流程
- 绘图
- Hugging Face

### 04. Literature
- [论文阅读与文献管理](04-literature/README.md)
- 如何读论文
- 如何找论文
- Scholar / arXiv / Semantic Scholar
- Zotero
- Related Work

### 05. Research
- [科研方法与实验设计](05-research/README.md)
- 如何找到科研问题
- 如何判断 idea 是否值得做
- baseline / ablation / control
- reproducibility
- statistics / metrics

### 06. AI for Research
- [AI 辅助科研](06-ai-for-research/README.md)
- ChatGPT / Codex / Claude Code
- AI 辅助编程
- AI 辅助读论文与实验
- 幻觉、验证与证据链

### 07. Writing
- [科研写作与表达](07-writing/README.md)
- 论文写作
- 图表与结果叙事
- LaTeX
- README
- 审稿标准

### 08. Research Life
- [科研协作与组会](08-research-life/README.md)
- 如何向导师汇报
- 如何参加组会
- 科研汇报 / PPT

### 09. Projects
- [完整科研循环实战](09-projects/README.md)
- 找论文 → clone → 配环境 → 跑实验 → 改代码 → 出图 → 写作 → GitHub

---

## 这个 Wiki 的原则

1. **以科研流程为主线，而不是以软件功能为主线。**
2. **优先解决真实科研中高频遇到的问题。**
3. **理论解释服务于实际操作。**
4. **代码、实验和结论尽量可复现。**
5. **AI 可以参与科研流程，但关键事实必须回到论文、代码、日志和实验结果验证。**
6. **先给出最小可用方法，再逐步进入进阶内容。**

---

## 推荐阅读方式

如果你刚开始科研，建议按以下顺序：

```text
00 Getting Started
→ 01 Computing
→ 02 Git
→ 03 ML Engineering
→ 04 Literature
→ 05 Research
→ 06 AI for Research
→ 07 Writing
→ 08 Research Life
→ 09 Projects
```

已有一定经验的读者可以直接按问题检索对应章节。

---

## 当前状态

- [x] 仓库与目录结构
- [x] 基础章节框架
- [ ] 第一批基础教程
- [ ] 完整科研循环示例
- [ ] 视频课程
- [ ] 静态文档站 / 搜索

---

## Contributing

欢迎提交 Issue、纠错和 Pull Request。

贡献前请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

> 本项目首先服务于“第一次真正开始做科研的人”。如果一篇文章不能帮助读者更快完成下一步科研动作，它就还不够好。
