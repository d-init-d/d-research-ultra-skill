# Ephemeral-First Worker Orchestration

v3.1.2 Release Notes

D Research Ultra v3.1.2 makes dynamic, task-scoped workers the default
multi-agent execution model. The Main Research Agent now prefers ephemeral
workers that exist only for the active task, runs independent roles in parallel
when the host supports it, preserves the same dependency graph sequentially
when it does not, and applies the bundled role checklists manually when no real
worker mechanism is available.

Persistent worker registration remains supported as an optional optimization,
but it is no longer part of normal installation or execution. Ultra creates
reusable agent definitions only when the user explicitly requests them and
confirms the target scope.

## What's New

- The canonical dispatch order is now ephemeral parallel workers, ephemeral
  sequential workers, then manual role checklists in the main context.
- Dynamic workers are explicitly session- or task-scoped. They may work on the
  current project without becoming persistent project agents or writing agent
  configuration files.
- Persistent registration requires explicit user intent and scope confirmation.
  Installing or invoking D Research Ultra alone does not authorize persistent
  agent creation at any scope.
- `agents/manifest.json` now exposes a machine-readable worker lifecycle policy
  for runtime adapters.
- A new `contract:check` validates aligned release metadata, the six canonical
  role files, and the ephemeral-first lifecycle as part of the full CI
  self-test.
- Worker model behavior is runtime-neutral: workers inherit the host default
  unless the user or runtime configuration explicitly selects another model.
- Claude Code, opencode, Minimax, Codex, private CLI, and generic runtime
  guidance now follows the same ephemeral-first lifecycle.

## Why It Matters

Ultra should be installable once and usable immediately without creating six
persistent agent definitions in every project. Ephemeral workers provide the
same role separation and parallel research workflow while keeping project
configuration clean and avoiding accidental global installation.

The new contract also removes an important ambiguity: operating on files in the
current project does not make a dynamic worker a project-level agent. Project
or user scope exists only when a runtime writes or registers a reusable agent
definition.

## Compatibility

- The bundled D Research core remains v3.1.1.
- The six worker roles and their canonical IDs are unchanged.
- Fast, standard, and completeness-first modes are unchanged.
- Execution waves and dependency ordering are unchanged.
- No new mandatory dependencies.
- No evidence-ledger schema changes.
- No helper-script CLI changes.
- Existing persistent workers remain compatible when users choose to use them.

## Upgrade Notes

No research workflow migration is required. Runtime adapters should stop
registering workers automatically and should implement ephemeral dispatch as
the default path. Adapters may continue to offer persistent registration, but
must request explicit user approval and scope selection before writing reusable
agent definitions.
