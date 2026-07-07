# Autonomous Bridge Architecture

## Goal
Connect GPT, Codex, GitHub, Drive, Vercel, Supabase, and browser validation through workbook-governed control flow.

## Control layers
- Workbook: source of truth and approval gate ledger
- Repo: support artifacts, validators, workflows, and receipts
- Runtime: branch automation and preview-only execution
- Validation: workbook, manifest, binary, and safety checks

## Bridge rules
- No direct action without a workbook reference.
- No secret values in public repo files.
- No production deploys from this scaffold branch.
- No connector action without a run-log entry.

## Failure handling
- Missing workbook binary becomes a blocker receipt.
- Missing required sheet fails validation.
- Any suspicious public-safe pattern fails the safety gate.
