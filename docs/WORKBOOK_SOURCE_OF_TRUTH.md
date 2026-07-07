# Workbook Source of Truth

## Status
ACTIVE CONTROL DOCUMENT

## Purpose
This document defines the canonical source truth for the AUTO BUILDER Intelligence Cube workbook system.

## Canonical Repositories

| Role | Repository | Status | Use |
|---|---|---|---|
| Workbook source repo | Strategic-Minds/INTELLIGENCE-CUBE | ACTIVE | Workbook governance, workbook releases, manifests, receipts, control docs |
| AUTO BUILDER execution repo | Strategic-Minds/AUTO_BUILDER-V1 | ACTIVE | Branch-safe implementation, runtime routes, Vercel cron, Supabase integration, validators |
| Historical v2 reference | Strategic-Minds/AUTOBUILDER-V2 | ARCHIVED_REFERENCE_ONLY | Reference only. Do not use as active execution source. |

## Workbook Authority Order
1. Current Jeremy instruction in the active session.
2. This workbook source truth document.
3. MANIFEST.json and WORKBOOK_INDEX.md.
4. Current patched master workbook release.
5. Current child workbook release.
6. GitHub receipts in receipts/.
7. AUTO_BUILDER-V1 runtime evidence.
8. Drive/Ops Sheet evidence when verified.
9. Historical docs and archived repos.

## Operating Rules
- INTELLIGENCE-CUBE stores workbook/control artifacts.
- AUTO_BUILDER-V1 executes approved branch-safe implementation.
- Workbook releases must include manifest version, date, source, validation state, and receipt reference.
- No workbook may claim live runtime readiness without validation evidence.
- Any unknown live system state must be marked COULD_NOT_VERIFY.

## Required Release Artifacts
- Master workbook file or workbook release pointer.
- Child workbook file or child release pointer.
- Manifest entry.
- Validation receipt.
- Blocker/workaround register entry.
- Repo role mapping.

## Next Gate
Before live automation, verify Vercel project binding, Supabase schema, Drive/Ops Sheet state, and cron health.
