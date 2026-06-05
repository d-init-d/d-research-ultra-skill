# D Research Ultra

Prebuilt multi-agent deep research skill for AI agents.

D Research Ultra is developed from the core
[D Research Skill](https://github.com/d-init-d/d-research-skill). It
ships the D Research core methodology as a self-contained package, then
adds a runtime-neutral orchestration layer and six ready-to-register
worker roles for teams that want a research system they can install and
use immediately.

[![Self-test](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/lint-and-self-test.yml/badge.svg)](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/lint-and-self-test.yml)
[![Link check](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/link-check.yml/badge.svg)](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/link-check.yml)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

Use the core [D Research Skill](https://github.com/d-init-d/d-research-skill)
when you want the methodology, references, scripts, and workflow so you
can design your own agent system. Use D Research Ultra when you want the
same foundation packaged as a ready-made multi-agent research pipeline.

## Positioning

| Package | Best for | What you get |
|---|---|---|
| [D Research Skill](https://github.com/d-init-d/d-research-skill) | Builders who want a flexible core methodology. | Core workflow, references, scripts, templates, adapters, examples, and evals. |
| D Research Ultra | Operators who want a prebuilt research agent system. | Everything in the core methodology plus a Main Research Agent, six portable worker roles, wave execution, spawn contract, and install recipes. |

D Research Ultra is not tied to one CLI, vendor, model provider, or
agent runtime. Host tools such as Claude Code, opencode, Minimax/Mavis,
Codex, or private agent CLIs can map the bundled roles to their own
subagent, task, worker, or background-agent mechanism.

## Product Scope

D Research Ultra is a skill package. It is not a hosted crawler, SaaS
product, Python package, Docker image, notebook, or API service.

An agent reads `SKILL.md` and follows the workflow. The repository
ships:

- portable agent instructions
- a runtime-neutral worker contract
- six worker role definitions
- research references and safety policies
- templates and examples
- local helper scripts
- eval benches and CI checks

Runtime-specific installation details are intentionally kept in this
README. `SKILL.md` stays compact and portable so agent context is spent
on the research task, not on vendor setup instructions.

## Capabilities

| Area | Capability |
|---|---|
| Research modes | Fast, standard, and completeness-first research. |
| Source strategy | Browser-first public-source discovery with source maps, query fanout, recall audits, archives, APIs, files, and contradiction checks. |
| Evidence model | Exact URLs, source types, access states, extraction methods, evidence ledgers, caveats, blockers, and confidence. |
| Multi-agent model | One Main Research Agent plus six portable worker roles. |
| Runtime model | Host CLIs map the bundled roles to native subagent/task/worker mechanisms. |
| Fallback model | If no real workers exist, the main agent runs the same gates manually and discloses the fallback. |
| Safety model | Read-only public-source work; no login bypass, paywall bypass, captcha evasion, private profiles, doxxing, stalking, or private-data aggregation. |
| Quality gates | Offline self-tests, internal-reference checks, decision-tree coverage, node syntax checks, and GitHub Actions. |

## Architecture

```text
D Research Ultra
  Main Research Agent
    - intake and safety routing
    - depth selection
    - worker dispatch
    - evidence merge
    - final verification gate
    - final answer

  Worker roster
    - D Research Source Mapper
    - D Research Recall Auditor
    - D Research Public Web & Community Hunter
    - D Research Data Extractor
    - D Research Evidence Verifier
    - D Research Report Synthesizer
```

The canonical roster lives in `agents/manifest.json`.
The orchestration playbook lives in `agents/orchestrator.md`.
The runtime adapter contract lives in `agents/spawn-contract.md`.
The portable worker prompts live in `agents/subagent-roles/`.

## Repository Layout

| Path | Purpose |
|---|---|
| `SKILL.md` | Skill entry point, triggers, execution modes, and output standards. |
| `AGENTS.md` | Root agent workflow, safety rules, specialized branches, and final-answer contract. |
| `agents/manifest.json` | Canonical role IDs, names, files, and execution waves. |
| `agents/orchestrator.md` | Main Research Agent playbook for pipeline mode. |
| `agents/spawn-contract.md` | Runtime-neutral contract for installing and dispatching workers. |
| `agents/subagent-roles/` | Six portable worker role definitions. |
| `references/` | Research protocols, source discovery, extraction, verification, safety, reporting, and specialized-domain guidance. |
| `templates/` | Evidence ledgers, search logs, PRISMA flow, data packages, reports, and research plans. |
| `scripts/` | Local helper scripts for probing, crawling, extraction, evidence ledgers, reports, evals, and validation. |
| `examples/` | Usage examples, datasets, eval benches, and fixtures. |
| `.github/workflows/` | CI checks for release health. |
| `.agents/skills/testing-scripts/` | Maintainer skill for script and reference verification. |

## Worker Roster

| Role ID | Worker name | Purpose |
|---|---|---|
| `source-mapper` | `D Research Source Mapper` | Build source maps, search matrices, candidate URLs, blockers, identity risks, and next queries. |
| `recall-auditor` | `D Research Recall Auditor` | Run adversarial second-pass recall across alternate names, languages, registers, archives, mirrors, and contradiction paths. |
| `public-web-community-hunter` | `D Research Public Web & Community Hunter` | Find lawful public web, community, forum, official social, video, and archive leads with privacy and identity discipline. |
| `data-extractor` | `D Research Data Extractor` | Extract structured data from public files, APIs, HTML tables, embedded data, PDFs, OCR, and visible text. |
| `evidence-verifier` | `D Research Evidence Verifier` | Verify claims with exact URLs, primary-source preference, contradictions, staleness checks, confidence, and ledger rows. |
| `report-synthesizer` | `D Research Report Synthesizer` | Produce source-backed report drafts from verified findings, with caveats, blockers, gaps, and no unsupported claims. |

## Execution Modes

### Fast

Use for atomic facts, one URL, one source, or a tightly scoped lookup.
The main agent runs direct verification and skips the full worker
pipeline.

### Standard

Use for ordinary multi-source research. The main agent can delegate
Source Mapper, Data Extractor, Evidence Verifier, and Report Synthesizer
when real workers are available.

### Completeness-First

Use for audit-grade, due-diligence, contested, low-recall, multilingual,
public-role, or long-horizon research.

Completeness-first runs as a dependency-aware wave graph:

1. Source Mapper plus Public Web & Community Hunter.
2. Recall Auditor plus Data Extractor.
3. Evidence Verifier.
4. Report Synthesizer.

Hosts with parallel workers may run each wave concurrently. Sequential
hosts preserve the same order. Hosts without workers use manual fallback
and disclose it in the research trail.

## Quick Start

Clone the repository into the skill directory used by your agent
runtime:

```bash
git clone https://github.com/d-init-d/d-research-ultra-skill.git d-research-ultra
```

Point the runtime at:

```text
d-research-ultra/SKILL.md
```

If your runtime supports worker agents, register the six role files from
`agents/subagent-roles/` using the names and IDs in
`agents/manifest.json`.

## Runtime Recipes

These recipes describe how to map the portable package into common agent
runtimes. They are operator guidance only; the core skill itself stays
runtime-neutral.

### Generic Agent Runtime

1. Install this repository as a skill folder.
2. Load `SKILL.md` as the skill entry point.
3. Load `AGENTS.md` as the root workflow when the runtime supports root
   agent instructions.
4. Register workers from `agents/subagent-roles/`.
5. Use `agents/manifest.json` for canonical names and execution waves.
6. Use `agents/spawn-contract.md` to map list/install/dispatch/result
   behavior to the host runtime.

### Claude Code

Install the repository where Claude Code loads project or user skills.
Then translate each file in `agents/subagent-roles/` into a Claude Code
custom subagent.

Keep the active chat/session agent as the Main Research Agent. Worker
agents should not call each other directly; orchestration remains in the
main session.

### opencode

Install this repository as a skill folder, then map the six role files
to opencode agents using your project configuration.

Keep `D Research Ultra Orchestrator` as the primary behavior and allow
delegation only to the six `D Research ...` workers listed in
`agents/manifest.json`.

### Minimax, Mavis, Codex, Or Private CLIs

Use the same portable adapter pattern:

1. Read `agents/manifest.json`.
2. Create or register each worker from its role file.
3. Use `agents/orchestrator.md` as the main-agent playbook.
4. Map dispatch, polling, failure handling, and final-result collection
   to the host runtime's native worker mechanism.

No core file requires a specific command name.

### No Worker Support

Install only the skill folder. The Main Research Agent will run the D
Research core workflow and apply the worker checklists manually when
needed.

## Optional Tooling Setup

For Node helper scripts:

```bash
npm ci
npx playwright install chromium
```

For Python helper scripts:

```bash
python --version
```

The bundled Python scripts are stdlib-first. Optional extras are listed
in `pyproject.toml` for embeddings, translation, and extraction
features.

## Verification

Run the full offline self-test chain before release:

```bash
npm run self-test
```

Useful focused checks:

```bash
npm run refs:check
npm run refs:check:decision-tree
node scripts/run_python.mjs scripts/check_node_syntax.py
node scripts/run_python.mjs scripts/check_no_plan_files.py
node scripts/run_python.mjs scripts/run_metadata.py self-test
```

GitHub Actions runs the release-health checks on push and pull request:

- `Lint and self-test`
- `Link check`

## Release Quality

D Research Ultra is maintained as a ready-to-ship skill package:

- Runtime-specific guidance lives in README, not in `SKILL.md`.
- Internal references are checked by `scripts/check_internal_refs.py`.
- Every `references/*.md` file must be reachable from `SKILL.md` or
  `AGENTS.md`.
- Helper scripts have offline self-tests.
- Node helper syntax is checked with `node --check`.
- Local research plan artifacts are blocked from commits.
- CI validates self-tests and link health.

## Safety

D Research Ultra is read-only and public-source first.

It must not:

- bypass login walls, paywalls, captchas, anti-bot systems, robots
  restrictions, rate limits, private groups, private profiles, or access
  controls
- use stolen cookies, leaked tokens, or unauthorized credentials
- profile private people
- deanonymize pseudonyms
- support stalking, harassment, doxxing, or private-data aggregation
- collect sensitive personal information outside a lawful public-role
  research scope

Blocked sources become blocker reports and manual retrieval notes.

## License

D Research Ultra uses the same license family as the core
[D Research Skill](https://github.com/d-init-d/d-research-skill):
[Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)
(`CC-BY-NC-4.0`).

See `LICENSE` for the full license text. In short, the material may be
shared and adapted with attribution for non-commercial purposes, subject
to the terms of the license.
