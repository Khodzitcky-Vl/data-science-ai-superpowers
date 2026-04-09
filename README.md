# Analytics AI Superpowers

**Skills for AI-agents that make every analyst more rigorous, every experiment more trustworthy, and every notebook reproducible.**

Ever shipped an experiment only to discover a broken metric weeks later? Spent hours debugging why two notebooks produce different numbers from the same data? Got review feedback that contradicted your methodology — and you weren't sure who was right?

These skills solve exactly that. They plug into your AI coding assistant (Claude Code or Codex) and teach it how analysts actually work — from the first vague question to the final decision-ready result.

---

## What Are Skills?

Skills are specialized instructions that upgrade your AI assistant's analytical capabilities. Instead of getting generic code suggestions, your assistant learns the methodology behind good analytics: how to design experiments, validate metrics, ensure reproducibility, and catch mistakes before they reach stakeholders.

You don't need to memorize when to use which skill — the **router skill** automatically activates the right one based on what you're doing.

---

## Skill Catalog

### Think Before You Code

#### Brainstorming
`ds-brainstorming`

Turns a vague research request into a design with explicit units, metrics, assumptions, and success criteria — before you write a single line of SQL.

**When to use:** Your stakeholder says "Can you look into whether X affects Y?" and you need to figure out what that actually means analytically.

**What you get:** A structured design document with hypotheses, metric hierarchy, time windows, and robustness checks — approved before any code is written.

---

#### Analysis Plan
`ds-analysis-plan`

Converts a research question into a step-by-step execution plan detailed enough for another analyst to rebuild from scratch.

**When to use:** You know what you want to answer, but the analysis spans multiple SQL queries, pandas transformations, and notebook sections.

**What you get:** A self-contained notebook plan with cohort definitions, metric computations, validation checkpoints, and expected outputs.

---

#### Experiment Design
`ds-experiment-design`

Designs A/B tests starting from causal structure — not from available tables. Validates randomization units, metric definitions, CUPED covariates, guardrails, and contamination risks.

**When to use:** You're planning an A/B test, A/A validation, or quasi-experiment and need to get the statistical foundation right before running anything.

**What you get:** A complete experiment specification: hypothesis, unit of randomization, population, primary and guardrail metrics, failure modes, and decision rules.

---

### Build with Confidence

#### Metric Validation
`ds-metric-validation`

Catches broken, misleading, or unstable metrics before they distort your experiment readout. Checks definition accuracy, unit alignment, sensitivity, robustness, leakage, and operational quality.

**When to use:** You're about to trust a metric in an experiment or report — and you want to make sure it actually measures what you think it measures.

**What you get:** Validation results covering count uniqueness, denominator drift, distribution analysis, balance checks, and a clear pass/fail assessment.

---

#### Notebook Reproducibility
`ds-notebook-reproducibility`

Ensures your notebook is trustworthy and rerunnable — by another analyst, next month, on fresh data.

**When to use:** Your analysis depends on parameters, caches, run order, seeds, or external helpers and you need someone else (or future you) to get the same result.

**What you get:** A clean notebook structure: parameters at top, single source of truth for data, separate sections, visible progress bars, and no hidden state.

---

#### Systematic Debugging
`ds-systematic-debugging`

Traces data mismatches back to their root cause through structured investigation — no guessing, no random fixes.

**When to use:** Your notebook output disagrees with SQL results. Row counts don't add up. Sample ratios look off. Something is wrong, but you don't know what.

**What you get:** A root cause diagnosis through four phases: investigation, pattern analysis, hypothesis testing, and verified fix.

---

### Ship with Proof

#### Verification Before Completion
`ds-verification-before-completion`

Blocks any claim that an analysis is "done" or a result is "significant" without fresh rerun evidence. No more stale outputs, no more screenshots as proof.

**When to use:** You're about to present a result, close a ticket, or make a recommendation — and you want to be absolutely sure the numbers still hold.

**What you get:** Fresh verification evidence: rerun outputs, validation checks, and a clear audit trail that your conclusion is backed by current data.

---

#### Requesting Analysis Review
`ds-requesting-analysis-review`

Packages your analysis into a complete review request — so the reviewer can actually evaluate your work instead of guessing at your methodology.

**When to use:** Your experiment analysis or metric study is close to decision-ready and you need independent validation before conclusions harden into decisions.

**What you get:** A structured review package: research question, hypothesis, metric definitions, data window, notebooks, SQL, outputs, and documented assumptions.

---

#### Receiving Analysis Review
`ds-receiving-analysis-review`

Treats reviewer comments as hypotheses to evaluate — not orders to follow. Separates real methodological issues from preferences and misunderstandings.

**When to use:** You received review feedback and some comments mix valid statistical concerns with stylistic preferences or unsupported claims.

**What you get:** A rigorous evaluation of each comment: verified, challenged, or deferred — with evidence for every decision.

---

### Scale Your Work

#### Dispatching Parallel Agents
`ds-dispatching-parallel-agents`

Runs independent analyses in parallel — separate SQL extracts, metric checks, robustness analyses — each in its own agent with a disjoint scope.

**When to use:** Your plan has 2+ tasks that don't share notebook state or output tables and can run concurrently.

**What you get:** Multiple analyses completed in parallel, each with self-contained artifacts and verification rules.

---

#### Subagent-Driven Analysis
`ds-subagent-driven-analysis`

Executes your analysis plan by dispatching a fresh subagent per task, then running two-stage review: methodology first, then reproducibility.

**When to use:** You have a written plan and want fast, high-quality execution with built-in quality gates.

**What you get:** Completed analysis tasks with methodology review and reproducibility review for each deliverable.

---

#### Executing Plans
`ds-executing-plans`

Loads an analysis plan and executes it in small batches with review checkpoints between them. Each batch produces reproducible artifacts.

**When to use:** You have a written plan and want to execute it step-by-step with verification between batches.

**What you get:** Incremental execution with summary tables, diagnostic cells, and reader-facing verification at each checkpoint.

---

### The Router

#### Using Superpowers
`ds-using-superpowers`

The entry point. Automatically detects what kind of analytical work you're doing and activates the right skill — so you never have to remember which skill to call.

**When to use:** Always. This skill runs by default and routes your requests to the appropriate specialized skill.

---

## Ready-Made Bundles

Pick a bundle that matches how you work:

| Bundle | Skills | Best for |
|--------|--------|----------|
| **`analytics-core`** | 7 skills | Everyday analytics — planning, validation, debugging, reproducibility |
| **`notebook-research`** | 10 skills | Notebook-heavy research with analysis review workflow |
| **`ab-experimentation`** | 7 skills | Experiment design, metric validation, and parallel execution |
| **`all-skills`** | 13 skills | Everything — the full toolkit |

---

## Quick Start

### Prerequisites

- Python 3.12+
- [`skilz`](https://pypi.org/project/skilz/) installed:

```bash
pip install skilz
```

### Install a bundle

```bash
# Claude Code
uvx --from git+ssh://git@github.com/your-org/analytics-ai-skills.git \
  analytics-ai-installer install analytics-core --agent claude --repo your-org/analytics-ai-skills

# Codex
uvx --from git+ssh://git@github.com/your-org/analytics-ai-skills.git \
  analytics-ai-installer install analytics-core --agent codex --repo your-org/analytics-ai-skills
```

### Install a single skill

```bash
skilz install your-org/analytics-ai-skills/ds-analysis-plan --agent codex
```

### Install everything

```bash
uvx --from git+ssh://git@github.com/your-org/analytics-ai-skills.git \
  analytics-ai-installer install all-skills --agent codex --project --repo your-org/analytics-ai-skills
```

---

## How Skills Work Together

Skills aren't isolated — they chain into natural workflows:

**"I need to run an A/B test"**
> Brainstorming &#8594; Experiment Design &#8594; Analysis Plan &#8594; Metric Validation &#8594; Verification Before Completion

**"My numbers don't match"**
> Systematic Debugging &#8594; Notebook Reproducibility &#8594; Verification Before Completion

**"Review my analysis before I present it"**
> Requesting Analysis Review &#8594; Receiving Analysis Review &#8594; Verification Before Completion

**"I have a plan, execute it fast"**
> Executing Plans &#8594; Dispatching Parallel Agents &#8594; Subagent-Driven Analysis &#8594; Verification Before Completion

---

## Acknowledgements

This skill set is inspired by [Jesse Vincent](https://github.com/obra)'s [Superpowers](https://github.com/obra/superpowers) — a collection of skills that demonstrate how AI coding assistants can be taught structured, principled workflows. We adapted and extended that idea for the data analytics and experimentation domain.
