# D Research Ultra Usage Examples

D Research Ultra can run in one context or with real worker agents,
depending on what the host runtime supports.

## Modes

### Fast

Use for atomic facts, one URL, or one clearly scoped source.

Example:

```text
d-research-ultra: find the official URL for RFC 9457
```

Expected behavior:

- classify as atomic fact
- hit the primary source
- verify the URL
- answer directly with exact source URL
- skip the full worker pipeline

### Standard

Use for normal multi-source research.

Example:

```text
d-research-ultra: compare LangGraph, CrewAI, and AutoGen for production agent workflows
```

Expected behavior:

- classify as technical/market research
- map official docs, repos, releases, issues, benchmarks, and recent
  analysis
- delegate Source Mapper, Data Extractor, Evidence Verifier, and Report
  Synthesizer if workers are available
- otherwise run those checklists manually
- return a source-backed comparison with exact URLs and caveats

### Completeness-First

Use for audit-grade, long-horizon, contested, due-diligence, low-recall,
or public-role tasks.

Example:

```text
d-research-ultra: audit public claims about <company/product/project> and find red flags
```

Expected worker waves:

1. Source Mapper and Public Web & Community Hunter
2. Recall Auditor and Data Extractor
3. Evidence Verifier
4. Report Synthesizer

Sequential runtimes use the same order. Runtimes without workers use
single-agent fallback and disclose it.

## Public-Role Research

Example:

```text
d-research-ultra: research the public role and published work of <named public figure>
```

Expected behavior:

- apply `references/person-aggregation.md`
- refuse private-person profiling, harassment, stalking, doxxing,
  deanonymization, or private data aggregation
- use Public Web & Community Hunter only for lawful public-role sources
  relevant to the task
- label same-name risks and identity confidence
- separate verified public-role evidence from leads and unknowns

## Policy Or Standards Research

Example:

```text
d-research-ultra: analyze the obligations and effective dates in a data-protection regulation
```

Expected behavior:

- classify as policy/standards analysis
- prioritize canonical source text, official guidance, current version,
  effective dates, amendments, errata, and exact clauses
- verify normative vs informative language
- return a source-backed clause table with caveats

## Dataset Collection

Example:

```text
d-research-ultra: collect a public dataset of official release dates and changelog URLs for these projects
```

Expected behavior:

- classify as dataset/extraction
- prefer official APIs, downloadable files, structured pages, and HTML
  tables before free-text extraction
- keep data dictionary, coverage notes, extraction methods, and
  blockers
- validate representative rows against source pages

## Audit Trail

For audit-grade work, include a compact trail:

```text
Audit trail:
- Mode: completeness-first
- Source Mapper: returned 42 candidate URLs, 5 blocked/partial
- Public Web & Community Hunter: skipped; not relevant to policy task
- Recall Auditor: returned 11 missed candidates and 3 stale-source risks
- Data Extractor: extracted 2 tables, coverage partial
- Evidence Verifier: verified 12 claims, contradicted 2, unresolved 1
- Report Synthesizer: drafted final report from verified rows
- Fallbacks: none
```

If a worker cannot run:

```text
Audit trail:
- Evidence Verifier: manual_fallback because the host runtime had no
  worker dispatch mechanism. The main agent applied the verifier
  checklist directly.
```

Do not hide fallbacks.
