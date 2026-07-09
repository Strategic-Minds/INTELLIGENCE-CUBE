# Codex Install Prompt: Highest Repo Ceiling All-In-One Workbook

PHASE: DOCS / BUILD HANDOFF

Branch: `codex/install-highest-repo-ceiling-all-in-one-workbook`

Target path:
`01_Builder_Docs/highest-repo-ceiling-all-in-one/AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx`

Rules:
- Do not push to main.
- Do not deploy production.
- Do not expose secrets.
- Do not mark production-ready.
- Do not alter locked release gates without operator approval.

Validation command:

```bash
python 01_Builder_Docs/highest-repo-ceiling-all-in-one/scripts/highest_repo_ceiling_all_in_one_validator.py 01_Builder_Docs/highest-repo-ceiling-all-in-one/AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx
```

Visual/UI requirements:
- Record approved mockup source truth.
- Capture desktop/tablet/mobile screenshots where UI exists.
- Use the visual drift ledger for P0/P1/P2 issues.
- Do not release a UI project with unresolved P0/P1 visual drift.

Receipt paths:
- `03_Bridge_Receipts/validation/RECEIPT_VALIDATE_HIGHEST_REPO_CEILING_ALL_IN_ONE.md`
- `03_Bridge_Receipts/visual/VISUAL_PARITY_REPORT.md`
- `03_Bridge_Receipts/rollback/ROLLBACK_VISUAL_PARITY.md`

Final output must include:
VERIFIED, INFERRED, COULD NOT VERIFY, BLOCKERS, WORKAROUNDS, NEXT ACTIONS.
