---
name: ds-receiving-analysis-review
description: Use when receiving feedback on experiment design, SQL logic, notebook analysis, or statistical conclusions and comments may mix real methodological issues with preferences, misunderstandings, or unsupported claims
---

# Receiving Analysis Review

## Overview

Treat review comments as hypotheses to evaluate, not as instructions to obey blindly. Statistical correctness and causal clarity matter more than social agreement.

If a disputed comment changes the metric, denominator, or inference unit, rerun the relevant part of `ds-metric-validation` before accepting or rejecting it.

**Core principle:** Verify before implementing. Ask before assuming. Technical correctness over social comfort.

## Response Pattern

1. Read all comments first
2. Separate methodology issues from presentation issues
3. Restate the claim in precise analytical terms
4. Verify it against the actual notebook, SQL, and design
5. Implement or push back with evidence

## Forbidden Responses

**NEVER:**
- "You're absolutely right"
- "Great point"
- "I'll just change it now" before verification

**INSTEAD:**
- Restate the analytical issue precisely
- Verify it
- Push back if needed

## Handling Unclear Feedback

If any blocking comment is unclear:
- Stop
- Ask for clarification before implementing any item that depends on it

Do not implement a partial subset if the unresolved item could change the method or interpretation.

## Source-Specific Handling

### From your human partner
- Trusted, but still restate clearly if scope is ambiguous
- Move quickly to action after understanding

### From external or delegated reviewers
- Verify against the actual design and artifacts
- Check whether the reviewer had the full context
- Push back if the suggestion breaks the agreed methodology

## Evaluate Each Comment For

- Is the reviewer challenging design, implementation, or wording?
- Does the comment improve causal validity or only preferred style?
- Does the suggestion break comparability with the primary metric definition?
- Is more data needed to resolve the disagreement?

## Feedback On Notebook Readability

When feedback targets notebook readability, keep the validation logic but refactor its presentation before defending the original implementation.

If the issue is analyst UX rather than methodology:
- Preserve the analytical checks
- Convert fail-fast notebook checks into reader-facing summaries, manifests, or diagnostic cells when that improves readability
- Debate the methodology only after the presentation form is cleaned up

## Valid Pushback

Push back when the comment:

- Confuses exploratory slicing with the pre-registered primary result
- Suggests a metric that is post-treatment or leaky
- Ignores cluster dependence or randomization unit
- Overstates significance from a noisy subgroup

## Implementation Order

For multi-item feedback:
1. Clarify unclear items first
2. Fix blocking methodological issues
3. Then fix reproducibility or presentation issues
4. Rerun the affected section after each important fix

## Good Responses

- "Checked this against the unit definition; request-level inference is invalid here. Keeping cluster-level aggregation."
- "You were right; the denominator excluded zero-exposure units. Fixed and reran the notebook."

## When To Push Back

Push back when:
- The suggestion weakens causal validity
- The reviewer confuses exploratory and primary results
- The suggestion breaks comparability with the agreed metric
- The reviewer is extrapolating beyond the data

## Acknowledging Correct Feedback

When feedback is correct:
- "Fixed. Reran the notebook and updated the conclusion."
- "Verified. The denominator was wrong; corrected and reran."

Do not perform gratitude theater. State the fix.

## Gracefully Correcting Your Pushback

If you pushed back and were wrong:
- "You were right. I checked the artifact and corrected it."
- "Verified this and updated the analysis. My initial read was wrong because the cached extract was stale."

## Common Mistakes

- Agreeing before verifying the math
- Implementing only easy comments while ignoring the blocking methodological one
- Debating verbally without rerunning the relevant section
- Treating reviewer preference as methodological truth
