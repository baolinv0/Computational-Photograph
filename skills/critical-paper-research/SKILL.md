---
name: critical-paper-research
description: Use when a user asks to read, critique, compare, reproduce, contextualize, or assess the novelty, evidence, limitations, deployment, or research value of an academic paper or an emerging research topic, especially in computational photography, ISP, image restoration, editing, and agent systems.
metadata:
  version: "1.0.0"
---

# Critical Paper Research / 批判性论文研究

> Goal: turn a paper into an **evidence-bounded research decision**, not a fluent summary. Reusable lessons should improve the **next** review.

## Scope & safety

- Apply to **public** academic papers, arXiv, technical reports and research comparisons. For private/unpublished manuscripts, confirm authorization and venue/company AI and confidentiality policies before external retrieval or sharing; default to authorized local processing.
- This skill is a procedure; **it cannot access the web/GitHub or save files by itself**. Use only actually available tools. Never claim a search, replication, benchmark, or GitHub write that did not occur.
- Follow user-specified scope and repository rules. Never turn a paper's author claim into independent verification, nor a lab benchmark into a shipped mobile product claim.

## Modes (choose the least costly that resolves the user's decision)

| Mode | When | Mandatory output |
|---|---|---|
| **L1 Triage** | Paper Watch / broad scan | Problem, real delta vs closest known prior, strongest evidence, key uncertainty, read/defer decision; explicitly identify whether only abstract was read |
| **L2 Deep Review** | “分析这篇论文”、compare paper/blog, claim novelty | 12-dimension audit, claim–evidence matrix, 3–5 nearest/competing works **when verifiably available**, rival explanations, missing controls, failure boundary, maturity and credible minimum experiment |
| **L3 Research Decision** | Reproduce, select direction, engineering planning | L2 plus a falsifiable hypothesis, minimal controlled experiment, cost/quality Pareto, stop/go criteria and evidence gaps before deployment; do **not** claim experiments were run |

For **survey/review papers**, audit search coverage, taxonomy, selection bias, contradictions and unresolved questions rather than forcing one-model ablations. When source access is limited, issue a scoped review with visible coverage limitations instead of feigning L2 completeness.

## Required process

1. **Intake and source of truth.** Resolve canonical identity (arXiv/DOI), version/date, authors, paper type and user's decision. Read the actual paper, relevant figures/tables, supplement and code/config **when available**. Note exactly which parts were checked. A user-supplied blog is *secondary evidence*, not the paper. Record source access failures.
2. **First-principles reconstruction.** Express task, inputs/outputs, constraints, objective, baseline, physical/information limits, and why old approaches fail. Separate true underlying problem from the authors' framing.
3. **Closest-prior and disconfirmation search.** BEFORE judging novelty, search both matching terms and *functional equivalents*, including earlier methods from other subfields, alternative architectures, source citations, papers that contradict “first”, and relevant deployed systems. Search by **method / task / evaluation / deployment**, not only paper title. Record search paths, cutoff and residual coverage gaps. See [literature-search.md](references/literature-search.md).
4. **Mechanism and attribution.** Build a `prior work → actual delta → predicted benefit → supporting experiment` chain for **each major claim**. Separate new algorithm from reuse/integration, model scale, new data, inference budget and tool availability. Recompute sensitive numerical claims from source definitions; use bounds/units.
5. **Audit experiments.** Inspect data overlap, training/test split, prompt/metric parity, baselines, seeds/variance, statistical uncertainty, ablations, equal-compute alternatives, evaluator dependence, negative results, weak subsets and selection policy. If a test is absent, label **not established**, not “disproved”. See [review-checks.md](references/review-checks.md).
6. **Two adversarial passes.** `Builder`: formulate the strongest evidence-supported contribution. `Reviewer`: find closest precedents, confounders, counterexamples and decisive missing controls. Reconcile via cited evidence. This can be done by **one agent in separate passes**; never imply independently run agents without actually running them.
7. **Domain & deployment fit.** For imaging topics read [imaging-checks.md](references/imaging-checks.md). Specify RGB/RAW/latent, input/output resolution **in pixels**, real vs synthetic data, fidelity vs aesthetics, runtime hardware and precision, *end-to-end* latency/memory/energy, and cloud vs on-device evidence. Do not equate 4K output with native 4K processing.
8. **Decision and verification.** Report **Fact / Author-reported / Independently checked / Inference / Unknown**. Distinguish scientific novelty, experimental strength, engineering value and product applicability. Provide the **smallest falsifiable experiment** that could overturn the conclusion, with controls, measurable effects, and exit criteria.
9. **Reusable learning.** Check existing rules before adding a new one. Record only a reusable mistake/insight with `trigger → failure mode → check → counterexample → boundary → evidence`; otherwise cite an existing rule. If sources change a prior judgment, retain an explicit correction trail. See [lesson-policy.md](references/lesson-policy.md).
10. **Persist only if requested or already authorized.** Respect repository authority, deduplicate paper IDs, update the **single canonical paper note**, optionally index lessons and write a short receipt. Confirm actual write/readback; otherwise supply files or text and state not uploaded. See [repository-integration.md](references/repository-integration.md).

## 12 audit questions

1. **Problem:** Why this problem, why now, and what physical/information constraints apply?
2. **Position:** What is the nearest prior work and adjacent competing paradigm?
3. **Novelty:** What exactly is original vs repackaged or integrated?
4. **Mechanism:** Why should it work, and which component is causal?
5. **Experimental validity:** Are baselines, data, hyperparameters and inference budgets comparable?
6. **Attribution:** Could better data/model/tool/evaluator/search budget explain the gain?
7. **Metrics:** Do metrics align with task success and avoid reward contamination?
8. **Failure boundary:** Which edge cases and negative results limit generalization?
9. **Replicability & cost:** Are training, weights, hardware, compute, latency, memory and energy actually available/measured?
10. **Trend:** Are multiple independent works, chronological prior art and counterexamples consistent with the claimed trend?
11. **Research / engineering / product:** What is gained in each category **separately**?
12. **Falsification:** What minimal test would change this decision?

## Evidence rubric and required artifact

Use evidence tags alongside each decisive claim:

- **E0 Unknown:** not accessed, missing or unverifiable.
- **E1 Stated:** paper/blog/author asserts; original experiment not inspected.
- **E2 Inspected:** original method/table/config supports a claim **under stated conditions**.
- **E3 Corroborated:** independent source or fair replication supports same claim.
- **E4 Reproduced:** actually rerun under documented conditions; exact replication scope stated.

These are **provenance levels**, not a single scalar for research quality. `E2` can still be weak causal evidence. Never upgrade E2→E3 merely because multiple articles repeat one source. Each quantitative statement includes benchmark/subset, baselines, metric direction, hardware (if performance), resolution, version and a link/location, where applicable.

For L2/L3, use [review-template.md](assets/review-template.md) as an **internal completeness check**, not a requirement to dump a 12-section essay. Put decisions first; separate author claims from reviewer inference; cite sections/figures/tables/code; disclose uncovered evidence. For systematic reviews, do not claim exhaustive coverage without a protocol and saturation/selection audit.

## Auto-triggered adversarial checks

| Trigger | Must explicitly check |
|---|---|
| “first/new/SOTA” | chronological nearest prior; functional equivalents; identical-budget matching; benchmark selection |
| “Agent improves” | same executor, tools and calls; Prompt Rewrite vs Best-of-N vs routing vs feedback; equal total budget; independent verifier |
| “restores high-frequency detail” | identifiable information vs hallucination, GT definition, degraded-observation consistency, negative cases |
| “native 4K / on-device / fast” | exact H×W and tokens, params and precision, real hardware, weight+activation peaks, pre/postprocessing, power, on-device vs server |
| “reward/RL/IQA superior” | scorer trained/selected/evaluated on same rubric/data? assessor independence and humans |
| “industry trend/product ready” | ≥2 independent lines of evidence, shipped product proof, counterexamples and alternative architectures |
| “compared to a blog” | source-of-claim trace: paper vs blog inference vs own calculation; recalculate key numbers |

## Minimum finish gate

No L2 conclusion about **novelty** without nearest-prior search (or prominent "not assessed"); no **on-device** claim without measured mobile hardware; no **causal Agent** claim without budget decomposition (or state unproven); no **trend** from one paper; no **success** claim without matched metric and failure boundary. If tools/data are unavailable, provide an honest partial assessment rather than fabricate completeness.

**Recommended sources / inspirations** (concepts adapted, no third-party content reproduced): `agentskills.io/specification`, Sci-Extract, K-Dense Literature Review and Peer Review, and this project's documented BluePixel/AgenticIR review lessons. See [sources.md](references/sources.md).