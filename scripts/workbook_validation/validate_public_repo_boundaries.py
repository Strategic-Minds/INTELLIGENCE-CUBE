from __future__ import annotations

import re
from pathlib import Path

PATTERNS = [
    r'BEGIN PRIVATE KEY',
    r'api[_-]?key\s*=',
    r'password\s*=',
    r'secret\s*=',
]
SKIP_SUFFIXES = {'.xlsx', '.png', '.jpg', '.jpeg', '.zip', '.gif', '.pdf'}
SKIP_DIRS = {'scripts/workbook_validation'}


def main() -> None:
    bad: list[str] = []
    for path in Path('.').rglob('*'):
        if not path.is_file() or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        if any(skip_dir in path.as_posix() for skip_dir in SKIP_DIRS):
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        for pat in PATTERNS:
            if re.search(pat, text, re.IGNORECASE):
                bad.append(str(path))
                break
    if bad:
        raise SystemExit('possible sensitive patterns: ' + ', '.join(sorted(set(bad))[:20]))
    print('public safety ok')


if __name__ == '__main__':
    main()
