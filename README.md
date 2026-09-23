<div align="center">
    <a href="https://pypi.python.org/pypi/ChatNote">
        <img src="https://img.shields.io/pypi/v/ChatNote.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatNote/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatNote/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
    <a href="https://arch.gh.wzhecnu.cn/ChatNote/">
        <img src="https://img.shields.io/badge/docs-mkdocs-blue.svg" alt="Documentation" />
    </a>
</div>

<div align="center">

[英文版](README.en.md) | [简体中文](README.md)
</div>

# ChatNote

ChatNote 是 ChatArch 系列的笔记工具 Python 包。当前为标准包骨架，仅提供版本、帮助和命令树入口；尚未实现笔记管理功能。


文档入口：<https://arch.gh.wzhecnu.cn/ChatNote/>

按场景选择文档：

| 场景 | 文档 |
| --- | --- |
| 第一次安装、运行命令行、确认包可用 | [CLI 树](docs/cli-tree.md) |
| 校对当前包有哪些一等能力和边界 | [能力地图](docs/capability-map.md) |
| 从 Python 代码调用包能力 | [接口树](docs/interface-tree.md) |

## 安装与验证

```bash
python -m pip install ChatNote
chatnote --version
chatnote --tree
```

## 从源码开发

在仓库根目录运行：

```bash
pip install -e ".[dev]"
chatnote --help
chatnote --version
chatnote --tree
chatnote --tree-brief
python -m pytest -q
python -m build
```

## 命令行规范

当前包依赖 `chatstyle>=0.2.0,<0.3.0` 和 `chatenv>=0.2.11,<0.3.0`，新增命令应优先使用：

- `add_tree_option()` 提供共享的 `--tree` / `--tree-brief`，`render_click_tree()` 从已注册 Click 元数据生成命令树。
- `CommandSchema` / `CommandField` 描述输入。
- `add_interactive_option()` 提供统一 `-i/-I`。
- `resolve_command_inputs()` 统一缺参补问、默认值、TTY 与校验。
- 当前未定义业务配置，不包含 `config.py` 或 `chatenv.configs` 入口点，也不创建配置文件；后续确有配置需求时再接入 ChatEnv。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first
- `docs/`：长期维护文档，由 mkdocs 构建

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
