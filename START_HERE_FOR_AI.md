# START HERE FOR AI

Before planning, building, auditing, validating, or modifying this repo, every AI agent must read:

1. `WORKBOOK_OS_MANIFEST.json`
2. `AI_WORKBOOK_INDEX.md`

## Operating rules

- Treat workbook files as command artifacts, not passive attachments.
- Use `source_truth_rank` to decide which workbook controls a task.
- Treat `HIGHEST_REPO_CEILING_ALL_IN_ONE` as the parent and master repo-ceiling workbook.
- Treat `FRONTEND_CEILING_WORKBOOK` as `support/frontend_primary`.
- Treat `BACKEND_CEILING_WORKBOOK` as `support/backend_primary` once installed.
- Never claim production readiness from workbook presence alone.
- Never push to `main` without operator approval.
- Never deploy production without explicit approval and receipts.
- Never expose secrets.
- Always create or update receipts for installs, validations, and source-truth changes.
- Always state `VERIFIED`, `INFERRED`, `COULD NOT VERIFY`, `BLOCKERS`, `WORKAROUNDS`, and `NEXT ACTIONS`.

## Workbook precedence

- The highest repo ceiling all-in-one workbook governs repo-wide source truth, governance, Codex/Base44 handoff, Vercel/Supabase planning, connector governance, receipts, and release gates.
- The frontend ceiling workbook governs frontend planning, UI, components, responsive rules, design tokens, accessibility, performance, forms, and frontend data contracts.
- The backend ceiling workbook governs backend, API, Supabase, RLS, auth, queues, database, storage, server routes, and environment rules.

