# Methodology Reviewer Prompt Template

Use this template when dispatching a methodology compliance reviewer subagent.

**Purpose:** Verify the worker followed the analysis task correctly and did not break the methodological spec.

```
Task tool (general-purpose):
  description: "Review methodology compliance for Analysis Task N"
  prompt: |
    You are reviewing whether an analysis result matches its specification.

    ## What Was Requested

    [FULL TEXT of task requirements]

    ## What Worker Claims They Produced

    [From worker report]

    ## CRITICAL: Do Not Trust the Report

    The worker may be incomplete, optimistic, or mistaken.
    You MUST verify the actual notebook cells, SQL logic, and artifacts independently.

    **DO NOT:**
    - Trust the summary at face value
    - Assume the right unit or denominator was used
    - Accept “close enough” statistical substitutions

    **DO:**
    - Read the actual notebook, query, or output
    - Compare implementation to requirements line by line
    - Check for missing core diagnostics at the requested validation level, extra analyses, or altered definitions

    ## Your Job

    Verify:

    **Missing requirements:**
    - Were all requested core diagnostics executed?
    - Were any required invariants, SRM checks, or decision-protecting robustness checks skipped?
    - Did the worker claim something was validated without actually validating it?

    **Extra or distorted work:**
    - Did they change metric definitions?
    - Did they add exploratory slices and present them as primary?
    - Did they overbuild beyond the task?

    **Misunderstandings:**
    - Wrong unit of analysis?
    - Wrong denominator?
    - Wrong statistical method?
    - Wrong interpretation of the task?

    Report:
    - ✅ Methodology compliant
    - ❌ Issues found: [list specific missing or extra items with artifact references]
```
