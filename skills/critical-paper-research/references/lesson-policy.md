# Research lessons: durable decision rules

A lesson is an actionable check with a trigger and limitation, not a retrospective slogan. Do not inflate seed lessons into independently validated general laws.

## Lifecycle

candidate (observed in one case) → validated (multiple independent reviews or controlled corroboration) → revised (new counterexample / condition) → retired (superseded).

Each rule: stable Rxx identifier, title, status, trigger, failure mode, action/check, decisive minimal counterexample, scope, source and correction history. Copy the template from assets/lesson-template.md.

## Seed rules (candidates)

### R01 — Novelty requires functional prior-art search
Trigger: first/novel/new mechanism claims. Failure: search by name and paper citations alone. Check: mathematical/functional analogues and older cross-field solutions; differentiate integration from novel algorithm. Source cases: PhoenixSR vs diffusion-supervision line, BluePixel source anchoring. Status: candidate.

### R02 — Numerical claims require source-level reconciliation
Trigger: paper vs blog claims and extrapolated numbers. Failure: wrong parameter counts, subsets, methods or units. Check PDF + config + equation; show the calculation and assumptions. Source case: BluePixel mobile 5.6B assumption vs project 9B backbone. Status: candidate.

### R03 — Hardware cost must be end-to-end
Trigger: "mobile-ready" or fast inference claims. Failure: using server step time, ideal TOPS or single activation as complete device performance. Check observed device / precision / weights / buffers / encoder / VAE / runtime / thermal and inference budget. Source case: BluePixel and DreamLite comparisons. Status: candidate.

### R04 — Agent gains require equal-budget attribution
Trigger: multi-step Agent improves image quality. Failure: extra samples, rewrite, stronger tools or judge masquerade as planning gains. Check Backbone; Prompt Rewrite; Best-of-N; fixed routing; Agent with/without verification at matched executor, tools and total budget. Source case: BluePixel and HarnessIR. Status: candidate.

### R05 — Evaluator dependence is not independent replication
Trigger: reward trained/used in model, agent search and benchmark. Failure: high internal score treated as general improvement. Check independent task metrics, held-out scenes and independent blind human/user study. Source case: BluePixReward. Status: candidate.

### R06 — Deployment novelty needs counterexample search
Trigger: claim no earlier on-device implementation. Failure: ignore alternative pipelines such as low-res edit + high-res recompose/tiling. Check earlier real-device demos, latency and quality under the exact task and definition. Source case: MobilePicasso and other mixed-resolution routes. Status: candidate.

## Write-back policy

Before adding a new lesson search for semantically equivalent rules. Prefer updating evidence and boundaries of an existing rule. New rule only for a distinct recurring failure mechanism, with traceable evidence. Preserve original mistaken judgment in a correction record: prior claim → newly checked evidence → why the error happened → corrected claim → procedural change. No automatic GitHub writes without authorization or existing repository policy.
