# D Research Ultra

Prebuilt multi-agent deep research skill for AI agents: D Research core
methodology plus a runtime-neutral orchestrator and six ready-to-register
worker roles.

[![Self-test](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/lint-and-self-test.yml/badge.svg)](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/lint-and-self-test.yml)
[![Link check](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/link-check.yml/badge.svg)](https://github.com/d-init-d/d-research-ultra-skill/actions/workflows/link-check.yml)

Use [`d-research-skill`](https://github.com/d-init-d/d-research-skill)
when you want the core methodology and prefer to build your own research
system. Use `d-research-ultra-skill` when you want the same methodology
packaged as a ready-made multi-agent research system.

## At A Glance

| Area | What D Research Ultra provides |
|---|---|
| Primary users | Agent operators who want a prebuilt source-backed research pipeline. |
| Access model | Read-only public-source research by default. Blocked sources become blocker reports. |
| Agent model | One Main Research Agent plus six portable worker role definitions. |
| Runtime model | Runtime-neutral. Host CLIs map the bundled roles to their own subagent/task/worker mechanism. |
| Fallback model | If no real workers exist, the main agent runs the same gates manually and discloses the fallback. |
| Verification | Offline self-tests, internal-reference checks, node syntax checks, and CI workflows. |

## Product Scope

This is a skill package, not a hosted crawler, SaaS product, Python
package, Docker image, notebook, or API service.

An agent reads `SKILL.md` and follows the workflow. The repository ships
instructions, adapter policies, worker role definitions, references,
templates, examples, eval benches, and optional helper scripts. The
helper scripts are small, local, and auditable; they support the
workflow but do not replace the agent.

The runtime-specific installation notes below are intentionally kept in
this README. `SKILL.md` stays portable and compact so agent context is
spent on research, not on vendor setup instructions.

## What Is Included

- `SKILL.md` - skill entry point and trigger guidance.
- `AGENTS.md` - root agent workflow and execution rules.
- `agents/manifest.json` - canonical worker roster and execution waves.
- `agents/orchestrator.md` - Main Research Agent playbook.
- `agents/spawn-contract.md` - runtime-neutral worker contract.
- `agents/subagent-roles/` - six portable worker role definitions.
- `references/`, `templates/`, `scripts/`, `adapters/`, `examples/`,
  and `docs/` - bundled D Research core methodology and tooling.
- `.github/workflows/` - CI checks for scripts and documentation health.
- `.agents/skills/testing-scripts/` - maintainer sub-skill for script
  verification after edits.

## Worker Roster

| Role ID | Worker name | Purpose |
|---|---|---|
| `source-mapper` | `D Research Source Mapper` | Source maps, search matrices, candidate URLs, blockers, identity risks, next queries. |
| `recall-auditor` | `D Research Recall Auditor` | Adversarial second-pass recall, alternate names/languages/registers, archives, mirrors, contradictions. |
| `public-web-community-hunter` | `D Research Public Web & Community Hunter` | Lawful public web, forum, community, official social, video, and archive leads with privacy discipline. |
| `data-extractor` | `D Research Data Extractor` | Structured extraction from public files, APIs, tables, embedded data, PDFs, OCR, and visible text. |
| `evidence-verifier` | `D Research Evidence Verifier` | Claim verification with exact URLs, primary-source preference, contradiction checks, confidence, and ledger rows. |
| `report-synthesizer` | `D Research Report Synthesizer` | Source-backed reports from verified findings, with caveats, blockers, gaps, and no unsupported claims. |

## Execution Modes

- **Fast**: one context, direct verification, no full pipeline.
- **Standard**: staged worker use for normal multi-source research.
- **Completeness-first**: wave-based six-worker pipeline for audit-grade,
  contested, due-diligence, low-recall, or long-horizon research.

Completeness-first runs as a wave graph:

1. Source Mapper + Public Web & Community Hunter.
2. Recall Auditor + Data Extractor.
3. Evidence Verifier.
4. Report Synthesizer.

Hosts with parallel workers may run each wave concurrently. Sequential
hosts preserve the same order. Hosts without workers use manual fallback.

## Install

### Generic Skill Install

Clone this repository into the skill directory used by your agent
runtime:

```bash
git clone https://github.com/d-init-d/d-research-ultra-skill.git d-research-ultra
```

Then point the runtime at `d-research-ultra/SKILL.md`.

If your runtime supports worker agents, register the six role files from
`agents/subagent-roles/` using the names in `agents/manifest.json`.

### Claude Code

Install the skill folder where your Claude Code setup loads project or
user skills. For subagents, translate each role file into a Claude Code
custom subagent:

- `agents/subagent-roles/source-mapper.md`
- `agents/subagent-roles/recall-auditor.md`
- `agents/subagent-roles/public-web-community-hunter.md`
- `agents/subagent-roles/data-extractor.md`
- `agents/subagent-roles/evidence-verifier.md`
- `agents/subagent-roles/report-synthesizer.md`

Use `agents/manifest.json` for canonical names. The Main Research Agent
should remain the active chat/session agent; worker agents should not
call each other directly.

### opencode

Install this repository as a skill folder, then map the six role files
to opencode agents using your project's agent configuration. Keep
`D Research Ultra Orchestrator` as the primary/main agent behavior and
allow task delegation only to the six `D Research ...` workers listed in
`agents/manifest.json`.

### Other Agent Runtimes

Use the same portable roster:

1. Read `agents/manifest.json`.
2. Create/register each worker from its role file.
3. Use `agents/orchestrator.md` as the main-agent playbook.
4. Map dispatch/poll/result handling to the host runtime's native
   worker mechanism.

The core skill never requires a specific command name.

### No Worker Support

If the host cannot run real worker agents, install only the skill folder.
The Main Research Agent will run the D Research core workflow and apply
the worker checklists manually when needed.

## Optional Tooling Setup

For the Node helpers:

```bash
npm ci
npx playwright install chromium
```

For the Python helpers:

```bash
python --version
```

The bundled Python scripts are stdlib-first. Optional extras are listed
in `pyproject.toml` for embeddings, translation, and extraction features.

## Verification

Run the full offline self-test chain:

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

CI runs the same core checks on pull requests and pushes.

## Runtime Contract

D Research Ultra expects host adapters to support as many of these
capabilities as possible:

- list configured workers
- install/register bundled worker definitions
- dispatch a task to a named worker
- run independent workers in parallel
- read final worker outputs
- restrict worker tools and permissions

If a host lacks worker support, the main agent runs the D Research core
workflow and applies the same role checklists manually.

See `agents/spawn-contract.md` for the adapter contract and
`agents/manifest.json` for canonical role metadata.

## Safety

D Research Ultra is read-only and public-source first. It must not
bypass login walls, paywalls, captchas, anti-bot systems, robots
restrictions, rate limits, private groups, private profiles, or access
controls.

For person-related work, it only supports lawful public-role research.
It refuses doxxing, stalking, harassment, deanonymization, private data,
or sensitive personal-data aggregation.

## Versioning

The Ultra version tracks the bundled D Research core version with an
Ultra suffix. Example: `3.1.0-ultra.1`.

The Python metadata uses PEP 440 local-version syntax
(`3.1.0+ultra.1`) while npm and the skill manifest use SemVer
prerelease syntax (`3.1.0-ultra.1`).
