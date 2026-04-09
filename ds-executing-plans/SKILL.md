---
name: ds-executing-plans
description: Use when you already have a written analysis plan and want to execute SQL, notebook, or validation tasks in a separate session with review checkpoints and rerun-based evidence between batches
---

# DS Executing Plans

## Overview

Load the analysis plan, challenge it, then execute in small batches with review checkpoints. Each batch should end with reproducible artifacts, not just changed notebook cells.

When the artifact is a notebook project, prefer improving the notebook in place. Do not create new helper modules by default unless the plan explicitly justifies them.

In notebooks, verification should be reader-facing first: emit summary tables, manifests, or diagnostic cells with explicit pass/fail columns. Avoid scattered fail-fast exceptions. If strict enforcement is needed, put it in one final optional validation cell.

Execution should preserve runtime observability from the plan. Do not let long loops, chunked transforms, or SQL steps run silently; default to `tqdm` for iterable work and add visible status or timing output for heavier steps.

**Core principle:** Batch execution with checkpoints for methodological review.

**Announce at start:** "I'm using the ds-executing-plans skill to execute this analysis plan."

**Use after:** `ds-analysis-plan`

**Use instead of:** `ds-subagent-driven-analysis` when you want a separate execution session and explicit pauses for human review

If a batch contains several tasks already marked `parallel-safe`, use `ds-dispatching-parallel-agents` for those tasks and merge the evidence before reporting back.

## The Process

### Step 1: Load and Review Plan
1. Read the full plan file
2. Review critically for methodological gaps
3. Raise concerns before starting if needed
4. If no concerns: create tasks and proceed

### Step 2: Execute Batch
**Default: First 3 tasks**

For each task:
1. Mark as in progress
2. Follow each step exactly
3. Run the verification specified in the plan
4. Mark as completed

### Step 3: Report
When batch complete:
- Show what ran
- Show artifacts and verification evidence
- Say: "Ready for feedback."

### Step 4: Continue
Based on feedback:
- Apply changes if needed
- Execute next batch
- Repeat until complete

When a batch has mixed task types:

- Keep dependency-heavy tasks sequential
- Dispatch only the explicitly independent tasks in parallel
- Rejoin on verification, not on agent self-report

### Step 5: Complete Analysis

After all tasks complete:
- Request an independent review with `ds-requesting-analysis-review`
- Then use `ds-verification-before-completion` before any final claim

## Batch Output

Each checkpoint should include:

- What queries or notebook sections ran
- What tables or plots were produced
- What validation checks passed or failed
- What changed in the current interpretation
- For notebook work, visible verification artifacts such as summary tables, manifests, or diagnostic cells instead of interleaved fail-fast exceptions
- What runtime progress signals were added or observed for long-running SQL, loops, or heavy notebook sections

## Runtime Observability

- Default to `from tqdm.auto import tqdm` for loops, chunked pandas work, batch API calls, and other iterable execution
- For SQL or remote jobs, show whatever the system can expose: query label, stage label, elapsed time, polling status, job id, chunk count, or row-count checkpoints
- If the tool has no native progress API, add concise stage-start and stage-finish messages with timings instead of leaving a blank cell or silent terminal wait
- Keep progress output human-readable; avoid log spam that hides failures

## Stop and Ask For Help

- The plan assumes a dataset or metric that does not exist
- Sample ratio mismatch or invariant failure appears
- Results contradict the design assumptions
- The notebook cannot be rerun cleanly

## When to Revisit Earlier Steps

Return to Step 1 when:
- The plan is updated
- A metric definition changes
- A core design assumption fails

Do not force through blockers.

## Remember

- Review plan critically first
- Follow plan steps exactly
- Do not skip verifications
- Use `ds-dispatching-parallel-agents` only for explicitly independent tasks
- Between batches: report and wait
- Stop when blocked, do not guess
- Keep one-off analytical logic inside the notebook unless an external module was explicitly justified in the plan
- Use notebook reruns, SQL reruns, validation checks, and artifact inspection as verification evidence
- Add minimal comments only where the analytical intent is not obvious from the code itself
- Prefer one short comment or markdown explanation before a non-obvious block over line-by-line narration
- Comment non-obvious filters, exclusions, joins or dedup logic, metric definitions, variance-reduction blocks, and validation cells
- In notebooks, default verification to reader-facing outputs; use one final optional strict-validation block only when hard enforcement is truly needed
- Do not introduce unit-test or `pytest` workflow unless the task explicitly becomes software engineering
- No special git-worktree procedure is required for this DS workflow
- Treat runtime observability as part of execution quality, not as optional polish
- Do not leave heavy loops or long SQL without visible progress; use `tqdm` by default and add status, timing, or row-count signals where `tqdm` does not apply

## Common Mistakes

- Continuing after a methodological red flag because the plan said to move on
- Reporting "analysis complete" without rerun evidence
- Hiding interpretation changes between batches
- Splitting a single notebook task into notebook code plus ad hoc helper modules without a reuse reason

## Integration

**Required workflow skills:**
- `ds-analysis-plan` - creates the plan this skill executes
- `ds-requesting-analysis-review` - review after execution
- `ds-verification-before-completion` - verify final analytical claims

**Optional workflow skill:**
- `ds-dispatching-parallel-agents` - parallelize only plan-marked independent tasks
