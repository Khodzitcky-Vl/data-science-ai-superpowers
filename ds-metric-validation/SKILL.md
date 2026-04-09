---
name: ds-metric-validation
description: Use when a metric definition, denominator, CUPED covariate, linearization choice, invariant, outlier treatment, missingness pattern, or leakage risk may distort an experiment or validation readout
---

# DS Metric Validation

## Overview

Validate the metric before trusting the experiment. A metric is acceptable only if it is interpretable, stable under the chosen unit, and sensitive to the business change you care about.

**Typical triggers:** unstable lift, denominator drift, SRM, invariant failure, heavy tails, metric sign flips after filter changes

## Validation Checklist

- Definition: numerator, denominator, filters, null handling
- Unit alignment: metric computed at the same level as inference
- Invariance: pre-treatment attributes stay balanced across groups
- Sensitivity: metric can plausibly move under the treatment
- Robustness: tails, winsorization, zero inflation, missingness
- Leakage: metric or covariates do not use post-treatment information improperly
- Operational quality: logging completeness, delayed events, backfills

## Core Tests

- Count uniqueness by intended unit
- Check denominator drift by group and by day
- Plot distribution, not only the mean
- Compare pre-period balance and sample ratio
- Quantify outlier contribution to lift and variance
- Recompute with alternative reasonable definitions

## Methods Notes

- CUPED needs a pre-period covariate available for most units and correlated with outcome
- Linearization is for ratio metrics when cluster size inflates variance
- Cluster bootstrap or cluster-robust errors matter when unit-level dependence is real

## Red Flags

- Metric flips sign after a small filter change
- A few clients or hotels drive most of the lift
- Control and treatment have different missingness patterns
- The metric only exists after a treatment-dependent event
- Denominator can be affected by the treatment itself

## Common Mistakes

- Validating only significance, not interpretability
- Treating post-treatment slices as pre-defined segments
- Ignoring exposure logging gaps because totals look close
