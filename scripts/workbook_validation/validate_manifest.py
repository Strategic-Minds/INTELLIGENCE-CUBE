from __future__ import annotations

import json
from pathlib import Path

MANIFEST = Path('WORKBOOK_OS_MANIFEST.json')
REQUIRED_KEYS = ['repo', 'active_master_workbook', 'connector_governance']
REQUIRED_SHEETS = {
    '13A_CONNECTOR_REGISTRY',
    '13B_CONNECTOR_CONTRACTS',
    '13C_CONNECTOR_RUN_LOG',
    '13D_CONNECTOR_INSTALL_MAP',
}


def main() -> None:
    if not MANIFEST.exists():
        raise SystemExit('manifest missing: WORKBOOK_OS_MANIFEST.json')
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    for key in REQUIRED_KEYS:
        if key not in manifest:
            raise SystemExit(f'missing manifest key: {key}')
    gov = manifest['connector_governance']
    if not gov.get('enabled'):
        raise SystemExit('connector governance must be enabled')
    sheets = set(gov.get('required_sheets', []))
    missing = sorted(REQUIRED_SHEETS - sheets)
    if missing:
        raise SystemExit(f'missing required sheets in manifest: {", ".join(missing)}')
    active = Path(manifest['active_master_workbook'])
    if not active.exists():
        raise SystemExit(f'active workbook missing at path: {active}')
    print('manifest ok')


if __name__ == '__main__':
    main()
