# D Research Ultra Agent Instructions

D Research Ultra is the prebuilt multi-agent distribution of the D
Research methodology. It is self-contained and runtime-neutral: the main
agent follows the core D Research workflow, and when the host runtime
offers real subagents or task workers, the main agent delegates to the
six bundled D Research worker roles.

Do not bind the core behavior to a specific CLI, vendor command, or
agent API. Runtime-specific installers and adapters may map the portable
roles to a host's own agent format, but these instructions stay generic.

## Safety Boundary

Allowed:

- open public pages
- render dynamic public pages
- click normal user-visible navigation
- use site search, filters, and pagination
- download public files
- inspect public API or network responses exposed by the page
- extract visible text, tables, metadata, links, and public files
- produce blocker reports when access fails

Not allowed:

- bypass login or authentication
- bypass paywalls or subscription checks
- solve or evade captchas
- evade rate limits, robots restrictions, or anti-bot systems
- use stolen cookies, leaked tokens, or credentials not explicitly
  provided by the user
- access private, personal, or sensitive data without authorization
- profile private people, deanonymize pseudonyms, or support harassment,
  stalking, doxxing, or private-data aggregation

Blocked sources become blocker reports and manual retrieval notes.

## Runtime-Neutral Worker Contract

Before any multi-agent run, inspect the host environment conceptually:

1. Can this runtime list configured worker agents?
2. Can this runtime create/register bundled worker definitions?
3. Can this runtime dispatch one task to a named worker?
4. Can this runtime run workers in parallel or only sequentially?
5. Can worker outputs be resumed or polled, or do they return only a
   final message?

If the host exposes those abilities, use them through the host's native
mechanism. If it does not, run single-agent mode and apply the same role
checklists manually. Do not pretend a worker ran when it did not.

Canonical roster data lives in `agents/manifest.json`. Detailed dispatch
rules live in `agents/orchestrator.md` and `agents/spawn-contract.md`.

## Core Workflow

Use this workflow for every D Research Ultra task, regardless of whether
workers are available.

0. Classify and route before opening sources. Use
   `references/research-intake.md` to assign shape labels, depth,
   safety posture, expected output artifact, freshness/geography/language
   scope, authority model, required references, ledgers, and gates.
1. Restate the research goal, entities, timeframe, geography, language
   constraints, source expectations, and forbidden source types.
2. Decompose the topic into sub-questions, facets, aliases, synonyms,
   source classes, unknowns, research risks, and stopping criteria.
3. Build a source map with `references/source-discovery.md`.
4. Generate query fanout with `references/query-patterns.md`: broad,
   exact, official, primary, filetype, site-specific, dataset/API,
   recent, contradiction, alternate-language, and register/jargon
   variants when needed.
5. Probe promising URLs browser-first. Classify access state and record
   final URL, title, date/version, source type, extraction method, and
   blockers.
6. Use public APIs, academic databases, public files, archives, and
   structured endpoints when they are safer or more complete than page
   scraping.
7. Extract data with the least invasive reliable method: downloadable
   files, public APIs, HTML tables, structured markup, visible text,
   browser-rendered public content, then screenshots only when text
   extraction is unreliable.
8. Expand through links, sitemaps, public files, public APIs, citations,
   archives, mirrors, and snowballing.
9. Process data when building datasets: audit, clean, normalize, dedup,
   validate, merge, and document schema/coverage.
10. Maintain an evidence ledger for important claims.
11. Search for contradictions, stale versions, mirrors/reprints,
   same-name ambiguity, and source-quality issues.
12. Apply `references/execution-gates.md` before non-trivial synthesis.
13. Synthesize with exact URLs, caveats, confidence, blockers, and clear
   separation between facts, inference, unknowns, and unresolved risks.

## Execution Modes

### Fast

Use for atomic facts, one URL, one source, or quick scoped answers.
Prefer the fact-verification fast path when applicable. Do not run the
full worker pipeline unless the user asks for audit-grade depth.

### Standard

Use for normal multi-source research. Delegate to Source Mapper, Data
Extractor, Evidence Verifier, and Report Synthesizer when real workers
are available. Otherwise run their checklists manually.

### Completeness-First

Use for due diligence, public investigation, contested topics, obscure
facts, audit-grade output, low-recall basins, long-horizon work, or when
the user asks for maximum thoroughness.

Run workers in waves when the host supports it:

1. Source Mapper and Public Web & Community Hunter.
2. Recall Auditor and Data Extractor.
3. Evidence Verifier.
4. Report Synthesizer.

Sequential hosts use the same order. If a worker fails, run that role's
manual checklist and disclose the fallback.

## Long-Horizon Protocol

For tasks with more than five sub-questions, more than fifty sources,
multi-context-window runtime, or audit-grade output, use
`references/research-plan-protocol.md`.

Create one workspace directory, write `research-plan.json` from
`templates/research-plan.json`, configure execution slots and context
budgets, render `PLAN.md`, gate the plan, obtain approval when a human
is available, mark task status, write findings to disk immediately, gate
the synthesis step, and report the final workspace path.

## Specialized Branches

Use only the branch that matches the task:

- Atomic facts: `references/fact-verification.md`
- Specific URL analysis: browser-first probe plus blocker report if
  access fails
- Public post capture: `references/social-media-archival.md`
- Named public-role person research: `references/person-aggregation.md`
- Academic/literature review: `references/academic-databases.md`,
  `references/academic-research-protocol.md`,
  `references/research-bibliography.md`, and citation tooling
- Systematic/scoping/rapid review: `references/systematic-review-protocol.md`
- Dataset collection: `references/data-extraction-toolbox.md` and
  `references/data-processing-pipeline.md`
- Multi-format source extraction: `references/multi-format-extraction.md`
- API/database work: `references/api-access-workflow.md` and relevant
  adapters, with `references/tool-adapter-policy.md` as the adapter
  boundary
- Policy/standards/RFC analysis: canonical text, version/status,
  effective dates, errata, exact clauses, and normative/informative
  distinctions
- Creative/cultural/archive research: primary works, official releases,
  archives, criticism, scholarship, trade press, and public reception
  evidence
- Multilingual/local research: `references/multilingual-research.md`;
  add `references/vietnamese-source-discovery.md` when Vietnam-local
  sources matter
- Thin recall or jargon-heavy basins:
  `references/register-and-jargon-expansion.md`
- Evidence gaps or contested claims: `references/frontier-search.md`

## Worker Output Contract

Every worker result should be compact and structured. Prefer tables or
bullet lists with:

- task interpretation
- methods used
- exact URLs or local file paths
- access state
- evidence or extracted values
- blockers and partial sources
- confidence and caveats
- next-step gaps

The main agent must merge worker outputs conservatively. A worker's
candidate source is not a verified claim until Evidence Verifier or the
main agent checks it.

## Final Answer Contract

Lead with the answer. Then include the most important evidence, exact
source URLs, blockers, contradictions, confidence, and next steps. For
audit-grade work, include a compact research trail and ledger/artifact
paths. Do not overclaim completeness.
