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
    5. Verify the outputs against the task requirements at the requested validation level
    6. Add minimal comments only where intent, methodology, or validation logic would otherwise be non-obvious
    7. Prefer one short comment or markdown explanation before a complex block over line-by-line narration
    8. Self-review before reporting back

    Work from: [directory]

    If you encounter unexpected results, missing data, or contradictions, **pause and ask**. Do not guess.

    ## Before Reporting Back: Self-Review

    Review your work with fresh eyes.

    **Completeness:**
    - Did I run the requested core diagnostics for the task's validation level?
    - Did I produce every requested artifact?
    - Did I miss a decision-protecting robustness check or validation step?
    - Did any risk signal appear that should escalate validation depth?

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

    **Readability:**
    - For every group comparison, distribution, time trend, statistical result,
      or correlation and variable relationship — did I add a chart?
    - For dense tables (5+ rows, multiple metrics) — did I add a supporting chart,
      or note "table-only" with an acceptable reason?
    - If I noted "table-only", is the reason acceptable? (Acceptable: ≤3 rows,
      exact integers a chart would distort, single-number summary. Not acceptable:
      "table is clear enough.")
    - Does each major analytical section have a markdown cell immediately preceding
      it that explains WHY this step is needed (not just what it does)?
    - Are the plot titles, axis labels, and annotations sufficient for a
      colleague reading without running the notebook?

    If you find issues during self-review, fix them before reporting.

    ## Report Format

    When done, report:
    - What you analyzed
    - What you reran and what compact diagnostics passed, failed, or triggered escalation
    - Artifacts produced
    - Files changed
    - Self-review findings
    - Any open issues or methodological concerns
```
