# Runtime-Neutral Spawn Contract

D Research Ultra ships portable role definitions. A host CLI or agent
runtime decides how those roles become real workers.

This file defines the behavior contract that adapters should satisfy.
It intentionally avoids vendor-specific command names.

## Capabilities

An ideal host supports:

1. `list_workers`: return configured worker names/IDs.
2. `install_worker`: register a worker from a bundled role file.
3. `run_worker`: dispatch one task to a named worker.
4. `run_parallel`: dispatch independent workers concurrently.
5. `read_worker_result`: collect final worker output.
6. `restrict_tools`: give workers read-only or scoped permissions.

D Research Ultra still works when only `run_worker` exists. If no real
worker mechanism exists, use single-agent fallback.

## Installation Behavior

Adapters should read `agents/manifest.json` and register the six roles
from `agents/subagent-roles/*.md`.

Ask the user before installing missing workers unless the host's normal
skill installer already asked for permission. Installation should be
idempotent: existing workers with matching canonical role IDs or names
should not be duplicated.

Worker system prompts come from each role file's `## System Prompt`
block. Descriptions and personas come from the `## Description` and
`## Persona` sections.

## Dispatch Behavior

Dispatch prompts should include only task-local context plus the
role-specific request. Do not paste all role files into every dispatch.
Configured workers already have their system prompts.

Workers must return compact, structured outputs. The Main Research
Agent is responsible for final synthesis and final user-facing wording.

## Parallel Behavior

The completeness-first pipeline is a wave graph:

1. Source Mapper and Public Web & Community Hunter.
2. Recall Auditor and Data Extractor.
3. Evidence Verifier.
4. Report Synthesizer.

If a host lacks true parallelism, run each wave sequentially. Preserve
the dependency order.

## Fallback Behavior

If a worker cannot run:

- record the role and failure reason
- run the role checklist manually in the main context
- mark the research trail with `manual_fallback`
- continue only if the evidence standard can still be met

Never simulate a worker silently.

## Adapter Output

Runtime adapters should document:

- where worker definitions are installed
- how users invoke the orchestrator
- how the adapter maps role IDs to host worker names
- which worker capabilities are unsupported
- how to uninstall or update workers
