---
name: "d-research-ultra"
description: "Prebuilt multi-agent deep research skill for AI agents. Use for source-backed web research, public-data collection, literature reviews, due diligence, policy or standards analysis, market or technical research, evidence ledgers, execution gates, blocker reports, and audit-grade synthesis. Ships the D Research core methodology plus a runtime-neutral orchestrator and six bundled worker-agent role definitions; the host CLI maps those roles to its own subagent/task mechanism when available, otherwise the main agent runs the same gates manually."
---

# D Research Ultra

D Research Ultra is the prebuilt multi-agent distribution of D Research.
It keeps the D Research core methodology self-contained in this package
and adds a runtime-neutral orchestrator plus six bundled worker roles.

Use this skill when the user needs source-backed research with a clear
audit trail, especially when the task is broad, high-recall, contested,
long-horizon, multilingual, or evidence-sensitive.

Do not use it to bypass login walls, paywalls, captchas, anti-bot
systems, robots restrictions, rate limits, private groups, private
profiles, or access controls. Blocked sources become blocker reports,
not escalation attempts.

## Package Model

This repository is a standalone skill package:

- Core D Research methodology: `AGENTS.md`, `references/`, `templates/`,
  `scripts/`, `adapters/`, `examples/`, and `docs/`.
- Ultra multi-agent layer: `agents/orchestrator.md`,
  `agents/spawn-contract.md`, `agents/manifest.json`, and the six role
  definitions in `agents/subagent-roles/`.
- Optional helper scripts remain small, local, and auditable. They
  support the workflow but do not replace the agent.

D Research Ultra is not tied to any specific CLI, vendor, or runtime.
The main agent delegates work through whichever subagent, task, worker,
background-agent, or agent-roster mechanism the host provides. If the
host has no real subagent mechanism, the main agent runs the same
checklists in single-agent mode and discloses that limitation.

## When To Use

Use this skill for:

- deep web research and source discovery
- public web data collection and structured extraction
- academic, literature, scoping, rapid, or PRISMA-style reviews
- market, competitor, product, and technical research
- due diligence, red-flag, risk, or public-claim review
- policy, standards, RFC, governance, and compliance analysis
- creative, cultural, media, trend, reception, and archive research
- public URL analysis and lawful public snapshot capture
- fact verification and contradiction checks
- evidence-ledger, blocker-report, and reproducibility workflows
- long-horizon research that benefits from isolated worker contexts

Refuse or reframe requests for private-person profiling, doxxing,
stalking, harassment, deanonymization, private data, or access-control
bypass.

## Execution Modes

Classify the request first with `references/research-intake.md`, then
choose the lightest mode that can meet the evidence standard.

### Fast Mode

Use for one atomic fact, one URL, one clearly scoped source, or a quick
answer where completeness is not requested.

- Main agent runs the D Research core workflow directly.
- Optionally delegate only to Evidence Verifier if the host has a cheap
  verifier subagent and the claim is important.
- Skip the full six-agent pipeline unless the user requests audit-grade
  depth.

### Standard Mode

Use for normal multi-source research.

- Main agent performs intake and source-map planning.
- Delegate Source Mapper, Data Extractor, Evidence Verifier, and Report
  Synthesizer when real worker agents are available.
- Apply `references/execution-gates.md` before final synthesis.

### Completeness-First Mode

Use when the user asks for audit-grade work, "full pipeline", "be
thorough", due diligence, contested claims, low-recall topics, or a
long-horizon task.

Run the six-worker pipeline in waves:

1. Wave 1, in parallel when the host supports it:
   Source Mapper and Public Web & Community Hunter.
2. Wave 2, in parallel after the first source batch:
   Recall Auditor and Data Extractor.
3. Wave 3:
   Evidence Verifier.
4. Wave 4:
   Report Synthesizer.

If the host only supports sequential subagents, run the same waves in
order. If a worker fails or is unavailable, run that role's checklist
manually and disclose the fallback.

## Worker Roster

The portable worker definitions live in `agents/subagent-roles/`.
Use the role IDs and names from `agents/manifest.json` as the canonical
roster.

| Role ID | Canonical worker name | Mission |
|---|---|---|
| `source-mapper` | `D Research Source Mapper` | Build source maps, search matrices, candidate URLs, blockers, identity risks, and next-query plans. |
| `recall-auditor` | `D Research Recall Auditor` | Run adversarial second-pass recall for missed sources, alternate language/register paths, archives, mirrors, and contradictions. |
| `public-web-community-hunter` | `D Research Public Web & Community Hunter` | Find lawful public web, community, forum, official social, video, and archive leads with strict privacy and identity labels. |
| `data-extractor` | `D Research Data Extractor` | Extract auditable structured data from public files, APIs, tables, embedded JSON, metadata, PDFs, OCR, and visible text. |
| `evidence-verifier` | `D Research Evidence Verifier` | Verify atomic claims against exact URLs, primary sources, contradiction checks, staleness checks, confidence, and ledger rows. |
| `report-synthesizer` | `D Research Report Synthesizer` | Turn verified findings into source-backed reports with caveats, blockers, gaps, confidence, and no unsupported claims. |

Read `agents/orchestrator.md` for the full dispatch procedure and
`agents/spawn-contract.md` for the host-runtime contract.

## Runtime-Neutral Spawn Contract

When a real worker mechanism exists, the main agent should:

1. Discover whether the six canonical workers are already configured.
2. If a host supports installing bundled role files, ask the user before
   creating or registering missing workers.
3. Dispatch role-specific task prompts using the host's own subagent or
   task mechanism.
4. Request compact, structured final outputs from each worker.
5. Merge only returned evidence and explicit caveats, not hidden worker
   assumptions.
6. Fall back to manual checklists when a worker cannot run.

Do not hard-code one vendor's command names in the core skill. Runtime
adapters may live outside this core layer, but the skill body should
remain portable.

## Core Workflow

For single-agent mode and all fallback paths, follow `AGENTS.md`.
Important references:

- Intake and routing: `references/research-intake.md`
- Source discovery: `references/source-discovery.md`
- Query fanout: `references/query-patterns.md`
- Browser-first crawl: `references/browser-first-crawl.md`
- API workflow: `references/api-access-workflow.md`
- Extraction: `references/data-extraction-toolbox.md`
- Multi-format extraction: `references/multi-format-extraction.md`
- Evidence ledger: `references/evidence-ledger.md`
- Execution gates: `references/execution-gates.md`
- Report generation: `references/report-generation.md`
- Reproducibility: `references/reproducibility-checklist.md`
- Tool adapter policy: `references/tool-adapter-policy.md`
- Long-horizon planning: `references/research-plan-protocol.md`

For specialized branches, load only the relevant reference file:

- atomic facts: `references/fact-verification.md`
- public posts: `references/social-media-archival.md`
- public-role named-person research: `references/person-aggregation.md`
- systematic reviews: `references/systematic-review-protocol.md`
- research bibliography: `references/research-bibliography.md`
- multilingual/local research: `references/multilingual-research.md`
- Vietnamese source discovery: `references/vietnamese-source-discovery.md`
- register/jargon recall: `references/register-and-jargon-expansion.md`
- frontier search: `references/frontier-search.md`

## Output Standard

Final answers should separate:

- verified facts
- source-backed inference
- unknowns and gaps
- blockers and manual retrieval paths
- contradictions or stale-source risks
- confidence by claim or section
- exact source URLs or local artifact paths

Do not present a result as complete until source mapping, recall,
coverage, evidence verification, blockers, and confidence have been
handled or explicitly marked out of scope.
