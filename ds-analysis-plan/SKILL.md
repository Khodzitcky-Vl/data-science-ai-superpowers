---
name: ds-analysis-plan
description: Use when a research question spans multiple SQL, pandas, or notebook steps and you need explicit cohorts, windows, metrics, validation checks, outputs, and statistical methods before touching queries or cells
---

# DS Analysis Plan

## Overview

Turn a research question into a reproducible execution plan. The plan should be detailed enough that another analyst can rebuild the notebook, rerun the queries, and reach the same checkpoints.

For notebook projects, the default analytical artifact is a self-contained notebook. Do not assume a notebook should be split into extra `.py` helper modules unless the plan can justify that dependency.

Plans must also specify runtime observability. Do not plan silent long-running loops, chunked jobs, or opaque SQL execution. Progress output must be compact in saved notebooks: use `tqdm` only when it will update in place, avoid nested high-frequency bars, and use coarse stage/timing/row-count checkpoints when a progress bar would spam the output.

**Use after:** `ds-brainstorming` or `ds-experiment-design`

**Next skill after planning:** `ds-subagent-driven-analysis` for same-session execution, `ds-executing-plans` for a separate execution session

If parts of the plan are independent, mark them explicitly for `ds-dispatching-parallel-agents`.

Default evidence comes from notebook reruns, SQL reruns, validation tables, figures, and memos, not from unit-test or `pytest` workflows.

Use the shared validation budget from `ds-using-superpowers`. Planning should protect the analytical decision without turning validation into the main body of the notebook.

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
**Validation level:** `light` | `standard` | `strict`
**Verification mode:** `report-only` | `strict`
```

Default for notebooks: `report-only`. Notebook verification should name the reader-facing output artifact, such as a summary table, manifest, or diagnostic cell, and the explicit pass/fail indicator that will appear there.

Default validation level:

- `light` for exploratory or first-pass analysis
- `standard` for normal decision-support analysis
- `strict` only for final publication, decision-ready claims, disputed results, failed core checks, debugging, or review blockers

## Task Granularity

Use small steps. Each step should produce one observable artifact.

- Define cohorts and exclusions
- Pull baseline data
- Add compact extraction diagnostics: row counts, unit counts, date range
- Build metric table
- Run required balance, SRM, or invariant diagnostics when the design needs them
- Estimate effect with stated method
- Stress-test with only the slices or robustness checks that protect the decision
- Write conclusion with limitations

Do not create a standalone validation task when the check can be a short diagnostic output inside the main analytical task.

## Required Fields Per Task

- Files or notebooks to edit
- Exact query or section to run
- Expected output shape
- Validation level: `light`, `standard`, or `strict`
- Minimum diagnostic artifact: summary table, manifest, diagnostic cell, command output, or other visible output
- Escalation triggers: what would require deeper validation or stopping the plan
- Verification mode: `report-only` or `strict` (default for notebooks: `report-only`)
- Interpretation note: what a pass or fail means
- Readability note: which non-obvious steps require a short code comment or markdown explanation
- Runtime observability note: how progress will be visible while the task runs and how saved notebook output will stay compact; prefer one visible outer progress signal plus concise stage, timing, status, or row-count output for long SQL and heavy cells
- Packaging note: stay self-contained in the notebook unless an external dependency is explicitly justified
- Parallelization note: `sequential`, `parallel-safe`, or `blocked-by-[task]`
- Visualization note: which specific charts this section must produce, or `table-only: [reason]`
- Narrative note: what the markdown cell immediately preceding this section must explain — the WHY (methodological justification), not only the WHAT

## Runtime Observability

- Any loop or chunked operation that may run long needs visible progress, but `tqdm` is not automatic. In notebooks, use at most one active progress bar per cell unless you have verified nested bars render cleanly.
- Long SQL or remote jobs should expose progress through available job state, polling status, elapsed time, stage labels, or visible row-count checkpoints
- Heavy notebook sections should emit concise progress signals that a human can watch, such as stage banners, chunk counters, timing summaries, or diagnostic status cells
- Prefer a few high-signal progress updates over noisy per-row logging
- For large inner loops, avoid `tqdm(inner_iterable)` when the notebook may save every refresh. Prefer batching, `mininterval`, `miniters`, `leave=False`, or manual checkpoints such as every 5%, 10%, or completed outer group.

## Method Selection

- CUPED: use when stable pre-period covariate exists
- Linearization: use when ratio metric variance is driven by cluster size
- Cluster-aware inference: use when rows inside the unit are dependent
- Non-parametric or robust summaries: use when tails dominate

## When a Visualization Is Required

Add a chart by default when any of these conditions apply:

- Two or more groups, cohorts, or segments are compared (cohort comparison, A/B split, partner groups, etc.)
- A metric distribution or spread is shown (histogram, ECDF, boxplot of any metric: success rate, revenue, retention, request volume)
- There is a time dimension (trend, dynamics, retention curve, daily counts)
- A result includes uncertainty (p-value, confidence interval, effect size)
- The output table contains 5+ rows of aggregated data that can be compared visually
- An assumption is being checked (linearity, normality, balance, SRM, covariate correlation)

`table-only` is acceptable only with an explicit reason (e.g. "single scalar output", "already visualized in [section name]").

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
