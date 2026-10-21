# Topic-first research context and reading decision

## Purpose
A paper is a node in a research field, not a self-contained product brochure. Judge its **information gain relative to the reader's current knowledge** before deciding how much time to invest. Do not conflate worth reading with novelty, credibility, replication or adoption.

## L1 lightweight preflight
1. Name Topic and one-sentence defining problem; identify 1–2 persistent bottlenecks or say unknown.
2. Identify the closest *verified* field predecessor and any directly connected team predecessor; if unavailable explicitly mark unverified.
3. State the paper's claimed and independently inspected delta.
4. Decision: **must-read / deep-read / selective / scan / defer**, why (maximum 3 reasons), exact sections or figures to prioritize, expected value (direction / breakthrough / system / engineering / contradiction / opportunity).
5. Separate: worth reading / claim可信 / worth reproducing / research investment. L1 must not require comprehensive genealogy.

## Visual storytelling
L2 begins with a compact dated Topic trend / rival-paradigm map, a **marked position** for the focal paper, and an input→blocks→output method diagram, subject to rendering capability. Diagrams are interpretive unless quoted from the paper; cite nodes and label uncertain inferred relations. Use icons sparingly and preserve legibility. See [visual-summary.md](visual-summary.md).

## L2 contextual research
### A. Topic map
- Scope, target task, fundamental constraints, maturity stage and unsettled bottlenecks
- Parallel methods and competition: data-first, model-first, representation, tools, optimization, systems, deployment (only applicable families)
- Chronological field milestones and genuinely nearest functional predecessors
- Positive AND negative empirical evidence; independent technical lines required to infer trends
- Which bottleneck paper addresses and which persist

### B. Author and team trajectory
- Verify named recurring **individual authors** and distinct collaborations across dated papers; distinguish institution-wide work
- Timeline: prior projects, acquired datasets, benchmarks, models, code, hardware/software assets
- Explain paper-to-paper inheritance (direct evidence vs inference) and potential pivots
- Compare **closest team predecessor** separately from **closest field predecessor**; they are often not the same
- Do not claim lab strategy or personal contributions solely from affiliation or author list

### C. Paper position and value
- Prior work → actual incremental mechanism/system integration → falsifiable prediction → result
- Counterfactual: what could a knowledgeable reader already have inferred without this paper?
- Identify changed beliefs and non-changed beliefs, and level E0–E4 for evidence provenance
- Reading value can be high even if novelty is modest (robust negative result, transferable recipe, consolidated deployment evidence).

## L3 research decision
Only on explicit request: add goal-dependent next actions, research portfolio fit, testable residual bottleneck, cost/quality/time constraints and smallest falsification experiment. Distinguish trend **observation** from team roadmap **inference** and product **evidence**.

## Topic Knowledge Base (reusable file structure)
Maintain one compact Topic note per stable topic, not one expensive resurvey per paper:
- Topic identifier / definition / owner or source repo / last verified / coverage cutoff
- Core questions; technical paradigms; dated milestone graph; active bottlenecks
- Claims and conflicting evidence with source pointers and confidence
- Team genealogies with author-level source evidence and inherited assets
- Related paper registry: canonical ID, version, novelty delta, lesson and reading tier
- Open hypotheses, priority experiments, falsifiers, product/deployment status
- Search log: six independent lanes as appropriate; known coverage holes and next refresh condition

Update policy: retrieve KB → search only missing/delta lanes → correct prior assertions with a visible changelog. Do not infer complete coverage from finite search. Every asserted relationship must have paper, code or reputable primary evidence.

## Quality gates
- No paper-level SOTA or first claim without field predecessor.
- No 'team has been pursuing X' claim without dated recurring-author or concrete shared-asset evidence.
- No trend claim from one lab or one architectural family.
- No mandatory deep review for an L1 defer decision.
- No forced arithmetic score of unrelated reading-value axes.
- Distinguish author claim, verified document, independent evidence, prediction, and unknown.
