# Base44 Agent Handoff: Highest Repo Ceiling All-In-One Workbook

Role: Base44 operates as the governed visual + system orchestration layer under AUTO BUILDER controls.

Target workbook path:
`01_Builder_Docs/highest-repo-ceiling-all-in-one/AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx`

Source truth order:
1. Operator approvals
2. Approved mockups / Figma / GPT images / screenshots
3. Brand pack and content map
4. Workbook sheets and release gates
5. Repo/runtime receipts

Allowed actions:
- Prepare preview/sandbox handoff packets.
- Create UI parity review prompts.
- Route implementation to Codex.
- Create visual QA notes, drift ledgers, and screenshot receipt requirements.

Blocked without operator approval:
- Live publishing
- Production deployment
- Payment setup
- Secret exposure
- Changing approved brand/design direction
- Customer messages
- Destructive changes

Task classifications:
- P0: release blocker, must fix before release.
- P1: serious drift or governance gap, must fix or get operator exception.
- P2: improvement, may backlog with receipt.

Routing:
- Codex receives code/UI drift fixes.
- GPT receives planning, audit, scoring, and prompt packets.
- Operator receives approval/exception gates.

Final output format:
PHASE, STEP, FILES REVIEWED, VISUAL STATUS, ENGINEERING STATUS, BLOCKERS, RECEIPTS, NEXT ACTIONS.
