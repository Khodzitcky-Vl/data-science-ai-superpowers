# DS Defense-in-Depth Validation

## Overview

When an analytical bug is caused by a wrong join, unstable denominator, or hidden filter, one patch feels sufficient. It is usually not. The next notebook cell, memo update, or helper function can bypass it.

**Core principle:** Add validation at every critical layer so the same class of bug becomes hard to reintroduce.

## Layers

### Layer 1: Extract Validation
- Expected row counts
- Expected unique units
- Window and timezone checks
- Assignment coverage checks

### Layer 2: Metric Table Validation
- Numerator and denominator sanity checks
- Missingness and zero-inflation checks
- Invariant and SRM checks

### Layer 3: Estimation Validation
- Cluster unit preserved
- Effect estimate compared against simple benchmark version
- Outlier contribution quantified

### Layer 4: Reporting Validation
- Tables, figures, and written conclusions agree
- Final memo uses the primary metric, not a convenient slice
- Limitations documented

## Applying the Pattern

When you find a bug:

1. Map every stage the broken value passes through
2. Add a validation check at each stage
3. Make each check cheap enough to rerun
4. Fail loudly when assumptions break

## Example

Bug: treatment conversion lift driven by duplicated hotel rows after enrichment

Defense-in-depth:
- Extract layer: uniqueness check on `hotel_id`
- Metric layer: denominator drift by group and day
- Estimation layer: compare clustered and unclustered estimates
- Reporting layer: note sensitivity of result to enrichment join

**Result:** The same join bug cannot silently survive to the final memo.
