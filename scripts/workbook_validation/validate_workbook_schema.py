from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

MANIFEST = Path('WORKBOOK_OS_MANIFEST.json')
EXPECTED = {
    '13A_CONNECTOR_REGISTRY',
    '13B_CONNECTOR_CONTRACTS',
    '13C_CONNECTOR_RUN_LOG',
    '13D_CONNECTOR_INSTALL_MAP',
}


def workbook_sheet_names(workbook_path: Path) -> list[str]:
    with zipfile.ZipFile(workbook_path) as zf:
        workbook_xml = ET.fromstring(zf.read('xl/workbook.xml'))
        ns = {'main': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
        return [sheet.attrib['name'] for sheet in workbook_xml.findall('main:sheets/main:sheet', ns)]


def main() -> None:
    if not MANIFEST.exists():
        raise SystemExit('manifest missing')
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    workbook_path = Path(manifest['active_master_workbook'])
    if not workbook_path.exists():
        raise SystemExit(f'active workbook missing: {workbook_path}')
    sheet_names = set(workbook_sheet_names(workbook_path))
    missing = sorted(EXPECTED - sheet_names)
    if missing:
      raise SystemExit(f'missing workbook sheets: {", ".join(missing)}')
    if not re.search(r'CONNECTOR', ' '.join(sheet_names), re.I):
      raise SystemExit('connector workbook expected but not found')
    print('workbook schema ok')


if __name__ == '__main__':
    main()
