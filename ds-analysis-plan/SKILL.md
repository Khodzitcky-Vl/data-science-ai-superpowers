---
name: ds-analysis-plan
description: Use when a research question spans multiple SQL, pandas, or notebook steps and you need explicit cohorts, windows, metrics, validation checks, outputs, and statistical methods before touching queries or cells
---

# DS Analysis Plan

## Overview

Turn a research question into a reproducible execution plan. The plan should be detailed enough that another analyst can rebuild the notebook, rerun the queries, and reach the same checkpoints.

For notebook projects, the default analytical artifact is a self-contained notebook. Do not assume a notebook should be split into extra `.py` helper modules unless the plan can justify that dependency.

Plans must also specify runtime observability. Do not plan silent long-running loops, chunked jobs, or opaque SQL execution. Default to `tqdm` for loops and chunked work, then add visible stage or status output for SQL and other heavy steps.

**Use after:** `ds-brainstorming` or `ds-experiment-design`

**Next skill after planning:** `ds-subagent-driven-analysis` for same-session execution, `ds-executing-plans` for a separate execution session

If parts of the plan are independent, mark them explicitly for `ds-dispatching-parallel-agents`.

Default evidence comes from notebook reruns, SQL reruns, validation tables, figures, and memos, not from unit-test or `pytest` workflows.

## Plan Header

Every plan should start with:

```markdown
# [Topic] Analysis Plan

**Goal:** one sentence
**Question:** what decision depends on this analysis
**Unit:** randomization and analysis unit
**Window:** pre-period, experiment period, exclusions
**Notebook shape:** self-contained notebook by default; justify any extra module or script dependency
**Methods:** SQL extracts, notebook steps, statistical tests, variance reduction
**Artifacts:** notebook path, query path, output tables, final memo
**Verification mode:** `report-only` | `strict`
```

Default for notebooks: `report-only`. Notebook verification should name the reader-facing output artifact, such as a summary table, manifest, or diagnostic cell, and the explicit pass/fail indicator that will appear there.

## Task Granularity

Use small steps. Each step should produce one observable artifact.

- Define cohorts and exclusions
- Pull baseline data
- Validate row counts and uniqueness
- Build metric table
- Run invariant checks and SRM checks
- Estimate effect with stated method
- Stress-test with slices or robustness checks
- Write conclusion with limitations

## Required Fields Per Task

- Files or notebooks to edit
- Exact query or section to run
- Expected output shape
- Verification artifact: summary table, manifest, diagnostic cell, command output, or other visible output
- Validation check plus pass/fail indicator: column, summary flag, or explicit diagnostic output
- Verification mode: `report-only` or `strict` (default for notebooks: `report-only`)
- Interpretation note: what a pass or fail means
- Readability note: which non-obvious steps require a short code comment or markdown explanation
- Runtime observability note: how progress will be visible while the task runs; default to `tqdm` for loops or chunked work, plus concise stage, timing, status, or row-count output for long SQL and heavy cells
- Packaging note: stay self-contained in the notebook unless an external dependency is explicitly justified
- Parallelization note: `sequential`, `parallel-safe`, or `blocked-by-[task]`

## Runtime Observability

- Any loop or chunked operation that may run long should be planned with `from tqdm.auto import tqdm`
- Long SQL or remote jobs should expose progress through available job state, polling status, elapsed time, stage labels, or visible row-count checkpoints
- Heavy notebook sections should emit concise progress signals that a human can watch, such as stage banners, chunk counters, timing summaries, or diagnostic status cells
- Prefer a few high-signal progress updates over noisy per-row logging

## Method Selection

- CUPED: use when stable pre-period covariate exists
- Linearization: use when ratio metric variance is driven by cluster size
- Cluster-aware inference: use when rows inside the unit are dependent
- Non-parametric or robust summaries: use when tails dominate

## Parallel-Safe Planning

Only mark tasks as parallel-safe when they have:

- Disjoint write scope
- No dependency on unresolved upstream results
- Independent outputs or tables
- No shared notebook state

## Common Mistakes

- Jumping into charts before defining the denominator
- Mixing exploratory slicing with confirmatory conclusions
- Leaving filters implicit inside notebook cells
- Planning a one-off analysis as a notebook plus helper package without a reuse reason
- Writing a plan that says "analyze metric" instead of listing concrete tables and checks
- Treating reproducibility as optional because the notebook already ran once
