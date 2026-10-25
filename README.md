# Sci Research Wiki · 科研基础 Wiki

> 从第一次进入实验室，到独立完成一次有证据、可复现、可交流的科研循环。

面向本科生与科研初学者的开源科研工作流手册。与按课程、软件或编程语言罗列知识点不同，本项目以 **研究问题 → 文献 → 环境与代码 → baseline → 实验与验证 → 结果 → 写作与汇报** 为主线。

## 阅读

- [网页书（GitHub Pages；需仓库 Pages 启用且部署成功）](https://ranchotao.github.io/sci-research-wiki/)
- [学习路线](docs/learning-path.md)
- [可运行教学实验](docs/09-projects/synthetic-experiment.md)
- [建设路线图与验收标准](ROADMAP.md)

## 模块

| 模块 | 首版实际教程 |
| --- | --- |
| 00 开始科研 | [第一次科研循环](docs/00-getting-started/research-loop.md) |
| 01 计算环境 | [Python 环境复现](docs/01-computing/python-environment.md) |
| 02 Git 协作 | [版本化科研实验](docs/02-git/versioned-experiment.md) |
| 03 ML Engineering | [实验协议与数据划分](docs/03-ml-engineering/experiment-protocol.md) |
| 04 Literature | [从论文到证据卡](docs/04-literature/read-a-paper.md) |
| 05 Research | [假设、基线与消融](docs/05-research/hypothesis-and-baselines.md) |
| 06 AI for Research | [核验与证据链](docs/06-ai-for-research/verification-ledger.md) |
| 07 Writing | [实验报告](docs/07-writing/write-a-report.md) |
| 08 Research Life | [每周研究汇报](docs/08-research-life/weekly-research-update.md) |
| 09 Projects | [合成回归端到端实验](docs/09-projects/synthetic-experiment.md) |

历史 `00-...` 到 `09-...` 顶层目录暂时保留作为原始策划档案，不做破坏性迁移；**正式网站内容以 `docs/` 为准**。首版每章一篇实用教程，不代表整个章节已经穷尽。详细待办见 [ROADMAP](ROADMAP.md)。

## 本地运行

Python 3.10+：

```bash
python -m venv .venv
# macOS / Linux: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
mkdocs serve
```

发布前检查：

```bash
python -m unittest discover -s tests -v
mkdocs build --strict
```

完整教学实验只依赖 Python 标准库：

```bash
python examples/synthetic-linear/run.py --out-dir results/synthetic-linear
```

## 网站部署

`.github/workflows/wiki.yml` 对 PR 执行测试和严格构建；合并到 `main` 后尝试 Pages 部署。仓库所有者还需在 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。未检查 Actions 与 Pages 结果前，不应声称网站已经上线。

## 贡献与来源

欢迎修正失效链接、命令、教学案例、页面结构和实验验证。先看 [贡献指南](CONTRIBUTING.md)与[参考致谢](docs/credits.md)。内容不得直接搬运受版权保护的第三方教程、论文 PDF、私有实验数据或泄露个人信息。AI 生成的技术论断须回到原始出处或实际运行核验。

本项目与 [BIMSA MathAI Wiki](https://github.com/RanchoTao/BIMSA-MathAI/) 面向不同需求：后者整理项目课程资源，本项目提供可迁移的科研工作流。
