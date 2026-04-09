CORE_SKILLS = [
    "ds-using-superpowers",
    "ds-brainstorming",
    "ds-analysis-plan",
    "ds-metric-validation",
    "ds-systematic-debugging",
    "ds-notebook-reproducibility",
    "ds-verification-before-completion",
]

BUNDLES = {
    "analytics-core": CORE_SKILLS,
    "notebook-research": [
        *CORE_SKILLS,
        "ds-experiment-design",
        "ds-requesting-analysis-review",
        "ds-receiving-analysis-review",
    ],
    "ab-experimentation": [
        "ds-using-superpowers",
        "ds-experiment-design",
        "ds-analysis-plan",
        "ds-metric-validation",
        "ds-verification-before-completion",
        "ds-dispatching-parallel-agents",
        "ds-subagent-driven-analysis",
    ],
    "all-skills": [
        "ds-analysis-plan",
        "ds-brainstorming",
        "ds-dispatching-parallel-agents",
        "ds-executing-plans",
        "ds-experiment-design",
        "ds-metric-validation",
        "ds-notebook-reproducibility",
        "ds-receiving-analysis-review",
        "ds-requesting-analysis-review",
        "ds-subagent-driven-analysis",
        "ds-systematic-debugging",
        "ds-using-superpowers",
        "ds-verification-before-completion",
    ],
}
