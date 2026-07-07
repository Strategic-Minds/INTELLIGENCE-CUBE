# GPT Business Implementation Plan

## Purpose
Define the approved bridge for GPT-driven business workflows in a workbook-first repo.

## Allowed scope
- Workbook-driven routing and approvals
- Connector registry and contract references
- Receipt logging for every automation step
- Validation before any branch or release action

## Disallowed scope
- Live credentials in repo or workbook
- Unapproved production actions
- Spending, publishing, or customer communication without explicit approval

## Operational sequence
1. Read the active master workbook.
2. Confirm the connector registry entry.
3. Confirm the connector contract and approval gate.
4. Record the planned action in the connector run log.
5. Execute only if the workbook and repo rules allow it.
6. Create a receipt after the action.

## Business capability areas
- Research and intake
- Planning and routing
- Connector governance
- Validation and receipts
- Review and escalation
