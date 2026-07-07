from __future__ import annotations

import json
import zipfile
from pathlib import Path

MANIFEST = Path('WORKBOOK_OS_MANIFEST.json')


def main() -> None:
    if not MANIFEST.exists():
        raise SystemExit('manifest missing')
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    workbook = Path(manifest['active_master_workbook'])
    if not workbook.exists():
        raise SystemExit(f'active workbook missing: {workbook}')
    required = set(manifest.get('connector_governance', {}).get('required_sheets', []))
    with zipfile.ZipFile(workbook) as zf:
        sheet_names = set()
        for name in zf.namelist():
            if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'):
                sheet_names.add(name)
        workbook_xml = zf.read('xl/workbook.xml').decode('utf-8', errors='ignore')
        missing = [sheet for sheet in required if sheet not in workbook_xml]
        if missing:
            raise SystemExit(f'missing required connector sheets: {", ".join(sorted(missing))}')
    print('connector sheets ok')


if __name__ == '__main__':
    main()
