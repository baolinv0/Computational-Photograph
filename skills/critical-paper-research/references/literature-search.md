# Prior-art and trend retrieval

Research novelty with disconfirmation, not confirmatory search. L2/L3 should record queries, source coverage, dates and unsearched lanes. Never promise absolute completeness.

## Independent retrieval lanes

| Lane | Search target | Pitfall prevented |
|---|---|---|
| A | Paper citations, predecessors, original implementations | Rebranding old methods |
| B | Functional equivalents under different terminology | Keyword bias |
| C | Competing paradigm / architecture achieving the same user goal | False "only viable solution" |
| D | Independent benchmarks, negative results, failure cases | Metric dependence |
| E | Actual hardware and deployed systems | Cloud-to-device extrapolation |
| F | Earlier publication versions, citing/cited-by, follow-on papers and code releases | Broken chronology |

Use title, mathematical operation, optimization objective, task and hardware separately. Search adjacent fields such as optimization, control, restoration, signal processing and ML. Find at least 3–5 closest/competing works when available; label gaps if fewer are verified.

## Evidence ledger

For every candidate prior: canonical identity; first verifiable public date; technical overlap; crucial difference; whether directly read; citation location; scope / uncertainty.

Classify differences: genuinely new objective, new algorithm, new architecture, integration, stronger data, additional compute, different task, or better experimental coverage.

Stop only after search paths are reported and either adequate convergence is observed or the budget/source limitation is explicitly disclosed. Repeated syndications of one claim are not independent evidence.

## Topic trend claims

Require multiple independent technical lines, chronological development, contradicters and deployment maturity. Separate trend observations from forecasts; do not equate publication with shipped product.

## Topic map and team genealogy

For L2/L3, map core goals, competing technical families, maturity and surviving limitations before labelling a single paper a trend. Trace verified team continuities via repeated authors plus concrete reused data, models or benchmarks; institution names alone do not prove research lineage. Log team predecessors separately from globally nearest prior. For reusable Topic KB structure and update gates see [topic-context.md](topic-context.md).
