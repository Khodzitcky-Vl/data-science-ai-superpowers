# Analysis Worker Prompt Template

Use this template when dispatching an analysis worker subagent.

```
Task tool (general-purpose):
  description: "Execute Analysis Task N: [task name]"
  prompt: |
    You are executing Analysis Task N: [task name]

    ## Task Description

    [FULL TEXT of task from plan - paste it here, do not make the subagent read the plan file]

    ## Context

    [Where this fits in the study, dependencies, metric context, current interpretation]

    ## Before You Begin

    If anything is unclear about:
    - Metric definitions or denominators
    - Time windows, exclusions, or cohorts
    - Expected outputs or acceptance criteria
    - Statistical method or robustness checks

    **Ask now.** Raise concerns before starting work.

    ## Your Job

    Once requirements are clear:
    1. Execute exactly what the task specifies
    2. Keep one-off analytical logic inside the notebook unless the task explicitly justifies an external module
    3. Rerun relevant SQL or notebook steps
    4. Save or report the requested artifacts
    5. Verify the outputs against the task requirements
    6. Add minimal comments only where intent, methodology, or validation logic would otherwise be non-obvious
    7. Prefer one short comment or markdown explanation before a complex block over line-by-line narration
    8. Self-review before reporting back

    Work from: [directory]

    If you encounter unexpected results, missing data, or contradictions, **pause and ask**. Do not guess.

    ## Before Reporting Back: Self-Review

    Review your work with fresh eyes.

    **Completeness:**
    - Did I run every requested check?
    - Did I produce every requested artifact?
    - Did I miss a robustness check or validation step?

    **Methodology:**
    - Is the unit of analysis correct?
    - Did I preserve the agreed metric definitions?
    - Did I accidentally introduce scope creep?

    **Reproducibility:**
    - Can the notebook section or query be rerun cleanly?
    - Are parameters, filters, and windows explicit?
    - Did I avoid adding unnecessary external helper modules for notebook-only logic?
    - Did I add concise comments for non-obvious filters, exclusions, joins or dedup logic, metric definitions, and validation steps?
    - Did I avoid commenting obvious operations line by line?
    - Do the written conclusions match the outputs?

    If you find issues during self-review, fix them before reporting.

    ## Report Format

    When done, report:
    - What you analyzed
    - What you reran and what passed
    - Artifacts produced
    - Files changed
    - Self-review findings
    - Any open issues or methodological concerns
```
