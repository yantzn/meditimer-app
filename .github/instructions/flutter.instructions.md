---
applyTo: "**/*.dart"
---
Dartコードを変更するときは、[Flutterアーキテクチャ規約](../../.agents/rules/flutter-architecture.md)を適用し、関係する場合は[投薬安全規約](../../.agents/rules/medication-safety.md)も適用する。UIとRepositoryの責務を分離し、Clock・依存性を注入し、イベント原本と訂正・監査履歴を維持する。実際に実行したテスト結果を記載し、未実行の検証を合格としない。
