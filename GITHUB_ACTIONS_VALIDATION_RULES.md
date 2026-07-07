# GitHub Actions Validation Rules

Workflow files in this repo support workbook operations only.

Planned validations:

1. workbook-schema-check.yml: verify required workbook folders and manifest references exist.
2. workbook-index-refresh.yml: validate workbook index metadata.
3. workbook-naming-check.yml: enforce workbook naming rules.
4. receipt-required-check.yml: require receipt updates when scaffold or workbook folders change.
5. child-workbook-completeness-check.yml: verify child workbook metadata claims include frontend, backend, tools, skills, assets, prompts, automation, validation, receipts, blockers, and rollback.
6. asset-reference-check.yml: ensure assets and web packs have workbook references.
7. security-boundary-check.yml: check public-repo safety boundaries.

Workflows are not considered live until committed, run, and receipts are created.
