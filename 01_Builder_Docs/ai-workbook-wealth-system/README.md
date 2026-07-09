# AI Workbook Wealth System Install

## Purpose
This folder installs the AI Workbook Wealth System production workbook library into INTELLIGENCE-CUBE as a governed workbook-first intelligence asset.

## Contents
- `AI_WORKBOOK_WEALTH_SYSTEM_PRODUCTION_LIBRARY.zip` - full 10-workbook library package plus receipts.
- `AI_WORKBOOK_WEALTH_SYSTEM_MASTER_INDEX.xlsx` - master index workbook.
- `INSTALL_MANIFEST.json` - file hashes, governance mode, validation status, and review gate.

## Governance
- Branch install only.
- No secrets.
- No production deployment.
- No live customer messages.
- No payments or spend.
- Merge requires operator review.

## Required validation before merge
1. Download the ZIP from this branch.
2. Compare SHA-256 hashes against `INSTALL_MANIFEST.json`.
3. Open the master index workbook and at least one category workbook.
4. Confirm source ledger, scorecard, validation, and audit receipt sheets are present.
5. Keep production locked unless current-market claims are web-verified.

## Receipt
Installed by AUTO BUILDER OS as validator/orchestrator into a review branch for INTELLIGENCE-CUBE.
