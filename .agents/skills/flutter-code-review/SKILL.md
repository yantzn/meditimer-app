---
name: flutter-code-review
description: Flutter・Dartの設計分離、永続化、非同期安全性、iOS/Android差分、テスト可能性、CI退行をレビューする。FlutterのPRで使用する。
---

# Flutterコードレビュースキル

1. `AGENTS.md`、Jira受入基準、`.agents/rules/flutter-architecture.md`を読む。
2. 変更差分だけでなく関連する呼び出し元・呼び出し先、モデル、Service、Repository、Widget、生成コードまで確認する。
3. UIとデータの責務、DI、状態遷移、不変データモデル、一方向データフローを検証する。`build()`内の隠れた業務判断を指摘する。
4. Null safety、`async`処理・キャンセル、Clock注入、例外表示、トランザクション、データ移行の後方互換性を確認する。
5. iOS/Android差分、夜間操作、アクセシビリティ、オフライン動作を検証する。
6. Unit/Widget/Integration Testの不足を特定し、Flutterコードが存在すれば`dart format`、`flutter analyze`、`flutter test`を実行する。
7. 投薬・日時が関係する場合は`medication-safety-review`、認証・同期・保存・ログが関係する場合は`security-review`を併用する。

## レビュー結果の形式

各指摘を**[Critical/High/Medium/Low] ファイル:行 — 事実・要件違反・影響・再現方法・修正案・不足テスト**で報告する。実装で確認した事実と仮説は区別する。実行した検証と未実行の検証を分ける。指摘なしの場合も「確認範囲では問題なし」と表現し、「安全保証」「本番利用可能」と断言しない。
