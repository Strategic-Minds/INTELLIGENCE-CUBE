# Workbook Upload Guide

This folder is safe for branch-scoped workbook uploads.

## Intended use

Use the branch-safe upload script when a workspace needs to copy workbook artifacts into this repo without targeting `main`.

## Script

```bash
python scripts/workbook_upload_branch_safe.py \
  --source-dir "C:/path/to/workspace/artifacts" \
  --destination-dir "01_Builder_Docs/highest-repo-ceiling-all-in-one" \
  --files AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_PACKAGE.zip \
  --validate-command "python 01_Builder_Docs/highest-repo-ceiling-all-in-one/scripts/highest_repo_ceiling_all_in_one_validator.py 01_Builder_Docs/highest-repo-ceiling-all-in-one/AUTO_BUILDER_HIGHEST_REPO_CEILING_ALL_IN_ONE_WORKBOOK.xlsx"
```

## Optional push

Add `--push` only when you intend to commit and push on the current branch.

## Safety rules

- Do not use `main`.
- Do not deploy production.
- Do not expose secrets.
- Do not write outside the repo root.
