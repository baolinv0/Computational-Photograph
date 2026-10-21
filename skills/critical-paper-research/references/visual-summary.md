# Visual-first paper research report

## Goal
Help the reader understand **field trend, the focal paper's location, its value, what it does and how** within the first glance. Visuals summarize evidence; they never replace claim-level source checks.

## L2 visual storyboard
1. **🧭 Topic field map:** Use a compact timeline or branching flow (prefer Mermaid flowchart when supported) showing at least two legitimate competing research paradigms, their dated representative works, and where the focal paper sits. Differentiate verified prior methods from inferred trend. Do not depict several parallel approaches as a mandatory linear sequence.
2. **📍 Paper placement and team genealogy:** Show distinct edges for field precedence, shared-author/team inheritance and alternative systems. Label sources and avoid treating mere institutional affiliation as project continuity. A short table may be clearer than a huge graph.
3. **⚙️ What/how:** Input (type, resolution, instruction) → reuse/novel components → output, annotate purposes, constraints and claim evidence. Reused methods should not be colored or labeled as novel inventions.
4. **💡 Value and 📊 evidence:** Three concrete novel-to-reader information increments, supported/uncertain distinctions, best original tables/figures, with exact conditions.
5. **⚠️ Open issues:** Compact 3–6 issues; differentiate observed failures, untested claims and mechanistic hypotheses. **No experiment designs unless explicitly requested.**

## Presentation discipline
- Opening: one paragraph verdict plus reading tier and one-line 'why'.
- Prefer 1–3 compact, legible visuals not 12 independent cards or diagrams.
- Support Markdown Mermaid syntax when renderer supports it, else ASCII and tables.
- Every dated milestone is sourced; annotate 'inferred' on uncertain connections.
- Show author paper figures where permitted and appropriate; otherwise redraw a conceptual schematic clearly marked as your own.
- Max 3 core value points, 3–6 weaknesses; put detailed audit tables after graphics.
- Avoid speculative performance comparisons, false precision, decorative icons, and invented quantitative charts.
- If user requests a full evidence audit, expand original result checks without losing the visual executive overview.
- No 'suggested experiments', design of new datasets, statistical test plans or stop/go tables in ordinary L1/L2 output.

## Compact example (conceptual, not factual claims)
```mermaid
flowchart LR
 A[Existing route A] --> P[📍 Focal paper]
 B[Competing route B] -. alternative .-> P
 P --> C[Resulting capability]
```

Preferred final section: **Knowledge delta** — Already known | Newly supported | Still unresolved — plus reusable research lessons only when legitimately distinct from existing rules.
