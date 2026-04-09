# Analytics AI Installer Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a Skilz-based installer CLI in this repository, copy the analytics skills into installable root-level directories, and initialize the workspace as a git repository.

**Architecture:** Keep each analytics skill as a root-level installable directory for Skilz, and add a lightweight Python CLI under `src/analytics_ai_installer` that installs named bundles by invoking `skilz install` repeatedly. Add concise docs and templates so the repository can be published directly as the canonical skills source.

**Tech Stack:** Python 3.12, argparse, subprocess, pytest, Skilz

---

### Task 1: Add failing tests for the installer CLI

**Files:**
- Create: `tests/test_analytics_ai_installer.py`

**Step 1:** Write tests for bundle listing and batch install command construction.

**Step 2:** Run `pytest tests/test_analytics_ai_installer.py -q` and confirm failure because the installer package does not exist yet.

### Task 2: Create the installer package and metadata

**Files:**
- Create: `pyproject.toml`
- Create: `README.md`
- Create: `src/analytics_ai_installer/__init__.py`
- Create: `src/analytics_ai_installer/bundles.py`
- Create: `src/analytics_ai_installer/cli.py`

**Step 1:** Implement the minimal CLI required by the tests.

**Step 2:** Run the targeted pytest command until it passes.

### Task 3: Add repository docs and templates

**Files:**
- Create: `docs/quickstart.md`
- Create: `docs/installation.md`
- Create: `docs/bundles.md`
- Create: `docs/troubleshooting.md`
- Create: `templates/AGENTS.analytics.md`
- Create: `templates/CLAUDE.analytics.md`

**Step 1:** Document one-command bundle installs and single-skill installs.

### Task 4: Copy analytics skills into the repository root

**Files:**
- Create: root-level `ds-*` skill directories copied from `/Users/vladimirkhodzitskii/Desktop/Code/data-science-ai-superpowers/skills`

**Step 1:** Copy each skill directory without editing its contents.

**Step 2:** Verify all expected `SKILL.md` files exist at the repository root.

### Task 5: Clean git hygiene and initialize the repository

**Files:**
- Modify: `.gitignore`

**Step 1:** Ignore local assistant state and caches that should not be committed.

**Step 2:** Run tests, initialize git, add files, and create the initial commit.
