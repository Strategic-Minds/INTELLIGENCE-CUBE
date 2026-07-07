from __future__ import annotations

import json
from pathlib import Path

MANIFEST = Path('WORKBOOK_OS_MANIFEST.json')


def main() -> None:
    if not MANIFEST.exists():
        raise SystemExit('manifest missing')
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    workbook = Path(manifest['active_master_workbook'])
    if not workbook.exists():
        raise SystemExit(f'active workbook missing: {workbook}')
    if workbook.suffix.lower() != '.xlsx':
        raise SystemExit(f'active workbook must be .xlsx: {workbook}')
    print('workbook upload ok')


if __name__ == '__main__':
    main()
