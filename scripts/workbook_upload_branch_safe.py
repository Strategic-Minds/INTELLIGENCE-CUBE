from __future__ import annotations

import argparse
import shlex
import shutil
import subprocess
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy workbook artifacts into the repo on a branch-safe path and optionally commit/push."
    )
    parser.add_argument("--source-dir", required=True, help="Directory containing workbook artifacts to upload.")
    parser.add_argument(
        "--destination-dir",
        required=True,
        help="Repo-relative destination directory, for example 01_Builder_Docs/highest-repo-ceiling-all-in-one.",
    )
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repo root directory. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="One or more artifact filenames to copy from source-dir into destination-dir.",
    )
    parser.add_argument("--commit-message", default="docs: upload workbook artifacts", help="Commit message to use.")
    parser.add_argument("--push", action="store_true", help="Push the current branch after committing.")
    parser.add_argument(
        "--validate-command",
        default=None,
        help="Optional command to run after copying, for example the workbook validator invocation.",
    )
    return parser.parse_args()


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=str(cwd), check=True)


def main() -> None:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    source_dir = Path(args.source_dir).resolve()
    destination_dir = (repo_root / args.destination_dir).resolve()

    if not source_dir.exists():
        raise SystemExit(f"source directory does not exist: {source_dir}")
    if repo_root.name == "":
        raise SystemExit("repo root is invalid")
    destination_dir.mkdir(parents=True, exist_ok=True)

    repo_root_resolved = repo_root.resolve()
    destination_dir_resolved = destination_dir.resolve()
    if repo_root_resolved not in destination_dir_resolved.parents and destination_dir_resolved != repo_root_resolved:
        raise SystemExit(f"destination escapes repo root: {destination_dir_resolved}")

    copied: list[str] = []
    for filename in args.files:
        src = source_dir / filename
        if not src.exists():
            raise SystemExit(f"missing source artifact: {src}")
        dst = destination_dir / filename
        if src.resolve() == dst.resolve():
            copied.append(str(dst.relative_to(repo_root)))
            continue
        shutil.copy2(src, dst)
        copied.append(str(dst.relative_to(repo_root)))

    if args.validate_command:
        run(shlex.split(args.validate_command), repo_root)

    run(["git", "status", "--short"], repo_root)

    if args.push:
        run(["git", "add", *copied], repo_root)
        run(["git", "commit", "-m", args.commit_message], repo_root)
        run(["git", "push", "origin", "HEAD"], repo_root)


if __name__ == "__main__":
    main()
