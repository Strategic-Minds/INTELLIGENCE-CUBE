# AI Workbook Index

This is the AI-readable front door for official workbook source truth.

| Workbook ID | Workbook Name | Repo Path | Source Truth Rank | Domain | Status | Read First? | Controls | Validation Evidence | Receipt Path | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HIGHEST_REPO_CEILING_ALL_IN_ONE | AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx | `01_Builder_Docs/highest-repo-ceiling-all-in-one/AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx` | primary/master_repo_ceiling | repo-wide source truth, governance, Codex/Base44 handoff, Vercel/Supabase planning, connector governance, receipts, release gates | installed | yes | parent/master repo ceiling workbook | `01_Builder_Docs/highest-repo-ceiling-all-in-one/VALIDATION_RESULT.txt` and `VALIDATION_SUMMARY.json` | `01_Builder_Docs/highest-repo-ceiling-all-in-one/UPLOAD_RECEIPT.md` | Workbook includes visual parity and release-gate concepts |
| FRONTEND_CEILING_WORKBOOK | AUTO_BUILDER_FRONTEND_CEILING_WORKBOOK.xlsx | `01_Builder_Docs/frontend-ceiling/AUTO_BUILDER_FRONTEND_CEILING_WORKBOOK.xlsx` | support/frontend_primary | frontend planning, UI, components, responsive rules, design tokens, accessibility, performance, forms, frontend data contracts | installed | when task touches frontend/UI/design/pages/components | frontend command ledger | `01_Builder_Docs/frontend-ceiling/README.md` and `03_Bridge_Receipts/frontend/RECEIPT_FRONTEND_CEILING_WORKBOOK_INSTALL.md` | `03_Bridge_Receipts/frontend/RECEIPT_FRONTEND_CEILING_WORKBOOK_INSTALL.md` | Use with the all-in-one ceiling workbook |
| BACKEND_CEILING_WORKBOOK | AUTO_BUILDER_BACKEND_CEILING_WORKBOOK.xlsx | `01_Builder_Docs/backend-ceiling/AUTO_BUILDER_BACKEND_CEILING_WORKBOOK.xlsx` | support/backend_primary | backend, API, Supabase, RLS, auth, queues, database, storage, server routes, environment rules | planned/uninstalled unless already present | when task touches backend/API/database/auth/runtime | backend command ledger | not yet available | not yet available | Reserved for future installation |

## Rules

- Workbooks are command artifacts.
- Do not infer production readiness from the index alone.
- Do not overwrite workbook source truth without operator intent.
- production remains locked until explicit live receipts exist.
