# Prebuilt Multi-Agent Research System

v3.1.1 Release Notes

D Research Ultra v3.1.1 is the first public-ready Ultra release. It is
developed from the core
[D Research Skill](https://github.com/d-init-d/d-research-skill) v3.1.1 and
packages the same browser-first research methodology as a ready-to-register
multi-agent system.

The release keeps `SKILL.md` runtime-neutral while adding an Ultra orchestration
layer, six portable worker roles, install guidance for common agent hosts, CI,
license metadata, and product-grade documentation.

## What's New

- D Research Ultra now shares the public `3.1.1` version line with the bundled
  D Research core release. Package metadata, Python metadata, and the Ultra
  manifest all report version `3.1.1`.
- The package includes a runtime-neutral Main Research Agent, spawn contract,
  canonical role manifest, and six ready-to-register worker roles:
  Source Mapper, Public Web & Community Hunter, Recall Auditor, Data Extractor,
  Evidence Verifier, and Report Synthesizer.
- `README.md` presents Ultra as the prebuilt companion to the core D Research
  Skill, with clear positioning, repository layout, role roster, host
  installation recipes, safety boundaries, CI status, and license information.
- Runtime-specific guidance lives in README documentation only. The skill
  entrypoint and role files remain portable across Minimax Code, Claude Code,
  opencode, Codex, and private agent runtimes.
- CI and local validation cover internal references, decision-tree reachability,
  Node script syntax, metadata self-tests, and release hygiene.

## Why It Matters

D Research core is the flexible methodology layer for builders who want to
design their own agent system. D Research Ultra is the ready-made distribution
for teams that want the same research discipline with a prebuilt worker roster
and orchestration contract.

Using the same `3.1.1` release number as core makes the relationship clear:
Ultra is not a vendor-specific fork and does not need a separate prerelease
suffix. It is the prebuilt multi-agent package for the matching D Research core
version.

## Compatibility

- No vendor-specific runtime is required.
- No new mandatory dependencies.
- No evidence-ledger schema changes from the bundled core methodology.
- No script CLI changes from the bundled helper surface.
- Host runtimes may map the role files to native subagents, workers, tasks, or
  background jobs.
- If a host has no real worker mechanism, the main agent can still run the same
  gates manually and disclose that fallback.

## Upgrade Notes

Install v3.1.1 if you want the public-ready Ultra package aligned with the core
D Research v3.1.1 release. Existing local Ultra drafts that used an `ultra`
version suffix should update package metadata and manifests to `3.1.1`; no
research workflow migration is required.
