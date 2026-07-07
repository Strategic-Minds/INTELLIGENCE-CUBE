from __future__ import annotations

from pathlib import Path

ROOTS = [
    Path('00_MASTER_WORKBOOK/current'),
    Path('01_WORKBOOK_INDEX/current'),
    Path('04_SOURCE_ATLAS_WORKBOOKS/internet_sources'),
    Path('05_IDEA_FACTORY_WORKBOOKS/ranked_ideas'),
    Path('06_INTELLIGENCE_OS_WORKBOOKS/ai_operating_system'),
]


def main() -> None:
    for root in ROOTS:
        print(f'[{root}]')
        if not root.exists():
            print('  missing')
            continue
        for item in sorted(root.glob('*.xlsx')):
            print(f'  - {item.as_posix()}')


if __name__ == '__main__':
    main()
