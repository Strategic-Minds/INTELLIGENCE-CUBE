# Blockers and Workarounds

## Known blockers
- Workbook binaries may be absent from the remote branch until uploaded.
- The current GitHub file tools in this session can create UTF-8 text files but cannot upload `.xlsx` binaries.

## Workarounds
- Use Codex local git or the GitHub UI to upload the workbook binaries to the mapped paths.
- Re-run validation after upload.
- Keep the branch blocked from PR readiness until the binary and sheets are verified.

## Exit criteria
- Active master workbook exists at the manifest path.
- Required connector sheets are present.
- Safety and receipt checks pass.
