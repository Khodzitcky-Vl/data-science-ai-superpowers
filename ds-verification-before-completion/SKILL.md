---
name: ds-verification-before-completion
description: Use when about to claim that an experiment result, metric validation, or notebook analysis is final, significant, trustworthy, or decision-ready and you need fresh rerun evidence instead of stale outputs
---

# DS Verification Before Completion

## Overview

No analytical conclusion without fresh evidence. If the notebook was not rerun under the stated parameters, or the outputs do not match the written conclusion, the work is not done.

If reruns are brittle, cached, or order-dependent, use `ds-notebook-reproducibility` first.

**Core principle:** Evidence before claims, always.

**Violating the letter of this rule is violating the spirit of this rule.**

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you have not run the verification in this message, you cannot claim the result is trustworthy.

## Verification Gate

Before any completion claim:

1. Rerun the relevant notebook cells or script entry point
2. Confirm input window, filters, and experiment identifiers
3. Check row counts, unit counts, and group balance
4. Recompute the reported estimate, interval, and significance metric
5. Verify that charts, tables, and written conclusions agree
6. State limitations that still matter

Skip any step = not verified.

## Common Failures

| Claim | Requires | Not Sufficient |
|-------|----------|----------------|
| Experiment is significant | Fresh effect size, interval, and significance output | Old screenshot or p-value alone |
| Metric is valid | Fresh denominator, unit, and robustness checks | "It looked stable earlier" |
| Notebook is reproducible | Clean rerun with explicit parameters | One successful run in dirty state |
| Result is decision-ready | Primary result, limitations, and review completed | Best slice looks good |
| Agent finished task | Artifacts checked independently | Agent summary alone |

## Minimum Evidence

- Exact data window
- Randomization and analysis unit
- Final sample sizes by group
- Metric definition used in the final result
- Statistical method used
- Reproducible artifact: notebook, query, exported table, or memo

## Red Flags - STOP

- Using "should", "probably", or "looks right"
- Declaring significance before rerun
- Claiming no effect without interval width
- Trusting agent output without checking artifacts
- Relying on partial reruns
- Any statement implying readiness without fresh evidence

## Not Sufficient

- "It ran yesterday"
- One screenshot without rerun
- A p-value without effect size and interval
- A lift estimate without denominator validation
- A notebook that depends on hidden local state

## Rationalization Prevention

| Excuse | Reality |
|--------|---------|
| "It ran yesterday" | Rerun it now |
| "I am confident" | Confidence is not evidence |
| "The effect is obvious" | Quantify it fresh |
| "Partial rerun is enough" | Partial reruns prove little |
| "The reviewer already checked it" | Verify independently |

## Key Patterns

**Result claim:**
```
✅ [Rerun notebook or script] [See: updated estimate, CI, sample sizes] "Result is X"
❌ "Should still be X"
```

**Requirements claim:**
```
✅ Re-read plan or decision question → verify each required artifact → report actual state
❌ "Notebook ran, so analysis is done"
```

**Delegated work:**
```
✅ Agent reports success → inspect artifacts → rerun critical checks → report actual state
❌ Trust agent report
```

## Why This Matters

- False analytical confidence causes bad product and experiment decisions
- A stale notebook can reverse the conclusion
- Unverified claims break trust quickly

## When To Apply

**ALWAYS before:**
- Claiming a result is final, significant, trustworthy, or decision-ready
- Publishing or socializing conclusions
- Moving to the next task
- Closing a review cycle

## The Bottom Line

Rerun. Read the outputs. Then make the claim.

This skill verifies notebook analysis through reruns, output inspection, and analytical checks, not through unit-test or `pytest` conventions unless explicitly requested.

## Common Mistakes

- Reporting the best slice instead of the primary result
- Forgetting to update the narrative after rerunning the notebook
- Claiming causality when the design only supports association
- Declaring no effect when confidence intervals are still too wide
