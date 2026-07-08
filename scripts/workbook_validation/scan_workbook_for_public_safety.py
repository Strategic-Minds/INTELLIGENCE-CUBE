from __future__ import annotations

from pathlib import Path
import json
import zipfile

MANIFEST = Path('WORKBOOK_OS_MANIFEST.json')
FORBIDDEN = ('BEGIN PRIVATE KEY', 'api_key=', 'password=', 'secret=')


def main() -> None:
    if not MANIFEST.exists():
        raise SystemExit('manifest missing')
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    workbook_path = Path(manifest['active_master_workbook'])
    if not workbook_path.exists():
        raise SystemExit(f'active workbook missing: {workbook_path}')
    with zipfile.ZipFile(workbook_path) as zf:
      for name in zf.namelist():
        if not name.endswith('.xml') and not name.endswith('.rels'):
          continue
        data = zf.read(name).decode('utf-8', errors='ignore')
        for token in FORBIDDEN:
          if token.lower() in data.lower():
            raise SystemExit(f'forbidden token found in workbook: {token} in {name}')
    print('workbook safety ok')


if __name__ == '__main__':
    main()
