# RELEASE_GATE

## Release gate
This repository only moves forward when:
- the active workbook exists at the manifest path
- required connector sheets validate
- workbook uploads validate
- public repo safety passes
- build passes
- smoke tests pass
- receipts exist for the work performed

## Release blockers
- no approval for production deploy
- missing receipt
- missing rollback path
- secret or credential leak
- unsafe scraper or unguarded external action

## Branch rule
This repo is branch-safe only unless the operator explicitly approves a release action.
