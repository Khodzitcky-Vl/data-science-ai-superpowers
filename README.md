# Analytics AI Skills

Repository with analytics-focused `ds-*` skills and a thin installer CLI for `Skilz`.

## What Is Here

- Root-level `ds-*` directories are installable skills.
- `analytics-ai-installer` installs named bundles in one command.
- `templates/` contains starter `AGENTS.md` and `CLAUDE.md` snippets.
- `2026-04-09-analytics-ai-installer-implementation.md` captures the original implementation plan.

## Repository Layout

```text
.
├── ds-*/                      # installable skills
├── src/analytics_ai_installer/  # bundle installer package
├── templates/                # starter agent instructions
├── tests/                    # installer CLI tests
├── pyproject.toml
└── README.md
```

## Prerequisites

- Python 3.12+
- `skilz`

Install `skilz`:

```bash
pip install skilz
```

## Install From Published Repository

List bundles directly from the published repository:

```bash
uvx --from git+ssh://git@github.com/your-org/analytics-ai-skills.git \
  analytics-ai-installer list-bundles
```

## Bundle Installs

Install the recommended Codex bundle:

```bash
uvx --from git+ssh://git@github.com/your-org/analytics-ai-skills.git \
  analytics-ai-installer install analytics-core --agent codex --repo your-org/analytics-ai-skills
```

Install the recommended Claude Code bundle:

```bash
uvx --from git+ssh://git@github.com/your-org/analytics-ai-skills.git \
  analytics-ai-installer install analytics-core --agent claude --repo your-org/analytics-ai-skills
```

Install every shipped skill into project scope:

```bash
uvx --from git+ssh://git@github.com/your-org/analytics-ai-skills.git \
  analytics-ai-installer install all-skills --agent codex --project --repo your-org/analytics-ai-skills
```

## Single Skill Install

```bash
skilz install your-org/analytics-ai-skills/ds-analysis-plan --agent codex
```

## Available Bundles

### `analytics-core`

Baseline skills for everyday analytics work.

### `notebook-research`

Extended bundle for notebook-heavy research and analysis review.

### `ab-experimentation`

Bundle for experiment design, metric validation, and parallel execution.

### `all-skills`

Installs every analytics skill shipped in this repository.

## Local Development

Install the package in editable mode:

```bash
python -m pip install -e .
```

List bundles from the checkout:

```bash
analytics-ai-installer list-bundles
```

Run tests:

```bash
pytest -q
```

## Templates

### `templates/AGENTS.analytics.md`

Starter guidance for projects that use these analytics skills as their default workflow layer.

### `templates/CLAUDE.analytics.md`

Starter instructions for Claude-oriented analytics projects using this skill set.

## Troubleshooting

### `skilz` is not found

Install it first:

```bash
pip install skilz
```

### Installer says `--repo` is required

Pass the Git repository explicitly:

```bash
analytics-ai-installer install analytics-core --agent codex --repo your-org/analytics-ai-skills
```

Or set:

```bash
export ANALYTICS_AI_SKILLS_REPO=your-org/analytics-ai-skills
```

## Verification

Expected smoke checks:

```bash
pytest tests/test_analytics_ai_installer.py -q
analytics-ai-installer list-bundles
```
