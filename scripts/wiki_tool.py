#!/usr/bin/env python3
"""Deterministic, standard-library tooling for the LLM Wiki."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "Wiki"
RAW = ROOT / "Raw" / "Sources"
SCHEMA = ROOT / "Schema"
CATALOG = WIKI / "catalog.jsonl"
MANIFEST = SCHEMA / "source-manifest.jsonl"
ALLOWED_TAGS = {"topic", "concept", "entity", "project", "log"}
GENERATED = {"index.md", "log.md"}


def repo_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def today() -> str:
    return dt.date.today().isoformat()


def markdown_files(folder: Path):
    if not folder.exists():
        return []
    return sorted(p for p in folder.rglob("*.md") if p.name != ".gitkeep")


def compiled_notes():
    return [p for p in markdown_files(WIKI) if p.name not in GENERATED]


def scalar(value: str):
    value = value.strip()
    if not value:
        return ""
    if value in ("[]", "{}"):
        return [] if value == "[]" else {}
    if value.lower() in ("true", "false"):
        return value.lower() == "true"
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        return [scalar(x) for x in value[1:-1].split(",") if x.strip()]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def frontmatter(path: Path):
    """Parse the deliberately small YAML subset used by repository templates."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return None, "file is not UTF-8 text"
    if not lines or lines[0].strip() != "---":
        return None, "missing opening frontmatter delimiter"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "missing closing frontmatter delimiter"
    data, key = {}, None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")) and raw.strip().startswith("-"):
            if key is None or not isinstance(data.get(key), list):
                return None, "list item without a list key"
            data[key].append(scalar(raw.strip()[1:].strip()))
            continue
        if ":" not in raw:
            return None, "invalid frontmatter line: " + raw
        key, value = raw.split(":", 1)
        key = key.strip()
        data[key] = [] if not value.strip() else scalar(value)
    return data, None


def markdown_body(path: Path) -> str:
    """Return a note's Markdown body, excluding its frontmatter when present."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        except StopIteration:
            return text
        return "\n".join(lines[end + 1:])
    return text


def body_excerpt(body: str, query: str, limit: int = 180) -> str:
    """Return a compact, deterministic excerpt around the first body match."""
    normalized = re.sub(r"\s+", " ", body).strip()
    index = normalized.casefold().find(query)
    if index < 0:
        return ""
    start = max(0, index - limit // 3)
    end = min(len(normalized), start + limit)
    if end - start < limit:
        start = max(0, end - limit)
    prefix = "…" if start else ""
    suffix = "…" if end < len(normalized) else ""
    return prefix + normalized[start:end].strip() + suffix


def link_path(value):
    value = str(value).strip()
    if value.startswith("[[") and value.endswith("]]" ):
        value = value[2:-2].split("|", 1)[0].strip()
    return value.replace("\\", "/")


def source_paths(meta):
    sources = meta.get("sources", [])
    return sources if isinstance(sources, list) else []


def load_notes():
    result = []
    for path in compiled_notes():
        meta, error = frontmatter(path)
        result.append((path, meta, error))
    return result


def coverage():
    covered = {repo_path(p): [] for p in markdown_files(RAW)}
    for note, meta, error in load_notes():
        if error or not meta:
            continue
        for entry in source_paths(meta):
            target = link_path(entry)
            if target in covered:
                covered[target].append(repo_path(note))
    return {key: sorted(value) for key, value in sorted(covered.items())}


def build(_args):
    WIKI.mkdir(parents=True, exist_ok=True)
    records = []
    for path, meta, error in load_notes():
        if error:
            print(f"warning: {repo_path(path)}: {error}", file=sys.stderr)
            continue
        tags = meta.get("tags", []) if isinstance(meta.get("tags"), list) else []
        records.append({"path": repo_path(path), "title": str(meta.get("title", path.stem)), "aliases": meta.get("aliases", []) if isinstance(meta.get("aliases"), list) else [], "summary": str(meta.get("summary", "")), "tag": tags[0] if tags else "", "topics": meta.get("topics", []) if isinstance(meta.get("topics"), list) else [], "sources": [link_path(x) for x in source_paths(meta)], "updated": str(meta.get("updated", ""))})
    records.sort(key=lambda item: item["path"])
    CATALOG.write_text("".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in records), encoding="utf-8")

    folders = sorted([WIKI] + [p for p in WIKI.rglob("*") if p.is_dir()])
    for folder in folders:
        children = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix == ".md" and p.name not in {"index.md", "log.md"})
        lines = ["# " + ("Wiki index" if folder == WIKI else folder.name), ""]
        for child in children:
            meta, error = frontmatter(child)
            label = str(meta.get("title", child.stem)) if not error else child.stem
            lines.append(f"- [[{repo_path(child)[:-3]}|{label}]]")
        lines.append("")
        (folder / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"built {len(records)} catalog records and {len(folders)} indexes")


def lint(_args):
    errors = []
    for path, meta, error in load_notes():
        label = repo_path(path)
        if error:
            errors.append(f"{label}: {error}")
            continue
        tags = meta.get("tags")
        if not isinstance(tags, list) or not tags or any(tag not in ALLOWED_TAGS for tag in tags):
            errors.append(f"{label}: tags must be a non-empty list from {', '.join(sorted(ALLOWED_TAGS))}")
        if not isinstance(meta.get("topics"), list):
            errors.append(f"{label}: topics must be a list")
        if not isinstance(meta.get("aliases"), list):
            errors.append(f"{label}: aliases must be a list")
        for key in ("status", "created", "updated", "sources", "source_count"):
            if key not in meta or meta[key] in ("", None):
                errors.append(f"{label}: missing required field {key}")
        for key in ("created", "updated"):
            try:
                dt.date.fromisoformat(str(meta.get(key)))
            except (TypeError, ValueError):
                errors.append(f"{label}: {key} must be an ISO date")
        try:
            if dt.date.fromisoformat(str(meta.get("updated"))) < dt.date.fromisoformat(str(meta.get("created"))):
                errors.append(f"{label}: updated cannot precede created")
        except (TypeError, ValueError):
            pass
        sources = source_paths(meta)
        if not isinstance(meta.get("sources"), list):
            errors.append(f"{label}: sources must be a list")
        elif not sources:
            errors.append(f"{label}: compiled notes require at least one source")
        if type(meta.get("source_count")) is not int:
            errors.append(f"{label}: source_count must be an integer")
        elif meta.get("source_count") != len(sources):
            errors.append(f"{label}: source_count must equal the number of sources")
        for entry in sources:
            target = link_path(entry)
            candidate = (ROOT / target).resolve()
            try:
                candidate.relative_to(RAW.resolve())
                is_raw_source = True
            except ValueError:
                is_raw_source = False
            if not target.startswith("Raw/Sources/") or not is_raw_source or not candidate.is_file():
                errors.append(f"{label}: invalid source link {entry!r}")
    return report(errors, "lint passed")


def source_scan(args):
    entries = coverage()
    if args.update:
        if not args.accept_covered:
            print("refusing manifest update: pass --accept-covered after verifying coverage", file=sys.stderr)
            return 2
        records = []
        for raw_path, notes in entries.items():
            path = ROOT / raw_path
            meta, _ = frontmatter(path)
            processed = bool(meta and meta.get("Processed") is True)
            records.append({"path": raw_path, "title": str(meta.get("Title", path.stem)) if meta else path.stem, "processed": processed, "covered_by": notes, "updated": today()})
        MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MANIFEST.write_text("".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in records), encoding="utf-8")
        print(f"updated manifest with {len(records)} sources")
    else:
        for raw_path, notes in entries.items():
            print(f"{raw_path}\t{'covered' if notes else 'uncovered'}")
    return 0


def source_lint(_args):
    errors = []
    covered = coverage()
    for path in markdown_files(RAW):
        meta, error = frontmatter(path)
        label = repo_path(path)
        if error:
            errors.append(f"{label}: {error}")
            continue
        for key in ("Title", "Reference", "Created", "Processed", "tags"):
            if key not in meta or meta[key] in ("", None, []):
                errors.append(f"{label}: missing required field {key}")
        if "Processed" in meta and not isinstance(meta["Processed"], bool):
            errors.append(f"{label}: Processed must be true or false")
        if meta.get("Processed") is True and not covered.get(label):
            errors.append(f"{label}: processed source has no Wiki coverage")
    return report(errors, "source-lint passed")


def source_delta(_args):
    manifest_paths = set()
    if MANIFEST.exists():
        for line in MANIFEST.read_text(encoding="utf-8").splitlines():
            try:
                manifest_paths.add(json.loads(line)["path"])
            except (json.JSONDecodeError, KeyError):
                print("warning: invalid manifest line", file=sys.stderr)
    delta = [p for p in coverage() if p not in manifest_paths]
    print("\n".join(delta))
    return 0


def source_coverage(_args):
    for raw_path, notes in coverage().items():
        print(f"{raw_path}: " + (", ".join(notes) if notes else "uncovered"))
    return 0


def search_catalog(args):
    if not CATALOG.exists():
        print("catalog missing; run build first", file=sys.stderr)
        return 2
    query = args.query.casefold().strip()
    if not query:
        return 0
    matches = []
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        path = (ROOT / item.get("path", "")).resolve()
        try:
            path.relative_to(WIKI.resolve())
        except ValueError:
            continue
        body = markdown_body(path) if path.is_file() else ""
        fields = {
            "title": str(item.get("title", "")),
            "aliases": " ".join(str(alias) for alias in item.get("aliases", [])),
            "summary": str(item.get("summary", "")),
            "topics": " ".join(str(topic) for topic in item.get("topics", [])),
            "body": body,
        }
        counts = {name: value.casefold().count(query) for name, value in fields.items()}
        if not any(counts.values()):
            continue
        # Each field is capped so one higher-priority field always outweighs all lower ones.
        score = sum(min(counts[name], 9) * weight for name, weight in {
            "title": 10000,
            "aliases": 1000,
            "summary": 100,
            "topics": 10,
            "body": 1,
        }.items())
        result = dict(item)
        result["score"] = score
        if counts["body"]:
            result["excerpt"] = body_excerpt(body, query)
        matches.append(result)
    matches.sort(key=lambda item: (-item["score"], item.get("path", "")))
    for item in matches:
        print(json.dumps(item, ensure_ascii=False, sort_keys=True))
    return 0


def log(args):
    path = WIKI / "log.md"
    WIKI.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text("---\ntags:\n  - log\ntopics: []\nstatus: seed\ncreated: " + today() + "\nupdated: " + today() + "\nsources: []\nsource_count: 0\naliases: []\n---\n\n# Wiki log\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n## {today()} — {args.title}\n\n{args.details}\n")
    print(f"added log entry to {repo_path(path)}")
    return 0


def doctor(_args):
    required = [WIKI, RAW, SCHEMA, ROOT / "scripts"]
    missing = [repo_path(p) for p in required if not p.is_dir()]
    print(f"Python: {sys.version.split()[0]}")
    print("directories: " + ("ok" if not missing else "missing " + ", ".join(missing)))
    print("catalog: " + ("present" if CATALOG.is_file() else "missing"))
    print("source manifest: " + ("present" if MANIFEST.is_file() else "missing"))
    print(f"compiled notes: {len(compiled_notes())}")
    print(f"raw sources: {len(markdown_files(RAW))}")
    return 1 if missing else 0


def report(errors, success):
    if errors:
        print("\n".join("error: " + e for e in errors), file=sys.stderr)
        return 1
    print(success)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, func in {"doctor": doctor, "build": build, "lint": lint, "source-lint": source_lint, "source-delta": source_delta, "source-coverage": source_coverage}.items():
        sub.add_parser(name).set_defaults(func=func)
    scan = sub.add_parser("source-scan")
    scan.add_argument("--update", action="store_true")
    scan.add_argument("--accept-covered", action="store_true")
    scan.set_defaults(func=source_scan)
    search = sub.add_parser("search-catalog")
    search.add_argument("--query", required=True)
    search.set_defaults(func=search_catalog)
    entry = sub.add_parser("log")
    entry.add_argument("--title", required=True)
    entry.add_argument("--details", required=True)
    entry.set_defaults(func=log)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
