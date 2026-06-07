# Runtime-Neutral Spawn Contract

D Research Ultra ships portable role definitions. A host CLI or agent
runtime decides how those roles become real workers.

This file defines the behavior contract that adapters should satisfy.
It intentionally avoids vendor-specific command names.

## Capabilities

An ideal host supports:

1. `run_ephemeral_worker`: start a task-scoped worker from a role prompt.
2. `run_parallel`: dispatch independent ephemeral workers concurrently.
3. `read_worker_result`: collect final worker output.
4. `restrict_tools`: give workers read-only or scoped permissions.
5. `list_workers`: optionally discover user-selected persistent workers.
6. `install_worker`: optionally register a persistent worker after
   explicit user approval.

D Research Ultra still works when only sequential ephemeral dispatch is
available. If no real worker mechanism exists, use single-agent fallback.

## Default Worker Lifecycle

Workers are ephemeral by default:

- initialize each worker from the matching role file
- provide only task-local context and required upstream results
- run independent roles in parallel when possible
- otherwise run them sequentially in dependency order
- collect the final structured result
- allow the worker session to end without writing persistent agent files

Worker system prompts come from each role file's `## System Prompt`
block. Descriptions and personas come from the `## Description` and
`## Persona` sections.

Working inside a project does not make an ephemeral worker a
project-scoped installation. A worker becomes persistent only when the
host writes or registers a reusable agent definition.

## Persistent Registration

Persistent registration is optional and never the default installation
path. Create persistent workers only when the user explicitly asks for
reusable agents and selects or confirms the host scope.

Adapters that support persistent registration should:

- explain the available scopes before writing files or configuration
- request approval for the selected scope
- read `agents/manifest.json` and register only the requested roles
- make installation idempotent using canonical role IDs or names
- document where definitions were written and how to remove them

Installing the Ultra skill does not itself authorize creation of
persistent worker definitions.

## Dispatch Behavior

Ephemeral dispatch should initialize the worker from its role file, then
include only task-local context, required upstream results, and the
role-specific request. Do not paste unrelated role files into a worker.

When the user has already selected a compatible persistent worker, the
adapter may dispatch to it without repeating its stored system prompt.

Workers must return compact, structured outputs. The Main Research
Agent is responsible for final synthesis and final user-facing wording.

Workers inherit the host's default model unless the user or runtime
configuration explicitly selects another model. Adapters must not assume
that every host uses the main session's exact model.

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

- whether ephemeral workers are supported
- whether parallel dispatch is supported
- which model-selection behavior the host uses
- where persistent worker definitions are installed, if the user opts in
- how users invoke the orchestrator
- how the adapter maps role IDs to host worker names
- which worker capabilities are unsupported
- how to uninstall or update persistent workers, if applicable
