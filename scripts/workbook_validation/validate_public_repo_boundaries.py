from __future__ import annotations

import re
from pathlib import Path

PATTERNS = [
    r'BEGIN PRIVATE KEY',
    r'\bapi[_-]?key\b\s*[:=]',
    r'\bpassword\b\s*[:=]',
    r'\bsecret\b\s*[:=]',
]
SKIP_SUFFIXES = {'.xlsx', '.png', '.jpg', '.jpeg', '.zip', '.gif', '.pdf'}
SKIP_PREFIXES = ('scripts/workbook_validation/', 'dashboard/.next/', '.git/')


def main() -> None:
    bad: list[str] = []
    for path in Path('.').rglob('*'):
        if not path.is_file() or path.suffix.lower() in SKIP_SUFFIXES:
            continue
        rel = path.as_posix()
        if any(rel.startswith(prefix) for prefix in SKIP_PREFIXES):
            continue
        text = path.read_text(encoding='utf-8', errors='ignore')
        for pat in PATTERNS:
            if re.search(pat, text, re.IGNORECASE):
                bad.append(rel)
                break
    if bad:
        raise SystemExit('possible sensitive patterns: ' + ', '.join(sorted(set(bad))[:20]))
    print('public safety ok')


if __name__ == '__main__':
    main()
