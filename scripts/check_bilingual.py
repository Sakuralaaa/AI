"""Static checks for bilingual documentation. Uses the Python standard library only."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
ZH_DIR = ROOT / "docs" / "zh-CN"
EN_DIR = ROOT / "docs" / "en"
STATUS_FILE = ROOT / "resources" / "translation-status.yml"

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
META_RE = re.compile(r"<!--\s*(.*?)\s*-->", re.DOTALL)
SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Bearer token": re.compile(r"Bearer\s+[A-Za-z0-9._~-]{24,}"),
}


def paired_docs(errors: list[str]) -> list[Path]:
    zh_files = {p.name for p in ZH_DIR.glob("*.md")}
    en_files = {p.name for p in EN_DIR.glob("*.md")}
    if zh_files != en_files:
        for name in sorted(zh_files - en_files):
            errors.append(f"missing English pair: docs/en/{name}")
        for name in sorted(en_files - zh_files):
            errors.append(f"missing Chinese source: docs/zh-CN/{name}")

    status_text = STATUS_FILE.read_text(encoding="utf-8")
    registered = set(re.findall(r"^\s*- path:\s*(\S+)\s*$", status_text, re.MULTILINE))
    for name in sorted(zh_files - registered):
        errors.append(f"not registered in translation-status.yml: {name}")
    for name in sorted(registered - zh_files):
        errors.append(f"translation-status.yml references missing document: {name}")

    return sorted(ZH_DIR.glob("*.md")) + sorted(EN_DIR.glob("*.md"))


def check_metadata(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    match = META_RE.match(text)
    if not match:
        errors.append(f"missing metadata comment: {path.relative_to(ROOT)}")
        return
    metadata = match.group(1)
    required = ["lang:", "status:", "last_updated:", "last_verified:"]
    for field in required:
        if field not in metadata:
            errors.append(f"missing {field} in {path.relative_to(ROOT)}")
    if path.parent.name == "en" and "source_revision:" not in metadata:
        errors.append(f"missing source_revision in {path.relative_to(ROOT)}")


def normalize_link(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target:
        target = target.split(" ", 1)[0]
    return unquote(target.split("#", 1)[0])


def check_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target = normalize_link(raw)
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            errors.append(f"link escapes repository in {path.relative_to(ROOT)}: {raw}")
            continue
        if not resolved.exists():
            errors.append(f"broken local link in {path.relative_to(ROOT)}: {raw}")


def check_secrets(path: Path, errors: list[str]) -> None:
    if ".git" in path.parts or not path.is_file():
        return
    if path.suffix.lower() not in {".md", ".yml", ".yaml", ".csv", ".py", ".do"}:
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"possible {label} in {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    docs = paired_docs(errors)
    for path in docs:
        check_metadata(path, errors)

    for path in ROOT.rglob("*.md"):
        if ".git" not in path.parts:
            check_links(path, errors)
    for path in ROOT.rglob("*"):
        check_secrets(path, errors)

    if errors:
        print("Documentation checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Documentation checks passed: {len(docs) // 2} bilingual chapter pairs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
