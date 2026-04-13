---
name: ds-notebook-reproducibility
description: Use when notebook results depend on parameters, caches, run order, hidden state, seeds, external helper code, or exported tables and the analysis must be rerunnable by another analyst
---

# DS Notebook Reproducibility

## Overview

A notebook is trustworthy only when another analyst can rerun it and get the same result or understand exactly why not.

The default reproducible form for analytical notebook work is one self-contained notebook with explicit parameters and notebook-local one-off logic.

Notebook must optimize for analyst readability. Prefer diagnostic outputs over interleaved assertions. Use runtime exceptions only for true prerequisites or one final strict-validation pass.

Use this before `ds-verification-before-completion` if reruns are fragile or outputs depend on stale notebook state.

Apply the shared validation budget from `ds-using-superpowers`. Reproducibility work should remove hidden state and stale outputs, not add a large validation framework to the notebook.

## Required Structure

- Parameters at the top: dates, experiment ids, filters, paths, seeds
- One source of truth for extracts and joins
- Separate sections for extraction, validation, estimation, robustness, and conclusion
- Keep validation sections compact; one diagnostic table or manifest is preferred when it covers the selected validation level
- Notebook-local helper functions for one-off analysis logic
- Visible but compact progress for long-running cells: use `tqdm` only when it updates in place in the notebook environment; otherwise use concise stage, timing, row-count, or percentage checkpoints
- Short markdown cells or block comments before genuinely non-obvious analytical sections
- Final output cells that can be rerun without hidden state

## Reproducibility Rules

- Set seeds for any stochastic step
- Avoid mutable hidden globals between cells
- Save intermediate datasets only when version and source are explicit
- Mark exploratory cells clearly if they should not drive the final conclusion
- Keep the notebook self-contained by default; introduce external `.py` modules only for real cross-project reuse, production needs, or another explicit technical reason
- If external helper code remains, pin its path and version and explain why notebook-local code is insufficient
- Export final tables or figures used in the memo
- Prefer one short comment or markdown explanation before a complex block over commenting obvious lines one by one
- Comment non-obvious filters, exclusions, joins or dedup logic, metric definitions, and validation logic that a fresh analyst might misread
- Do not scatter runtime assertions throughout an analyst-facing notebook; use visible verification outputs by default
- Reserve exceptions for missing prerequisites or a final optional strict validation step
- Do not leave long-running notebook cells opaque; the rerun should show progress via a compact progress bar, stage labels, timing, or status cells so another analyst can tell that work is advancing
- Do not use nested or high-frequency `tqdm` bars when they create many saved output lines. For large inner loops, prefer one outer bar plus sparse checkpoints, or set coarse `mininterval`/`miniters`, `leave=False`, or `disable=True` for inner bars.

## Quick Checks

- For final or strict claims: restart kernel and rerun all
- For intermediate scoped claims: rerun the relevant section and state what remains unverified
- Confirm outputs appear in the same order
- Confirm long-running cells expose visible progress and do not look frozen during reruns
- Confirm saved outputs are not polluted by hundreds of progress-bar refresh lines
- Check that cached files are either regenerated or intentionally pinned
- If the notebook imports external helper code, verify the dependency is justified, versioned, and not just a cleanliness refactor

## Common Mistakes

- Manual edits inside CSV extracts
- Reusing a DataFrame created in a cell that no longer reflects the current query
- Mixing exploratory plots with the final readout
- Leaving parameter values hardcoded deep inside the notebook
- Moving one-off notebook logic into helper scripts for style rather than reproducibility or reuse
