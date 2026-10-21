# Repositories and write-back contract

These are optional integrations; the skill functions without GitHub and must not claim that a GitHub directory is automatically installed into ChatGPT.

Computational-Photograph is the canonical location for a paper's technical review, under papers/arxiv-<id>.md where possible. Read ARCHIVE_PROTOCOL.md and registry before any update. Update the existing canonical paper note rather than creating a duplicate.

CameraPaper holds company attribution, products, cross-company trends and reusable research methodology under knowledge/research-methodology/. Read AGENTS.md, README.md and DATA_SCHEMA.md before modifying it; its brand evidence is not a substitute for a full paper review.

Notion and alphaXiv, if actually connected, can serve as reading indexes or paper bookmarks but must not silently overwrite manual statuses or duplicate authoritative text.

## Write workflow

1. Search existing paper identity and rule ID; inspect current main branch policies and source files.
2. Separate verified source claims from inference, and mark exactly what was checked this time.
3. Update canonical article, relevant knowledge entry, links and registry only where materially changed. Write to relevant dated update record if repository rules require.
4. Use commit or PR only with explicit user authorization or existing standing policy; resolve concurrent writes by refetching current version.
5. Read the remote file back, report exact GitHub links and outstanding unverified items. On failure report partial-write status.

Never invent successful replication, review, installation, sync, or publication.
