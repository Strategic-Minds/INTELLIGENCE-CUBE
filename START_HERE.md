# START_HERE

Read this first on every Codex or GPT run.

## Source of truth order
1. [`WORKBOOK_OS_MANIFEST.json`](./WORKBOOK_OS_MANIFEST.json)
2. [`01_WORKBOOK_INDEX/current/`](./01_WORKBOOK_INDEX/current)
3. [`00_MASTER_WORKBOOK/current/`](./00_MASTER_WORKBOOK/current)
4. [`10_VALIDATION_RECEIPTS_ROLLBACK/`](./10_VALIDATION_RECEIPTS_ROLLBACK)
5. [`BLOCKERS.md`](./BLOCKERS.md)
6. relevant support docs and scripts

## Safety rules
- Work branch-safe only.
- Do not mutate `main`.
- Do not deploy production.
- Do not store secrets in repo files.
- Do not claim success without receipts.
- If a workbook directive conflicts with repo scaffolding, the workbook wins.

## First actions
- Inspect the workbook and manifest.
- Print the current branch, files inspected, blockers, and next action.
- Validate workbook paths before edits.
- Update receipts for every meaningful change.

## Current highest-state focus
- workbook truthfulness
- validation coverage
- governed autonomy
- public-repo safety
- mobile command cockpit quality
