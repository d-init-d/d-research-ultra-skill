# D Research Ultra Worker Roles

These files define the six bundled D Research Ultra worker roles. They
are portable role definitions, not runtime-specific agent configs.

Each role file contains:

- `## Description`
- `## Persona`
- `## System Prompt`

Installers and runtime adapters should read those sections and translate
them into the host's native worker-agent format.

## Canonical Roles

| Role ID | Role file | Worker name |
|---|---|---|
| `source-mapper` | `source-mapper.md` | `D Research Source Mapper` |
| `recall-auditor` | `recall-auditor.md` | `D Research Recall Auditor` |
| `public-web-community-hunter` | `public-web-community-hunter.md` | `D Research Public Web & Community Hunter` |
| `data-extractor` | `data-extractor.md` | `D Research Data Extractor` |
| `evidence-verifier` | `evidence-verifier.md` | `D Research Evidence Verifier` |
| `report-synthesizer` | `report-synthesizer.md` | `D Research Report Synthesizer` |

`agents/manifest.json` is the source of truth for role IDs, names,
files, and execution waves.

## Loading Rule

The Main Research Agent does not need to read every role file during
normal dispatch. A configured worker already has its system prompt.
For normal pipeline runs, the main agent uses `agents/orchestrator.md`
and `agents/manifest.json` to compose compact task prompts.

Read a role file only when:

- installing/registering that worker in a host runtime
- running a worker directly from the role file
- maintaining or reviewing the role definition itself

## Persona Conventions

- Source Mapper: "Recalls every reachable, lawful, public source before anyone else writes a word."
- Recall Auditor: "Adversarial second-pass hunter; finds what the first pass missed."
- Public Web & Community Hunter: "Lawful public web/community source specialist with strict privacy and identity discipline."
- Data Extractor: "Turns accessible public sources into clean, auditable structured data."
- Evidence Verifier: "Claims in. Sources checked. Confidence out."
- Report Synthesizer: "Verified findings into source-backed reports, no overclaim."
