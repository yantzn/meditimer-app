#!/usr/bin/env python3
"""Fail-fast repository structure checks; does not claim to run an AI or medical review."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md",
    "AGENTS.md",
    "analysis_options.yaml",
    ".github/workflows/ci.yml",
    ".github/dependabot.yml",
    ".github/pull_request_template.md",
    ".github/copilot-instructions.md",
    ".agents/rules/flutter-architecture.md",
    ".agents/rules/medication-safety.md",
    ".agents/rules/security.md",
    "docs/architecture.md",
    "docs/security-threat-model.md",
    "docs/quality-gates.md",
    "docs/ai-review-red-team.md",
    ".agents/skills/flutter-code-review/SKILL.md",
    ".agents/skills/security-review/SKILL.md",
    ".agents/skills/medication-safety-review/SKILL.md",
    ".agents/skills/test-design/SKILL.md",
)
SKILLS = {
    "flutter-code-review",
    "security-review",
    "medication-safety-review",
    "test-design",
}


def main() -> int:
    errors: list[str] = []
    for item in REQUIRED:
        path = ROOT / item
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing/empty: {item}")

    for name in SKILLS:
        path = ROOT / ".agents" / "skills" / name / "SKILL.md"
        if not path.is_file():
            continue
        contents = path.read_text(encoding="utf-8")
        if not re.match(r"\A---\s*\nname: " + re.escape(name) + r"\n", contents):
            errors.append(f"{path.relative_to(ROOT)}: missing expected name in YAML frontmatter")
        if not re.search(r"(?m)^description:\s*\S", contents):
            errors.append(f"{path.relative_to(ROOT)}: missing description")
        if len(contents.splitlines()) < 12:
            errors.append(f"{path.relative_to(ROOT)}: incomplete review procedure")

    safety_path = ROOT / ".agents/rules/medication-safety.md"
    if safety_path.is_file():
        text = safety_path.read_text(encoding="utf-8")
        for invariant in ("D-01", "D-02", "D-05", "D-07", "intervalMinutes", "Critical"):
            if invariant not in text:
                errors.append(f"Missing medication-safety rule marker: {invariant}")

    # This is a structural safeguard, not proof that AI recognized the red-team cases.
    redteam = ROOT / "docs/ai-review-red-team.md"
    if redteam.is_file():
        text = redteam.read_text(encoding="utf-8")
        for case in ("MED-S1", "MED-S2", "MED-S3", "SEC-S1", "SEC-S2", "DATA-S1"):
            if case not in text:
                errors.append(f"Missing red-team scenario: {case}")

    pubspec = ROOT / "pubspec.yaml"
    if pubspec.exists():
        for name in ("pubspec.lock", "lib/main.dart"):
            if not (ROOT / name).is_file():
                errors.append(f"Flutter project is incomplete: {name}")
        if not (ROOT / "test").is_dir():
            errors.append("Flutter project is incomplete: test/ directory")
        print("Flutter scaffold found: Flutter checks must run in their separate CI job.")
    else:
        print("PENDING (not passed): Flutter analyzer/tests — pubspec.yaml not created yet.")

    if errors:
        print("Repository policy validation FAILED:", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1
    print("Repository policy structure PASS. AI review and medical/security correctness NOT evaluated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
