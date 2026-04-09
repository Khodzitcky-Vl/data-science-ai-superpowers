from analytics_ai_installer import cli


def test_list_bundles_outputs_names_and_sizes(capsys):
    result = cli.list_bundles()

    captured = capsys.readouterr()

    assert result == 0
    assert "analytics-core" in captured.out
    assert "notebook-research" in captured.out
    assert "all-skills" in captured.out


def test_install_bundle_calls_skilz_for_each_skill(monkeypatch):
    calls = []

    monkeypatch.setattr(cli.shutil, "which", lambda name: "/usr/bin/skilz")

    def fake_run(cmd):
        calls.append(cmd)

        class Result:
            returncode = 0

        return Result()

    monkeypatch.setattr(cli.subprocess, "run", fake_run)

    result = cli.install_bundle(
        bundle="analytics-core",
        agent="codex",
        project=True,
        repo="acme/analytics-ai-skills",
    )

    assert result == 0
    assert calls
    assert calls[0] == [
        "skilz",
        "-y",
        "install",
        "--git",
        "https://github.com/acme/analytics-ai-skills",
        "--skill",
        "ds-using-superpowers",
        "--agent",
        "codex",
        "--project",
    ]


def test_resolve_repo_requires_flag_or_env(monkeypatch):
    monkeypatch.delenv("ANALYTICS_AI_SKILLS_REPO", raising=False)

    try:
        cli.resolve_skills_repo(None)
    except SystemExit as exc:
        assert exc.code == 1
    else:
        raise AssertionError("Expected SystemExit when repo is unset")
