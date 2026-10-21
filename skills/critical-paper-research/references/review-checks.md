# Critical experimental audit

For each central contribution, explicitly trace:

| Field | Question |
|---|---|
| Claim | What precisely is claimed, under what scope? |
| Source | Which PDF section, figure, table, appendix or code lines? |
| Prior | What is the closest earlier approach? |
| Delta | Which part is actually new? |
| Evidence | Dataset, size, metric, direction, baselines, seeds, confidence, budget |
| Alternative | Better model/data/labels/tools, more samples, stronger evaluator, cherry-picked subset? |
| Boundary | Where does the method not work? |
| Decisive test | Cheapest ablation or paired experiment distinguishing causal explanations |

## Mandatory checks

- Trace every reported number to original units, exact dataset/subset, checkpoint and evaluation date; do not mix 3305 and 2513 samples.
- Compare like with like: model size, training data, extra expert tools, prompting, total inference calls and human intervention.
- Check train/validation/test leakage; reference-image or scene overlap; repeated prompts; evaluator built using training reward.
- Investigate per-task negative results, seed variance, confidence intervals and worst-case examples. Unknown is not equivalent to false.
- If an Agent is credited: evaluate Backbone, prompt rewrite, same-budget Best-of-N, fixed heuristic routing, learned planning, with/without verification, independent scorer.
- If new components are proposed simultaneously: isolate component contributions and their interactions, not just total gain.
- Distinguish author qualitative demonstrations from blinded independent user preference assessments.
- Distinguish implementation availability (repository shell) from runnable released weights and full training recipe.

## Builder–Reviewer reconciliation

Builder states strongest evidence-supported contribution. Reviewer searches falsifying prior art and uncontrolled variables. Final decision may be "promising but insufficient evidence"; do not force certainty.

## Test recommendation

Declare hypothesis, paired inputs and baseline, control variables, outcome and side-effects, required sample size or power rationale when possible, cost, and a negative result that would change the research decision.
