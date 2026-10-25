# 版本化科研实验

## 为什么研究项目一定要有版本控制

一个结论必须能回答：“这张图是哪一版代码、哪一份配置、哪些数据产生的？”Git 管代码历史，**不自动解决数据版本或大文件存储**。

## 最小工作流

在已经获得 Git 仓库访问权限的前提下：

```bash
git clone https://github.com/RanchoTao/sci-research-wiki.git
cd sci-research-wiki
git status
git switch -c docs/my-first-improvement
# 修改一个文档或脚本
git add docs/
git commit -m "docs: improve research tutorial"
git push -u origin docs/my-first-improvement
```

到 GitHub 创建 Pull Request，让修改经过 review，再合并。初学者不要在尚未理解历史时使用 `push --force`、`reset --hard` 或批量重写提交。

## 将实验与代码版本绑定

在运行实验时记录：

```bash
git rev-parse HEAD
git status --short
python --version
```

如果工作区非空，提交实验代码与配置，或额外归档 diff。单有 commit SHA 但实验在未提交修改上运行，仍然不可完整追溯。

建议实验回执目录包含 `config.json`、`runs.csv`、`summary.json`、`README.md`，并记录输入数据的版本或哈希。大量实验输出应存到专门的对象存储/归档，而不是不加选择地 push 到 Git。

## 练习

复现实验一次，并在本地记录当前 commit、`git status` 及执行命令；随后更改实验参数，新建分支，比较两个版本的原始指标而不是只比较截图。

- [Pro Git（免费在线书）](https://git-scm.com/book/en/v2)
- [GitHub：Pull Request 简介](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)

**下一步**：[机器学习实验协议](../03-ml-engineering/experiment-protocol.md)。
