# CODEX HANDOFF RULES

## Frontend Ceiling Section

The frontend ceiling workbook is the operator ledger for frontend planning and implementation.

It must be used together with the highest repo ceiling all-in-one workbook when the task involves:

- frontend planning
- UI implementation
- component rules
- responsive behavior
- accessibility
- performance
- forms
- frontend data contracts
- Vercel/Next.js runtime planning
- Supabase frontend contracts
- validation
- receipts
- release gates

## Source-truth rule

- `01_Builder_Docs/frontend-ceiling/AUTO_BUILDER_FRONTEND_CEILING_WORKBOOK.xlsx` governs frontend-specific execution.
- `01_Builder_Docs/highest-repo-ceiling-all-in-one/AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx` governs the broader ceiling and release-gate layer.
- Neither workbook should overwrite the other.
- The clean one-shot workbook variant intentionally excludes visual parity and screenshot/design parity rules.

## Safety rules

- Do not push to `main`.
- Do not deploy production.
- Do not expose secrets.
- Do not add live connector actions.

