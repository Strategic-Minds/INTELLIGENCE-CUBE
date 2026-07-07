# Repo Map

## Canonical Roles

| Repo | Role | Status | Notes |
|---|---|---|---|
| Strategic-Minds/INTELLIGENCE-CUBE | Workbook source and intelligence control repo | ACTIVE | Holds workbook docs, manifests, releases, receipts, connector maps, and dashboard specs. |
| Strategic-Minds/AUTO_BUILDER-V1 | Real AUTO BUILDER execution repo | ACTIVE | Holds implementation code, runtime routes, validators, Vercel/Supabase integration plans, and branch-safe execution work. |
| Strategic-Minds/AUTOBUILDER-V2 | Historical reference only | ARCHIVED | Reference content only. Do not treat as live execution source. |

## Artifact Routing

| Artifact Type | Home Repo |
|---|---|
| Master workbook | INTELLIGENCE-CUBE |
| Child workbooks | INTELLIGENCE-CUBE |
| Workbook receipts | INTELLIGENCE-CUBE |
| Dashboard specs | INTELLIGENCE-CUBE first, AUTO_BUILDER-V1 implementation later |
| Runtime routes | AUTO_BUILDER-V1 |
| Validator cron | AUTO_BUILDER-V1 |
| Supabase schema specs | INTELLIGENCE-CUBE docs first, AUTO_BUILDER-V1 implementation later |
| Batch install packs | INTELLIGENCE-CUBE |

## Current Branch
`docs/workbook-canon-source-truth-20260707`

## Next Gate
Use this map before any GPT, Codex, Vercel, or branch implementation action.
