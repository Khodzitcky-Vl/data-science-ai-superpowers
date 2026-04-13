# DS Root Cause Tracing

## Overview

Analytical bugs often appear at the end of the pipeline: wrong lift, broken ratio, impossible confidence interval, or a chart that does not match the table. Fixing the final aggregation is usually symptom treatment.

**Core principle:** Trace backward through the SQL, notebook, and metric pipeline until you find the first transformation where the result becomes wrong.

## When to Use

- Final metric is wrong but raw data may still be correct
- The mismatch appears after a long CTE chain or notebook pipeline
- Unit counts, denominators, or windows drift somewhere mid-pipeline
- You need to locate which join, filter, or grouping introduced the error

## The Tracing Process

### 1. Observe the Symptom
```
Notebook says treatment lift = +4.2%
Warehouse table says treatment lift = -0.8%
```

### 2. Find Immediate Cause
**Which final computation directly creates the mismatch?**
- Ratio calculation?
- Winsorization step?
- Join to experiment assignment?
- Daily aggregation before cluster-level rollup?

### 3. Ask: What Produced This Input?
- Which upstream table fed the ratio?
- Which CTE or DataFrame created the denominator?
- Which assignment or exposure mapping was joined in?

### 4. Keep Tracing Up
At each step compare:
- Row counts
- Unique units
- Date windows
- Numerator and denominator sums
- Null rates

### 5. Find Original Trigger
Typical sources:
- Wrong join cardinality
- Hidden filter
- UTC vs local-day window mismatch
- Assignment table keyed at client level but aggregated at request level
- Post-treatment denominator definition

## Instrumentation Pattern

When you cannot trace mentally, materialize checkpoints:

```sql
select
  dt,
  count(*) as rows,
  count(distinct client_id) as clients,
  sum(numerator) as numerator,
  sum(denominator) as denominator
from candidate_step
group by 1
order by 1;
```

Do the same in the notebook after each major transformation.

## Key Principle

Never “fix” the final chart first. Trace until you find the first broken intermediate artifact, then fix there.
