---
name: ds-experiment-design
description: Use when planning or revisiting an A-B test, A-A validation, split methodology, or quasi-experiment and decision quality depends on the hypothesis, randomization unit, exposure unit, guardrails, or contamination risk
---

# DS Experiment Design

## Overview

Design the experiment before touching the notebook. A clean statistical readout cannot rescue a weak unit of randomization, a biased metric, or a vague decision rule.

If metric definitions, denominators, CUPED, or linearization are still uncertain, switch to `ds-metric-validation` before trusting the design.

## When to Use

- New A/B test design for API, funnel, pricing, ranking, or availability changes
- Validating randomization unit, split logic, CUPED, linearization, or guardrails
- Reframing an existing study because results are hard to interpret
- Quasi-experiments where contamination, interference, or seasonality may dominate

## Required Outputs

Write these down before analysis:

- Hypothesis: expected business effect and why it should exist
- Unit: user, client, hotel, request, pseudo-session, or other unit actually randomized
- Population: inclusion, exclusion, time window, ramp rules
- Metrics: primary, secondary, guardrails, invariants
- Failure modes: leakage, interference, denominator drift, missing data, novelty effects
- Decision rule: effect size, confidence interval, p-value policy, minimum detectable effect, practical significance

## Core Pattern

Start from causal structure, not from available tables.

1. What receives treatment?
2. What can observe treatment?
3. What can interfere across groups?
4. Which metric moves if the business outcome improves?
5. Which metric would falsely move because of logging or traffic composition?

If these answers point to different entities, randomization and analysis units are probably misaligned.

## Quick Checks

- Randomization unit equals exposure unit?
- Exposure unit equals metric denominator?
- Guardrails can detect harm unrelated to the primary metric?
- Enough pre-period data for CUPED or baseline adjustment?
- Segment heterogeneity known before slicing results?

## Common Mistakes

- Choosing the metric because it is easy to query
- Treating request-level rows as independent when treatment is client-level
- Adding slices only after seeing the result
- Calling statistically noisy movement a business win
- Ignoring operational constraints such as throttling, caching, or supplier mix
