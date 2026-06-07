---
name: "testing-scripts"
description: "Use when editing D Research Ultra helper scripts, references, package metadata, CI, or internal links. Runs the focused checks that protect script syntax, internal references, self-tests, and local artifact hygiene."
---

# Testing Scripts

Use this maintainer skill after editing scripts, references, examples,
templates, package metadata, or CI files in D Research Ultra.

## Quick Checks

Run focused checks first:

```bash
npm run refs:check
npm run refs:check:decision-tree
npm run contract:check
node scripts/run_python.mjs scripts/check_node_syntax.py
node scripts/run_python.mjs scripts/check_no_plan_files.py
node scripts/run_python.mjs scripts/run_metadata.py self-test
```

## Full Check

Run the full offline self-test chain before release:

```bash
npm run self-test
```

If Playwright is not installed locally:

```bash
npm ci
npx playwright install chromium
```

## Pass Criteria

- Every command exits with status 0.
- `refs:check` prints that all backticked internal refs resolve.
- `refs:check:decision-tree` confirms reference reachability.
- `contract:check` confirms aligned release metadata, six valid role
  files, and the ephemeral-first lifecycle policy.
- Node syntax checks every `.mjs` file.
- No `PLAN-*.md` local roadmap files are present.
- The full self-test chain ends without failures.

## Failure Triage

- Broken internal refs: update the path or restore the referenced file.
- Node syntax failure: run the printed `node --check <file>` command
  after patching.
- Missing Python on Windows: use Python on PATH, Python launcher, or a
  runtime-provided Python executable.
- Playwright failure: run `npm ci` and `npx playwright install chromium`.
