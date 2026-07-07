# Connector Install Status

Status snapshot for the workbook-first Intelligence Cube repo.

## Current state
- Active workbook path declared in `WORKBOOK_OS_MANIFEST.json`.
- Required connector sheets are defined in the manifest.
- Workbook binary upload must exist in the repository before the status can move to `validated`.

## Required workbook sheets
- `13A_CONNECTOR_REGISTRY`
- `13B_CONNECTOR_CONTRACTS`
- `13C_CONNECTOR_RUN_LOG`
- `13D_CONNECTOR_INSTALL_MAP`

## Status values
- `pending_binary_upload_verification`
- `uploaded_pending_validation`
- `validated`

## Validation rule
The status may only move to `validated` after the workbook file exists at the manifest path and the workbook contains every required connector sheet.
