# Workbook Governance

## Mission
Govern the Intelligence Cube workbook as a command and control artifact for Strategic Minds planning, intelligence, dashboards, manifests, and receipts.

## Locked Flow
PLAN -> DISCOVERY -> DOCS -> BRANCH IMPLEMENTATION -> VALIDATION -> RECEIPTS -> APPROVAL.

## Default Allowed Work
- Read repo docs and workbook metadata.
- Create branch-only docs and receipts.
- Generate dashboard specs, queues, manifests, and validation plans.
- Prepare implementation packets for AUTO_BUILDER-V1.

## Approval Gate
Changes outside branch-only documentation require a specific current-session approval from Jeremy.

## Workbook Release Rules
Every workbook release must include:
1. Version ID.
2. Source repo and branch.
3. Related AUTO_BUILDER-V1 execution target.
4. Validation state.
5. Receipt path.
6. Known blockers.
7. Next approval gate.

## Required Labels
- VERIFIED
- INFERRED
- COULD_NOT_VERIFY
- BLOCKER
- WORKAROUND
- NEXT_ACTION

## Dashboard Governance
The dashboard must display queue state, receipt state, validation state, blocker state, and priority lanes before any release is considered ready.
