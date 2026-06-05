# D Research Ultra Agents

This directory contains the runtime-neutral multi-agent layer for D
Research Ultra.

The current chat agent is the Main Research Agent. It performs intake,
chooses execution depth, dispatches worker roles when the host runtime
supports real subagents/tasks, merges returned evidence, applies final
gates, and writes the final source-backed answer.

There is no vendor-specific command in this layer. Host-specific
installers or adapters should translate these portable role definitions
into the local agent format.

## Files

| File | Purpose |
|---|---|
| `manifest.json` | Canonical role IDs, names, descriptions, files, and execution waves. Use this as the source of truth for adapters/installers. |
| `spawn-contract.md` | Runtime-neutral contract for discovering, installing, dispatching, polling, and falling back from worker agents. |
| `orchestrator.md` | Main Research Agent playbook for intake, wave planning, dispatch prompts, merging, and fallback. |
| `subagent-roles/*.md` | Portable worker role definitions. Each file contains description, persona, and a system-prompt block. |
| `main-expert-instructions.md` | Historical upstream expert reference. Read only when doing meta-maintenance or recovering canonical wording; normal runs use `orchestrator.md`. |

## Base Roster

| Role ID | Worker name | Role file |
|---|---|---|
| `source-mapper` | `D Research Source Mapper` | `subagent-roles/source-mapper.md` |
| `recall-auditor` | `D Research Recall Auditor` | `subagent-roles/recall-auditor.md` |
| `public-web-community-hunter` | `D Research Public Web & Community Hunter` | `subagent-roles/public-web-community-hunter.md` |
| `data-extractor` | `D Research Data Extractor` | `subagent-roles/data-extractor.md` |
| `evidence-verifier` | `D Research Evidence Verifier` | `subagent-roles/evidence-verifier.md` |
| `report-synthesizer` | `D Research Report Synthesizer` | `subagent-roles/report-synthesizer.md` |

## Loading Discipline

For normal research runs, load:

1. `SKILL.md`
2. `AGENTS.md`
3. `agents/orchestrator.md` if multi-agent mode is possible
4. `agents/spawn-contract.md` when mapping to a runtime
5. Role files only when installing/registering workers or when a worker
   itself starts with that role prompt

Do not re-read all role files on every dispatch. The manifest and
orchestrator contain enough information to compose task prompts. The
role files are full system prompts for worker configuration, not
general reference manuals.
