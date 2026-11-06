#!/usr/bin/env python3
"""AI指示・スキルの構造検査。AIレビューや医療安全の実施判定はしない。"""

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
            errors.append(f"ファイルが存在しない、または空です: {item}")

    for name in SKILLS:
        path = ROOT / ".agents" / "skills" / name / "SKILL.md"
        if not path.is_file():
            continue
        contents = path.read_text(encoding="utf-8")
        if not re.match(r"\A---\s*\nname: " + re.escape(name) + r"\n", contents):
            errors.append(f"{path.relative_to(ROOT)}: YAMLフロントマターのnameが不正です")
        if not re.search(r"(?m)^description:\s*\S", contents):
            errors.append(f"{path.relative_to(ROOT)}: descriptionがありません")
        if len(contents.splitlines()) < 12:
            errors.append(f"{path.relative_to(ROOT)}: レビュー手順が不足しています")

    safety_path = ROOT / ".agents/rules/medication-safety.md"
    if safety_path.is_file():
        safety = safety_path.read_text(encoding="utf-8")
        for invariant in ("D-01", "D-02", "D-05", "D-07", "intervalMinutes", "Critical"):
            if invariant not in safety:
                errors.append(f"投薬安全規約の必須項目がありません: {invariant}")

    # これは検証ケース一覧の構造チェックであり、AIが問題を検知できる証明ではない。
    redteam = ROOT / "docs/ai-review-red-team.md"
    if redteam.is_file():
        cases = redteam.read_text(encoding="utf-8")
        for case in ("MED-S1", "MED-S2", "MED-S3", "SEC-S1", "SEC-S2", "DATA-S1"):
            if case not in cases:
                errors.append(f"レッドチーム試験ケースがありません: {case}")

    pubspec = ROOT / "pubspec.yaml"
    if pubspec.exists():
        for name in ("lib/main.dart",):
            if not (ROOT / name).is_file():
                errors.append(f"Flutterプロジェクトの必須ファイルがありません: {name}")
        if not (ROOT / "pubspec.lock").is_file():
            print("未確定: pubspec.lockはCIの公式Flutter SDKで生成後にコミットします。")
        if not (ROOT / "test").is_dir():
            errors.append("Flutterプロジェクトのtest/ディレクトリがありません")
        print("Flutter構成を検出しました。Flutter専用CIジョブも必ず実行してください。")
    else:
        print("未実行（合格ではありません）: Flutter解析・テスト。pubspec.yamlは未作成です。")

    if errors:
        print("リポジトリ規約チェックに失敗しました:", file=sys.stderr)
        for error in errors:
            print(f" - {error}", file=sys.stderr)
        return 1
    print("リポジトリ規約の構造検証: 合格。AIレビュー・医療安全・情報セキュリティの正しさは未評価です。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
