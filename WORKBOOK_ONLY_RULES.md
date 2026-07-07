# Workbook Only Rules

1. Workbooks are the command artifacts.
2. Repo files are support artifacts only unless referenced by a workbook.
3. Every app or system must have a project-specific child workbook.
4. Child workbooks must include frontend, backend, repo/runtime, assets, tools, skills, prompts, automation, marketing, validation, receipts, blockers, rollback, and approval gates unless technically impossible.
5. If something cannot live inside the workbook, the workbook must store the reference path, storage target, prompt, expected output, validation rule, receipt requirement, and blocker if missing.
6. Actual secrets are forbidden in workbooks and repos.
7. Production, payments, customer messages, spend, destructive actions, and public publishing require explicit operator approval.

## GPT startup requirement

Every GPT must read the manifest, master workbook, latest index workbook, relevant child workbook, receipts, and blockers before acting.

## Codex requirement

Codex may implement only approved branch/preview tasks from a workbook or issue. Codex must not push to main or deploy production without approval.
