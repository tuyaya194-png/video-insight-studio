#!/usr/bin/env python3
"""Validate the public repository structure without third-party packages."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "video-to-insight-html"


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []
    required = [
        ROOT / "README.md",
        ROOT / "README.zh-CN.md",
        ROOT / "LICENSE",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
        ROOT / "THIRD_PARTY_NOTICES.md",
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "images" / "hero.svg",
        ROOT / "docs" / "images" / "dual-output.svg",
        ROOT / "docs" / "demo" / "text" / "index.html",
        ROOT / "docs" / "demo" / "presentation" / "index.html",
        SKILL / "SKILL.md",
        SKILL / "LICENSE.txt",
        SKILL / "agents" / "openai.yaml",
        SKILL / "assets" / "text-version" / "index.html",
        SKILL / "assets" / "presentation-version" / "index.html",
    ]
    for path in required:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}", failures)

    skill_md = SKILL / "SKILL.md"
    if skill_md.is_file():
        content = skill_md.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", content, re.S)
        if not match:
            fail("SKILL.md has invalid frontmatter boundaries", failures)
        else:
            lines = [line for line in match.group(1).splitlines() if line.strip()]
            parsed: dict[str, str] = {}
            for line in lines:
                if ": " not in line:
                    fail(f"unsupported frontmatter line: {line}", failures)
                    continue
                key, value = line.split(": ", 1)
                parsed[key] = value
            if set(parsed) != {"name", "description"}:
                fail(f"unexpected frontmatter keys: {sorted(parsed)}", failures)
            if parsed.get("name") != "video-to-insight-html":
                fail("skill name must remain video-to-insight-html", failures)
            if len(parsed.get("description", "")) > 1024:
                fail("skill description exceeds 1024 characters", failures)

    forbidden = [
        "/Users/" + "liulingfeng",
        "TO" + "DO:",
        "FIX" + "ME:",
        "__GITHUB" + "_OWNER__",
    ]
    scan_suffixes = {".md", ".py", ".yaml", ".yml", ".html", ".svg", ".txt"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in scan_suffixes:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for token in forbidden:
            if token in text:
                fail(f"forbidden token {token!r} in {path.relative_to(ROOT)}", failures)

    validator = SKILL / "scripts" / "validate_project.py"
    if validator.is_file():
        result = subprocess.run(
            [
                sys.executable,
                str(validator),
                "--text-dir",
                str(SKILL / "assets" / "text-version"),
                "--presentation-dir",
                str(SKILL / "assets" / "presentation-version"),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode != 0:
            fail(f"template validation failed: {result.stdout}{result.stderr}", failures)

    report = {"ok": not failures, "failures": failures}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
