# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and this project uses Semantic Versioning. The Ultra release version describes
the prebuilt product surface; `agents/manifest.json` records the bundled core
version separately.

## [Unreleased]

## [3.1.2] - 2026-06-07

### Changed

- Made ephemeral, task-scoped workers the default execution model.
- Defined the runtime fallback order as ephemeral parallel workers,
  ephemeral sequential workers, then manual role checklists.
- Made persistent worker registration an explicit user opt-in instead
  of part of normal skill installation or execution.
- Clarified that dynamic workers may operate on the current project
  without becoming persistent project agents.
- Added host-default model inheritance guidance without assuming that
  every runtime uses the main session's exact model.
- Updated Claude Code, opencode, Minimax, Codex, and generic runtime
  recipes to match the ephemeral-first contract.
- Added machine-readable worker lifecycle policy to
  `agents/manifest.json`.
- Added `contract:check` to keep release metadata, role files, and the
  ephemeral-first lifecycle aligned in CI.

### Compatibility

- The six role definitions, execution waves, research workflow,
  evidence model, script interfaces, and bundled D Research core v3.1.1
  remain unchanged.
- Existing persistent workers remain usable when the user selects them;
  this release only stops treating registration as the default path.

## [3.1.1] - 2026-06-05

### Added

- Created D Research Ultra as the prebuilt multi-agent distribution of
  D Research v3.1.1.
- Added a runtime-neutral Ultra layer:
  - `agents/manifest.json`
  - `agents/spawn-contract.md`
  - `agents/orchestrator.md`
  - six portable worker role files under `agents/subagent-roles/`
- Added execution modes for fast, standard, and completeness-first work.
- Added the wave-based completeness-first pipeline:
  1. Source Mapper + Public Web & Community Hunter
  2. Recall Auditor + Data Extractor
  3. Evidence Verifier
  4. Report Synthesizer
- Added a standalone README for the Ultra package.

### Changed

- Reframed the package as runtime-neutral. Core instructions no longer
  require a specific CLI, command name, or vendor agent API.
- Renamed the previous public-social worker to
  `Public Web & Community Hunter` to keep the base preset broad,
  lawful, and less niche.
- Rewrote `SKILL.md`, `AGENTS.md`, and the orchestrator playbook around
  a generic host-runtime spawn contract.
- Replaced the previous main-expert backup file with a compact portable
  Main Research Agent reference.

### Notes

- D Research Ultra bundles the D Research core methodology and can be
  installed alone.
- Host adapters may translate the portable role files into their own
  subagent/task/worker format.
- If a runtime has no real worker mechanism, the main agent still runs
  the D Research core workflow and manually applies the role checklists.
