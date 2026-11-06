# MediTimer

小児発熱・服薬セーフティロガー（MediTimer）— iOS / Android 向け、オフラインファーストの発熱・投薬**記録支援**アプリ。

> 開発準備中。医療上の投与可否・用量・併用可否を判定するアプリではありません。

## Project references

- [Jira MEDI](https://yantzn.atlassian.net/jira/core/projects/MEDI/board)
- [System requirements (Confluence v0.4)](https://yantzn.atlassian.net/wiki/spaces/MFS/pages/14745601)
- [UI mockup source / gap analysis](https://yantzn.atlassian.net/wiki/spaces/MFS/pages/14778369)
- [Development roadmap](https://yantzn.atlassian.net/wiki/spaces/MFS/pages/14778427)

## Current scope

P0: Flutter/Drift/Firestore feasibility, safety/regulatory review and operating-cost validation.
P1: offline child, medication, symptom and temperature records; prescription interval history; clinic view/PDF.
P2: cross-platform caregiver sync, manually linked medications, conflict-aware status.
P3: premium entitlements and store releases.

Flutter, local persistence, backend and monetization libraries are **candidates**, not final choices until P0 findings are reviewed.

## Quality policy

Read [AGENTS.md](AGENTS.md), [architecture](docs/architecture.md), [safety/security rules](.agents/rules/medication-safety.md) and [quality gates](docs/quality-gates.md) before making changes. Skills in `.agents/skills/` provide reusable review protocols. AI reviews **assist** but do not replace automated tests, human review, medical advice or regulatory assessment.

### CI bootstrap state

This repository starts with only policy and tooling; there is no Flutter app or `pubspec.yaml` yet. The `repo-policy` CI job runs immediately. The `flutter-checks` job is **skipped, not passed**, until a Flutter project is added. Once bootstrapped, it runs format, analyzer and unit/widget tests on pull requests.

Before opening a Flutter implementation PR, initialize the Flutter app and add `flutter_lints` as a dev dependency. Check in `pubspec.lock`, a `lib/main.dart` and `test/` tests. CI rejects an incomplete Flutter scaffold.

## Workflow

- Work items: Jira `MEDI`.
- Branch: `feature/MEDI-123-description`, `fix/MEDI-123-description`, `docs/MEDI-123-description`, or `spike/MEDI-123-description`.
- PR title: `[MEDI-123] Meaningful summary`.
- Do not merge changes with unaddressed Critical/High safety or cross-household access findings.
- No personal medication/child health data in repository, screenshots, sample fixtures or CI logs.

See [quality gates](docs/quality-gates.md) for local checks and the release checklist.
