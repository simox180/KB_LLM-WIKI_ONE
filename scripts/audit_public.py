#!/usr/bin/env python3
"""Fail when public-facing repository content appears to expose local state."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", "__pycache__"}
OBSIDIAN_STATE_DIRS = {"plugins", "cache", "logs"}
TEXT_LIMIT = 2_000_000
RULES = {
    "private key": re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----"),
    "obvious secret": re.compile(r"(?i)(?:api[_-]?key|secret|password|token)\s*[:=]\s*['\"]?[A-Za-z0-9_./+\-]{16,}"),
    "local machine path": re.compile(r"(?i)(?:[A-Z]:\\Users\\|/Users/|/home/)"),
}


def is_obsidian_state(relative: Path) -> bool:
    parts = relative.parts
    return len(parts) >= 2 and parts[0] == ".obsidian" and parts[1] in OBSIDIAN_STATE_DIRS


def main():
    findings = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in SKIP_PARTS for part in relative.parts) or not path.is_file() or path.stat().st_size > TEXT_LIMIT:
            continue
        if is_obsidian_state(relative):
            findings.append(f"plugin or cache state: {relative.as_posix()}")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for name, pattern in RULES.items():
            if path == Path(__file__).resolve() and name == "local machine path":
                continue
            if pattern.search(content):
                findings.append(f"{name}: {relative.as_posix()}")
    if findings:
        print("public audit failed:", file=sys.stderr)
        print("\n".join("- " + item for item in findings), file=sys.stderr)
        return 1
    print("public audit passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
