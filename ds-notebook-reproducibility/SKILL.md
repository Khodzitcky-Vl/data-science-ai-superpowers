---
name: ds-notebook-reproducibility
description: Use when notebook results depend on parameters, caches, run order, hidden state, seeds, external helper code, or exported tables and the analysis must be rerunnable by another analyst
---

# DS Notebook Reproducibility

## Overview

A notebook is trustworthy only when another analyst can rerun it and get the same result or understand exactly why not.

The default reproducible form for analytical notebook work is one self-contained notebook with explicit parameters and notebook-local one-off logic.

Use this before `ds-verification-before-completion` if reruns are fragile or outputs depend on stale notebook state.

## Required Structure

- Parameters at the top: dates, experiment ids, filters, paths, seeds
- One source of truth for extracts and joins
- Separate sections for extraction, validation, estimation, robustness, and conclusion
- Notebook-local helper functions for one-off analysis logic
- Final output cells that can be rerun without hidden state

## Reproducibility Rules

- Set seeds for any stochastic step
- Avoid mutable hidden globals between cells
- Save intermediate datasets only when version and source are explicit
- Mark exploratory cells clearly if they should not drive the final conclusion
- Keep the notebook self-contained by default; introduce external `.py` modules only for real cross-project reuse, production needs, or another explicit technical reason
- If external helper code remains, pin its path and version and explain why notebook-local code is insufficient
- Export final tables or figures used in the memo

## Quick Checks

- Restart kernel and rerun all
- Confirm outputs appear in the same order
- Check that cached files are either regenerated or intentionally pinned
- If the notebook imports external helper code, verify the dependency is justified, versioned, and not just a cleanliness refactor

## Common Mistakes

- Manual edits inside CSV extracts
- Reusing a DataFrame created in a cell that no longer reflects the current query
- Mixing exploratory plots with the final readout
- Leaving parameter values hardcoded deep inside the notebook
- Moving one-off notebook logic into helper scripts for style rather than reproducibility or reuse
