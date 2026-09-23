"""Keep the bootstrap's docs and tag-only publishing contract honest."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_no_provider_is_declared_or_documented_as_implemented():
    assert not (ROOT / "src/chatnote/config.py").exists()
    metadata = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    assert 'entry-points."chatenv.configs"' not in metadata
    zh = (ROOT / "docs/capability-map.md").read_text(encoding="utf-8")
    en = (ROOT / "docs/capability-map.en.md").read_text(encoding="utf-8")
    assert "| ChatEnv 配置提供者 | 未启用 |" in zh
    assert "| ChatEnv provider | Not enabled |" in en


def test_interface_tree_documents_only_current_files():
    for name in ("interface-tree.md", "interface-tree.en.md"):
        text = (ROOT / "docs" / name).read_text(encoding="utf-8")
        assert "__init__.py" in text
        assert "cli.py" in text
        assert "<service>.py" not in text


def test_publish_is_tag_only_with_unconditional_version_guard():
    text = (ROOT / ".github/workflows/publish.yml").read_text(encoding="utf-8")
    assert 'tags:\n      - "v*"' in text
    assert "workflow_dispatch" not in text
    guard = text.split("- name: Verify tag matches package version", 1)[1].split("- name: Check tag commit", 1)[0]
    assert "if:" not in guard
    assert '"${GITHUB_REF_NAME}" != "${RELEASE_TAG}"' in guard
    assert "git fetch --no-tags origin main:refs/remotes/origin/main" in text
    assert "git merge-base --is-ancestor" in text
    assert "id-token: write" in text
    assert "pypa/gh-action-pypi-publish@release/v1" in text
    assert "environment:" not in text
    for secret_marker in ("secrets.PYPI", "TWINE_PASSWORD", "PYPI_API_TOKEN"):
        assert secret_marker not in text
