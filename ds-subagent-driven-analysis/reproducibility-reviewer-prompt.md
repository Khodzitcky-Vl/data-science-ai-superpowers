# Reproducibility Reviewer Prompt Template

Use this template when dispatching a reproducibility and interpretation reviewer subagent.

**Purpose:** Verify the analysis is well-built, reproducible, and interpreted correctly.

**Only dispatch after methodology compliance passes.**

```
Task tool (general-purpose or analysis-reviewer):
  Use template at ds-requesting-analysis-review/analysis-reviewer.md

  WHAT_WAS_ANALYZED: [from worker report]
  PLAN_OR_REQUIREMENTS: Analysis Task N from [plan-file]
  DESCRIPTION: [task summary]
  NOTEBOOK_PATH: [notebook or script path]
  QUERY_REFERENCE: [query file / SQL cell reference]
  ARTIFACT_REFERENCE: [table, figure, export references]
```

**Reviewer returns:** Strengths, Issues (Critical/Important/Minor), Assessment
