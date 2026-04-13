---
name: ds-metric-validation
description: Use when a metric definition, denominator, CUPED covariate, linearization choice, invariant, outlier treatment, missingness pattern, or leakage risk may distort an experiment or validation readout
---

# DS Metric Validation

## Overview

Validate the metric before trusting the experiment. A metric is acceptable only if it is interpretable, stable under the chosen unit, and sensitive to the business change you care about.

**Typical triggers:** unstable lift, denominator drift, SRM, invariant failure, heavy tails, metric sign flips after filter changes

Metric validation should follow the shared validation budget from `ds-using-superpowers`. Do the minimum checks needed to protect the decision, then escalate only when risk signals appear.

## Minimum Checks

- Definition: numerator, denominator, filters, null handling
- Unit alignment: metric computed at the same level as inference
- Denominator sanity: counts by group and day where relevant
- Missingness overview for numerator, denominator, and key covariates
- Interpretability: metric can plausibly move under the treatment and maps to the business question

For exploratory work, these checks can be one compact diagnostic table plus a short interpretation note.

## Escalate When

- Sample ratio, invariant, or pre-period balance looks suspicious
- Denominator drifts by group, day, client, hotel, or traffic source
- Metric flips sign after a small reasonable filter change
- A few clients, hotels, partners, or requests drive most of the lift or variance
- Control and treatment have different missingness patterns
- The metric or covariate may use post-treatment information
- Logging gaps, delayed events, or backfills may affect the result

## Standard Checks

- Count uniqueness by intended unit
- Compare pre-period balance and sample ratio where assignment groups exist
- Plot the primary metric distribution, not only the mean
- Quantify outlier contribution to the primary estimate or variance

## Optional Robustness

Use these when the escalation triggers appear or the result is decision-ready:

- Recompute with one or two alternative reasonable definitions
- Check tails, winsorization, zero inflation, and missingness sensitivity
- Sensitivity analysis for alternative definitions or segment mix
- Leakage: metric or covariates do not use post-treatment information improperly
- Operational quality: logging completeness, delayed events, backfills

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
