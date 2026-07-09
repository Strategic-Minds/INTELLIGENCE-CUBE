from __future__ import annotations

from pathlib import Path
import sys


REQUIRED_FILES = [
    Path("START_HERE_FOR_AI.md"),
    Path("AI_WORKBOOK_INDEX.md"),
    Path("WORKBOOK_OS_MANIFEST.json"),
]


def must_contain(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise SystemExit(f"missing required text in {label}: {needle}")


def main() -> None:
    for rel in REQUIRED_FILES:
        if not rel.exists():
            raise SystemExit(f"missing required file: {rel}")

    index_text = Path("AI_WORKBOOK_INDEX.md").read_text(encoding="utf-8", errors="ignore")
    manifest_text = Path("WORKBOOK_OS_MANIFEST.json").read_text(encoding="utf-8", errors="ignore")
    start_text = Path("START_HERE_FOR_AI.md").read_text(encoding="utf-8", errors="ignore")

    must_contain(index_text, "HIGHEST_REPO_CEILING_ALL_IN_ONE", "AI_WORKBOOK_INDEX.md")
    must_contain(index_text, "FRONTEND_CEILING_WORKBOOK", "AI_WORKBOOK_INDEX.md")
    must_contain(index_text, "BACKEND_CEILING_WORKBOOK", "AI_WORKBOOK_INDEX.md")
    must_contain(index_text, "production remains locked", "AI_WORKBOOK_INDEX.md")
    must_contain(start_text, "WORKBOOK_OS_MANIFEST.json", "START_HERE_FOR_AI.md")
    must_contain(start_text, "AI_WORKBOOK_INDEX.md", "START_HERE_FOR_AI.md")
    must_contain(start_text, "source_truth_rank", "START_HERE_FOR_AI.md")
    must_contain(manifest_text, "primary/master_repo_ceiling", "WORKBOOK_OS_MANIFEST.json")
    must_contain(manifest_text, "support/frontend_primary", "WORKBOOK_OS_MANIFEST.json")
    must_contain(manifest_text, "support/backend_primary", "WORKBOOK_OS_MANIFEST.json")
    must_contain(manifest_text, "production_readiness", "WORKBOOK_OS_MANIFEST.json")

    print("AI WORKBOOK INDEX VALIDATION: PASS")
    print("required_files=3")
    print("official_workbooks_indexed=3")
    print("production_readiness_lock=present")


if __name__ == "__main__":
    main()

