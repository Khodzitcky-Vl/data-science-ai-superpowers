---
name: ds-systematic-debugging
description: Use when notebook outputs, SQL results, experiment metrics, row counts, or sample ratios disagree and duplicate joins, timezone bugs, missing rows, hidden filters, or stale notebook state may explain the mismatch
---

# DS Systematic Debugging

## Overview

Do not patch the notebook until you know where the numbers diverge. Most analysis bugs come from bad joins, silent filters, shifted windows, or mismatched units.

If the mismatch is actually a bad metric definition rather than a pipeline bug, switch to `ds-metric-validation`.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you have not completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY analytical issue:
- Notebook and SQL disagree
- Metrics drift unexpectedly
- SRM or invariant checks fail
- Joins explode row counts
- Windows or timezones look wrong
- Exports, tables, and narrative disagree

**Use this ESPECIALLY when:**
- Under time pressure
- “Just one filter tweak” seems obvious
- You already tried multiple fixes
- Previous fix did not work
- You do not fully understand where the mismatch begins

## The Four Phases

You MUST complete each phase before proceeding to the next.

## The Rule

No fixes before locating the first broken transformation.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. Reproduce the mismatch with exact query, notebook cell, and parameters
2. Lock the comparison point: row count, unique units, date range, metric sum
3. Trace backward from the broken table to the rawest available source
4. Compare working and broken paths one transformation at a time
5. Fix only the first confirmed cause

## What to Compare

- Row counts after every join or filter
- Unique counts by experiment unit
- Timezone, truncation, and inclusive or exclusive window boundaries
- Join cardinality and duplicate explosion
- Null handling and denominator construction
- Event timestamps versus ingestion timestamps

See `root-cause-tracing.md` in this directory for the complete backward tracing technique.

### Phase 2: Pattern Analysis

**Find the pattern before fixing:**

1. Find a working example in the same codebase, warehouse, or notebook family
2. Compare definitions, joins, grouping, and windows line by line
3. Identify every difference, however small
4. Understand dependencies: assignment table, exposure table, cache, helper function, timezone, extract freshness

## High-Value Diagnostics

- Build a tiny sample of affected units and follow them end to end
- Materialize intermediate tables instead of reading chained CTEs mentally
- Compare SQL output and notebook DataFrame shape before aggregations
- Break ratio metrics into numerator and denominator first

See `condition-based-waiting.md` for cases where the issue is caused by waiting on stale extracts, async jobs, or refreshed outputs with arbitrary sleeps.

### Phase 3: Hypothesis and Testing

**Scientific method:**

1. Form a single hypothesis
2. Test the smallest possible change or check
3. If it fails, form a new hypothesis
4. Do not stack fixes

### Phase 4: Implementation

**Fix the root cause, not the symptom:**

1. Add validation or a failing reproduction
2. Implement one fix
3. Rerun the relevant checks
4. If 3+ fixes fail, question the analytical design or data architecture

## Your Human Partner's Signals You Are Doing It Wrong

Watch for these redirects:

- "Will that show where the numbers diverge?" - you proposed a fix before isolating the mismatch
- "Which table first goes wrong?" - you are still at the symptom layer
- "Stop guessing" - you are proposing patches without evidence
- "Rerun it cleanly" - notebook state is contaminating the diagnosis
- "Why did the result change?" - you changed multiple things at once

When you see these: STOP. Return to Phase 1.

## Red Flags

- "The chart looks wrong, let me tweak the filter"
- "Totals are close enough"
- "The notebook cache may be stale" without proving it
- Adding multiple fixes before isolating the source
- "One more tweak" after multiple failed attempts
- Proposing a metric redefinition before proving the pipeline is correct

## Common Failure Modes

- Many-to-many joins hidden inside dimension enrichment
- Time windows defined in local time in one place and UTC in another
- Experiment groups assigned at client level but aggregated at request level
- Notebook cells executed out of order, leaving stale state

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "The mismatch is small, close enough" | Small mismatches often reveal the exact broken step. |
| "I can just tweak the filter" | Filter tweaks without root cause destroy trust in the analysis. |
| "The notebook is messy anyway" | Messy state is a reason to debug more carefully, not less. |
| "I'll fix the narrative first" | The narrative is downstream of the bug. |
| "One more fix attempt" | Multiple failed fixes mean the diagnosis is weak or the design is wrong. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| **1. Root Cause** | Reproduce, lock comparison point, trace back | Know where numbers first diverge |
| **2. Pattern** | Find working reference, compare line by line | Know which difference matters |
| **3. Hypothesis** | Form one theory, test minimally | Confirmed or rejected cleanly |
| **4. Implementation** | Add validation, fix one thing, rerun | Mismatch resolved and reproducible |

## Supporting Techniques

These techniques are part of systematic debugging and available in this directory:

- `root-cause-tracing.md` - trace bugs backward through the SQL or notebook pipeline
- `defense-in-depth.md` - add validation at multiple analytical layers after finding root cause
- `condition-based-waiting.md` - replace arbitrary sleeps with explicit readiness checks
