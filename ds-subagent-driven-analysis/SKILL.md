---
name: ds-subagent-driven-analysis
description: Use when executing a written analysis plan in the current session and tasks are mostly independent across SQL extracts, notebook sections, metric validations, robustness checks, or memo sections
---

# DS Subagent-Driven Analysis

Execute plan by dispatching a fresh subagent per task, with two-stage review after each: methodology compliance review first, then reproducibility and interpretation review.

For notebook projects, the default expectation is still a self-contained notebook. Workers should not create extra helper modules for one-off analytical logic unless the task explicitly justifies that dependency.

Workers must preserve runtime observability from the plan. Long loops, chunked jobs, and SQL-heavy steps should not run silently; default to `tqdm` for iterable work and add visible status or timing output elsewhere.

**Core principle:** Fresh subagent per task + two-stage review (methodology then reproducibility/interpretation) = high quality, fast iteration

**Use after:** `ds-analysis-plan`

**Use instead of:** `ds-executing-plans` when you want to stay in the same session and keep iteration fast

If the current step contains 2 or more independent tasks with disjoint scope, combine this skill with `ds-dispatching-parallel-agents`.

## When to Use

```dot
digraph when_to_use {
    "Have analysis plan?" [shape=diamond];
    "Tasks mostly independent?" [shape=diamond];
    "Stay in this session?" [shape=diamond];
    "ds-subagent-driven-analysis" [shape=box];
    "ds-executing-plans" [shape=box];
    "Manual execution or ds-brainstorming first" [shape=box];

    "Have analysis plan?" -> "Tasks mostly independent?" [label="yes"];
    "Have analysis plan?" -> "Manual execution or ds-brainstorming first" [label="no"];
    "Tasks mostly independent?" -> "Stay in this session?" [label="yes"];
    "Tasks mostly independent?" -> "Manual execution or ds-brainstorming first" [label="no - tightly coupled"];
    "Stay in this session?" -> "ds-subagent-driven-analysis" [label="yes"];
    "Stay in this session?" -> "ds-executing-plans" [label="no - separate session"];
}
```

**vs. DS Executing Plans:**
- Same session
- Fresh subagent per task
- Two-stage review after each task: methodology first, then reproducibility and interpretation
- Faster iteration without waiting for human review after every task

## Per-Task Flow

```dot
digraph process {
    rankdir=TB;

    subgraph cluster_per_task {
        label="Per Task";
        "Dispatch analysis worker (./analysis-worker-prompt.md)" [shape=box];
        "Analysis worker asks questions?" [shape=diamond];
        "Answer questions, provide context" [shape=box];
        "Analysis worker executes, reruns, self-reviews" [shape=box];
        "Dispatch methodology reviewer (./methodology-reviewer-prompt.md)" [shape=box];
        "Methodology reviewer confirms task matches spec?" [shape=diamond];
        "Analysis worker fixes methodological gaps" [shape=box];
        "Dispatch reproducibility reviewer (./reproducibility-reviewer-prompt.md)" [shape=box];
        "Reproducibility reviewer approves?" [shape=diamond];
        "Analysis worker fixes reproducibility or interpretation issues" [shape=box];
        "Mark task complete" [shape=box];
    }

    "Read plan, extract all tasks with full text, note context, create TodoWrite" [shape=box];
    "More tasks remain?" [shape=diamond];
    "Dispatch final analysis reviewer for entire study" [shape=box];
    "Use ds-verification-before-completion" [shape=box style=filled fillcolor=lightgreen];

    "Read plan, extract all tasks with full text, note context, create TodoWrite" -> "Dispatch analysis worker (./analysis-worker-prompt.md)";
    "Dispatch analysis worker (./analysis-worker-prompt.md)" -> "Analysis worker asks questions?";
    "Analysis worker asks questions?" -> "Answer questions, provide context" [label="yes"];
    "Answer questions, provide context" -> "Dispatch analysis worker (./analysis-worker-prompt.md)";
    "Analysis worker asks questions?" -> "Analysis worker executes, reruns, self-reviews" [label="no"];
    "Analysis worker executes, reruns, self-reviews" -> "Dispatch methodology reviewer (./methodology-reviewer-prompt.md)";
    "Dispatch methodology reviewer (./methodology-reviewer-prompt.md)" -> "Methodology reviewer confirms task matches spec?";
    "Methodology reviewer confirms task matches spec?" -> "Analysis worker fixes methodological gaps" [label="no"];
    "Analysis worker fixes methodological gaps" -> "Dispatch methodology reviewer (./methodology-reviewer-prompt.md)" [label="re-review"];
    "Methodology reviewer confirms task matches spec?" -> "Dispatch reproducibility reviewer (./reproducibility-reviewer-prompt.md)" [label="yes"];
    "Dispatch reproducibility reviewer (./reproducibility-reviewer-prompt.md)" -> "Reproducibility reviewer approves?";
    "Reproducibility reviewer approves?" -> "Analysis worker fixes reproducibility or interpretation issues" [label="no"];
    "Analysis worker fixes reproducibility or interpretation issues" -> "Dispatch reproducibility reviewer (./reproducibility-reviewer-prompt.md)" [label="re-review"];
    "Reproducibility reviewer approves?" -> "Mark task complete" [label="yes"];
    "Mark task complete" -> "More tasks remain?";
    "More tasks remain?" -> "Dispatch analysis worker (./analysis-worker-prompt.md)" [label="yes"];
    "More tasks remain?" -> "Dispatch final analysis reviewer for entire study" [label="no"];
    "Dispatch final analysis reviewer for entire study" -> "Use ds-verification-before-completion";
}
```

## Prompt Templates

- `./analysis-worker-prompt.md` - Dispatch analysis worker subagent
- `./methodology-reviewer-prompt.md` - Dispatch methodology compliance reviewer subagent
- `./reproducibility-reviewer-prompt.md` - Dispatch reproducibility and interpretation reviewer subagent

## Example Workflow

```
You: I'm using DS Subagent-Driven Analysis to execute this plan.

[Read plan file once]
[Extract all tasks with full text and context]
[Create TodoWrite with all tasks]

Task 1: Build assignment-quality baseline extract

[Dispatch analysis worker with full task text + context]

Worker: "Before I begin - should assignment quality be checked at client or pseudo-session level?"

You: "Client is the randomization unit. Pseudo-session can be used only as a diagnostic slice."

Worker:
  - Built baseline extract
  - Reran SQL and notebook cells
  - Produced assignment coverage table and daily counts
  - Self-review: Found one filter mismatch, fixed it

[Dispatch methodology reviewer]
Methodology reviewer: ❌ Issues:
  - Missing invariant check for country mix
  - Extra slice presented as if primary

[Worker fixes issues]

[Methodology reviewer re-reviews]
Methodology reviewer: ✅ Methodology compliant

[Dispatch reproducibility reviewer]
Reproducibility reviewer: Important issue:
  - Final notebook cell uses stale cached extract path

[Worker fixes notebook parameter]

[Reproducibility reviewer re-reviews]
Reproducibility reviewer: ✅ Approved

[Mark task complete]
```

## Parallel Case

When several tasks are truly independent:

1. Confirm disjoint write scope and no shared notebook state
2. Dispatch one worker per task through `ds-dispatching-parallel-agents`
3. Review each result separately
4. Integrate only after all artifacts and verifications are in hand

## Reviewer Focus

- Methodology review: unit alignment, metric correctness, statistical method, leakage, bias
- Reproducibility review: rerun stability, parameter clarity, notebook self-containment, final tables or plots, wording of conclusions, whether non-obvious analytical logic has concise explanatory comments, and whether long-running work has visible progress signals

## Advantages

**vs. Manual execution:**
- Fresh context per task
- Questions surfaced before work begins
- Review loops catch methodological drift early

**vs. DS Executing Plans:**
- Same session
- Continuous progress
- Review checkpoints happen automatically

## Integration

**Required workflow skills:**
- `ds-analysis-plan` - creates the plan this skill executes
- `ds-requesting-analysis-review` - review template for reproducibility and interpretation review
- `ds-verification-before-completion` - verify final conclusions before claiming readiness

**Subagents should use when needed:**
- `ds-systematic-debugging` - when numbers disagree or reruns drift
- `ds-metric-validation` - when metric definitions or denominators become suspect
- `ds-notebook-reproducibility` - when notebook state is fragile

**Alternative workflow:**
- `ds-executing-plans` - use for a separate execution session instead of same-session execution

**Verification model:**
- Rerun notebook or SQL steps
- Check artifacts and validation outputs
- Do not assume unit-test or `pytest` workflow
- No special git-worktree setup is required

## Red Flags

- One worker handles multiple unrelated tasks with stale context
- Review starts before the result is rerun
- Style-only comments block methodology comments, but missing comments on non-obvious analytical logic are still valid reproducibility issues
- The controller trusts a worker summary without checking artifacts
- Parallel workers edit the same notebook or output table
- Skip review loops after issues are found
- Start reproducibility review before methodology review is green
- Move to next task while either review has open issues
- A worker moves one-off notebook logic into a new `.py` helper module without explicit task justification
- A worker leaves long loops, chunked transforms, or SQL-heavy tasks without `tqdm`, status output, or any other visible progress signal
