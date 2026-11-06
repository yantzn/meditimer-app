---
name: flutter-code-review
description: Reviews Flutter/Dart changes for architecture boundaries, persistence, async safety, platform parity, testability and CI regressions; use for every app PR.
---

# Flutter code review

1. Read `AGENTS.md`, the Jira AC and `.agents/rules/flutter-architecture.md`.
2. Inspect the **actual diff** and neighboring call paths, not just changed lines; identify new data models, services, widgets and generated code.
3. Check UI/data separation, repository abstractions, dependency injection, state transitions and immutable models. Reject hidden business decisions in widget build methods.
4. Review null safety, `async` lifecycle and cancellation, time provider injection, error feedback, transaction boundary and data-migration compatibility.
5. Validate iOS/Android parity, night use, accessibility and offline behavior.
6. Demand unit tests of logic, widget tests of flows, integration tests of data persistence; run `dart format --output=none --set-exit-if-changed .`, `flutter analyze`, `flutter test` when code exists.
7. Additionally call medication-safety-review for medication/time changes and security-review for auth, sync, storage or logging changes.

## Output contract

For each finding: **[Critical/High/Medium/Low] path:line — observed behavior; why it violates requirement; concrete reproduction/fix; missing test.** Include direct Jira/SRS references. Separate observed facts from suspected risks. State checks executed and skipped. If no findings, say "No issues found in inspected scope", not "safe" or "production ready".
