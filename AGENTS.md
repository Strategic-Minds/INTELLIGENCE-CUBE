# AGENTS.md

## Project law
This repo is workbook-first. Read `WORKBOOK_OS_MANIFEST.json` and the active workbook before edits.

## Codex rules
- Work on feature branch only.
- Do not push directly to main.
- Do not deploy production.
- Do not store secrets.
- Update receipts for every change.
- If workbook binary or required sheet is missing, create a blocker instead of guessing.

## Required validation
Run manifest, workbook binary, connector sheet, public safety, dashboard scaffold, and Playwright checks before PR readiness.
