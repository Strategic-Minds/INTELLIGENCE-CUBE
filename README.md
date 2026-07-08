# INTELLIGENCE-CUBE

## AUTO BUILDER Workbook-Only Operating Repo

This repository is the workbook-first command center for the AUTO BUILDER Intelligence Cube system.

**Primary rule:** the workbook is the command artifact. Markdown, YAML, scripts, images, prompts, and repo folders are support artifacts only unless a workbook explicitly points to them.

## Start here

Every GPT, Codex agent, GitHub Action, Vercel workflow, Vercel cron, Base44 handoff, or human operator must begin with:

1. `WORKBOOK_ONLY_RULES.md`
2. `WORKBOOK_OS_MANIFEST.json`
3. `GPT_REHYDRATE_START_HERE.md`
4. the latest workbook index in `01_WORKBOOK_INDEX/current/`
5. the master workbook in `00_MASTER_WORKBOOK/current/`
6. the relevant child workbook
7. current receipts and blockers in `10_VALIDATION_RECEIPTS_ROLLBACK/`

## Public repo warning

This repo is public. Do not commit secrets, credentials, private customer data, payment keys, service-role keys, passwords, API tokens, or private business data. Store secret values only in approved secret managers and reference secret names only.

## Required workflow

PLAN -> DISCOVERY -> WORKBOOK -> APPROVAL -> CODEX/BRANCH -> VALIDATE -> RECEIPTS -> RELEASE GATE

Do not push production changes, send customer messages, process payments, spend money, or mutate production without explicit operator approval.
