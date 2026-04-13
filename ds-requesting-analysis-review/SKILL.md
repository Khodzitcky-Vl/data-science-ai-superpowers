---
name: ds-requesting-analysis-review
description: Use when an experiment analysis, metric study, notebook investigation, or methodology proposal is close to decision-ready and you need an independent check of design, statistics, interpretation, and reproducibility
---

# Requesting Analysis Review

## Overview

Ask for review before the conclusion hardens into a decision. The reviewer should challenge methodology, not just style.

Request review before publishing, socializing, or escalating a result. After review, use `ds-receiving-analysis-review` to process feedback rigorously.

Dispatch an analysis-reviewer subagent to catch methodological errors before they become business decisions.

**Core principle:** Review the work that can change decisions. Do not turn light exploratory tasks into review-heavy process by default.

## When to Request Review

**Mandatory:**
- After `standard` or `strict` tasks in `ds-subagent-driven-analysis` that affect final conclusions
- After completing a major experiment or validation study
- Before publishing a final conclusion or recommendation

**Optional but valuable:**
- When stuck on interpretation
- Before redesigning a metric
- After fixing a complex analytical bug
- After a `light` task if a risk signal appears: unit mismatch, denominator drift, SRM, invariant failure, stale cache, leakage risk, or narrative/output disagreement

## Review Package

Provide:

- Research question and business decision
- Hypothesis and experiment unit
- Metric definitions and final formulas
- Data window and exclusions
- Validation level and compact diagnostic evidence
- Notebook, SQL, and exported result tables
- Summary of assumptions, limitations, and open questions

## Ask the Reviewer to Check

- Randomization and analysis unit alignment
- Sample ratio mismatch and invariant metrics
- Statistical method choice
- Sensitivity to outliers, tails, and segment mix
- Interpretation of confidence intervals and practical significance
- Reproducibility appropriate to the validation level; final results require strict evidence

## How to Request

**1. Gather the review package**
- `{WHAT_WAS_ANALYZED}` - what was produced
- `{PLAN_OR_REQUIREMENTS}` - plan section, design doc, or task requirements
- `{DESCRIPTION}` - brief summary of the result
- `{NOTEBOOK_PATH}` - notebook or script path
- `{QUERY_REFERENCE}` - SQL path or query reference
- `{ARTIFACT_REFERENCE}` - output tables, figures, exports

**2. Dispatch analysis-reviewer subagent**

Use the template at `analysis-reviewer.md`

**3. Act on feedback**
- Fix Critical issues immediately
- Fix Important issues before moving on
- Note Minor issues for later
- Push back if the reviewer is wrong, with evidence

## Good Moments to Request Review

- After experiment design, before data pull
- After metric validation, before the final effect estimate
- After the full notebook is rerun, before publishing conclusions

## Common Mistakes

- Asking for review with only screenshots
- Requesting feedback after already socializing the result as final
- Hiding known limitations instead of surfacing them explicitly

See template at: `ds-requesting-analysis-review/analysis-reviewer.md`
