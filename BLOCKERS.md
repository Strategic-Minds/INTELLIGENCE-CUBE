# BLOCKERS

## Open blockers
- Workbook schema and secret-scan coverage still need to be enforced as first-class validators.
- The support modules in `dashboard/lib/` must be fully migrated from scaffold objects to canonical runtime state.
- Browser scraping should remain public-URL only and receive stronger SSRF hardening before broader automation.

## Policy blockers
- Production deploys are blocked without explicit approval.
- Main-branch mutation is blocked.
- Secrets are blocked from the repo.
- Unverified “ready/validated/complete” statuses are blocked.

## Receipt rule
Every blocker closure must leave a receipt in `10_VALIDATION_RECEIPTS_ROLLBACK/`.
