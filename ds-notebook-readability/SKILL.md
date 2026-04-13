---
name: ds-notebook-readability
description: Use when creating, editing, reviewing, or finalizing analytical notebooks whose code, assumptions, transformations, diagnostics, or conclusions need to be understandable to another analyst
---

# DS Notebook Readability

## Overview

Analytical notebooks are handoff artifacts, not only execution logs. A reader should understand why each important step exists, what assumption it encodes, and how to interpret its output without reverse-engineering the code.

Use this skill alongside the normal analysis, reproducibility, and verification skills. It does not replace methodological validation; it makes the methodology readable.

## Core Rule

Comment analytical intent, not syntax.

Add a markdown note, docstring, or short block comment when the reader cannot infer the reason for a choice from names and nearby context. Do not explain obvious pandas, SQL, plotting, or export mechanics.

## When To Add Explanation

Add explanation around any code that answers one of these questions:

- Why is this input, source, window, cohort, threshold, or filter chosen?
- What is the unit, grain, or denominator of the data at this point?
- What assumption makes this transformation valid?
- What edge case is being handled, and why does it matter analytically?
- What would change the interpretation if this check failed?
- Why is this method, model, estimator, or diagnostic appropriate here?
- Which output is authoritative for later conclusions?
- How does this block map intermediate results into a decision, label, status, or recommendation?

If the answer is not already visible in a nearby markdown cell or function name, add a concise explanation.

## Comment Shapes

Use the lightest form that makes the notebook readable:

- Section markdown: 2-5 lines before a major section explaining purpose, inputs, outputs, and interpretation.
- Function docstring: for any helper or ordinary function that encodes
  analytical intent, business rules, metric logic, assumptions, diagnostics,
  status mapping, or decision logic.
- Block comment: 1-4 lines immediately before a non-obvious transformation, check, or decision rule.
- Inline comment: only for a compact edge case that would otherwise be missed.

Prefer one clear block comment before a group of related operations over comments on every line.

## Handoff Pass

Before considering a notebook ready for another analyst, scan:

- code cells longer than about 40 lines
- cells with helper functions
- cells with SQL or remote extracts
- cells with joins, deduplication, filtering, bucketing, imputation, or aggregation
- cells that define metrics, labels, statuses, models, diagnostics, or conclusions
- cells that generate final tables, charts, exports, or narrative text

For each cell, ask:

1. Can a new analyst tell why this cell exists?
2. Can they tell what assumptions or business rules are encoded?
3. Can they tell how to interpret the output?
4. Can they tell which downstream result depends on it?

If any answer is no, add markdown, a docstring, or a block comment.

## What Not To Comment

Do not add comments that only restate syntax:

- `groupby` groups rows
- `merge` joins dataframes
- `display` shows a table
- `to_csv` exports a file
- `plt.tight_layout` adjusts a plot
- variable names that already describe the intent clearly

Avoid tutorial-style explanations unless the notebook is explicitly educational. The audience is an analyst who can read code but should not have to guess the methodology.

## Quality Bar

A readable analytical notebook has:

- explicit section purpose before major blocks
- documented parameters and non-default choices
- visible assumptions near the code that relies on them
- helper docstrings for analytical/business logic
- diagnostics with interpretation, not just output
- final decision rules explained in prose near the implementation
- limitations and diagnostic-only branches marked clearly

## Common Mistakes

- Adding comments after the notebook is finished but only to easy lines.
- Explaining code mechanics while leaving analytical choices implicit.
- Hiding key assumptions inside variable names or hardcoded constants.
- Treating charts and tables as self-explanatory when they drive conclusions.
- Leaving recommendation or status logic as code-only business rules.
