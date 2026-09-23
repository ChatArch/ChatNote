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

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatNote

ChatNote is a ChatArch Python package for note tooling. It currently provides only the standard package skeleton with version, help, and CLI tree entry points; note management is not implemented.


Documentation entry: <https://arch.gh.wzhecnu.cn/ChatNote/en/>

Choose documentation by scenario:

| Scenario | Document |
| --- | --- |
| Install the package, run the CLI, and confirm it works | `docs/cli-tree.en.md` |
| Check first-class capabilities and current boundaries | `docs/capability-map.en.md` |
| Call package behavior directly from Python | `docs/interface-tree.md` |

## Install and Verify

```bash
python -m pip install ChatNote
chatnote --version
chatnote --tree
```

## Develop from Source

Run from the repository root:

```bash
pip install -e ".[dev]"
chatnote --help
chatnote --version
chatnote --tree
chatnote --tree-brief
python -m pytest -q
python -m build
```

## CLI Contract

This package depends on `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.11,<0.3.0`. New commands should prefer:

- `add_tree_option()` for shared `--tree` / `--tree-brief` flags and `render_click_tree()` to render registered Click metadata.
- `CommandSchema` / `CommandField` for inputs.
- `add_interactive_option()` for the shared `-i/-I` switch.
- `resolve_command_inputs()` for missing args, defaults, TTY behavior, and validation.
- No business configuration is defined, so this package does not include `config.py`, register a `chatenv.configs` entry point, or create configuration files. Add a ChatEnv provider only when configuration is needed.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first
- `docs/`: long-lived project docs built by mkdocs

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
