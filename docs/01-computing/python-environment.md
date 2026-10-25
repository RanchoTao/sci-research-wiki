# Python 环境复现

## 目标

在 Windows、macOS 或 Linux 上创建互不干扰的环境；让别人能根据你的记录重建一次运行。

## 最小可用教程

先确保已安装 Python 3.10 或更新版本。下面的命令在项目根目录执行：

```bash
python --version
python -m venv .venv
```

macOS / Linux（bash/zsh）：

```bash
source .venv/bin/activate
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
```

激活后统一使用 `python -m pip`，这样可以减少 pip 和 Python 指向不同解释器的风险：

```bash
python -m pip --version
python -m pip install -r requirements.txt
python -m pip list
```

`requirements.txt` 应在项目仓库中；真正需要严格复现的实验还应记录精确版本/锁文件、Python 版本及系统/设备信息。不建议在多个项目间复用一个全局环境。

## 科研场景：别人能否重跑？

给实验保留最少这些字段：代码 commit、Python 版本、依赖与关键硬件/驱动版本、启动命令、配置、数据来源与校验值、输出位置。对于 GPU 训练还需记录 PyTorch 对应的 CUDA build 和驱动；**驱动、CUDA Toolkit、PyTorch CUDA runtime 不是同一个东西**。

## 高频错误

| 症状 | 优先检查 |
| --- | --- |
| `ModuleNotFoundError` | `python -m pip --version` 是否对应当前解释器 |
| PowerShell 拒绝激活脚本 | 检查执行策略；也可直接运行 `.venv\Scripts\python.exe`，避免全局修改安全策略 |
| 另一台机器跑不动 | Python/包版本、平台 wheel、GPU 环境和数据路径 |
| `pip install` 成功但 IDE 报错 | 编辑器是否选择了项目的 `.venv` 解释器 |

## 练习与资料

用全新目录复现自己的一个脚本，保存 `python --version` 和 `python -m pip list` 输出；不要提交 `.venv/`。

- [Python 官方 venv 文档](https://docs.python.org/3/library/venv.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/)

**下一步**：[Git 版本化实验](../02-git/versioned-experiment.md)。
