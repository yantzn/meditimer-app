# 品質ゲート

## 初期状態とCIの意味

現在は規約・品質チェックを準備する段階で、**Flutterアプリ本体はまだありません**。

PRごとに`repo-policy`ジョブがPythonの規約検査を実行します。`detect-flutter`はFlutterの有無を明示し、`pubspec.yaml`が存在しない場合は`flutter-checks`が**スキップ（未実行）**となります。これはFlutterのテストが合格したことを意味しません。

規約の構造検証をローカルで実行：

```bash
python3 scripts/validate_quality_policy.py
```

MEDI-2/MEDI-10でFlutterアプリを作成した後：

```bash
flutter pub get --enforce-lockfile
dart format --output=none --set-exit-if-changed lib test
flutter analyze --fatal-infos
flutter test --coverage
```

`flutter_lints`をdev_dependenciesへ追加し、`pubspec.lock`、`lib/main.dart`、`test/`をコミットする。解析設定は`analysis_options.yaml`を利用する。

## 品質ゲート一覧

| 品質ゲート | 適用時期 | 自動化 | 完了の考え方 |
| --- | --- | --- | --- |
| AI指示・スキル構造の検査 | すべてのPR | Pythonで実行 | 必須 |
| Dartの整形・静的解析 | Flutter初期化後 | GitHub Actions | 必須 |
| Unit/Widget Test | Flutter初期化後 | GitHub Actions | 必須 |
| iOS/Androidの実機スモーク試験 | P1リリース時 | 未整備 | 手動またはCIの証跡が必要 |
| Firestore Security RulesのEmulator試験 | P2リリース時 | 未整備 | 別家庭へのアクセス拒否が必須 |
| オフライン・競合・権限失効テスト | P2リリース時 | 未整備 | 実証が必要 |
| AIによる投薬安全・セキュリティレビュー | 該当変更時 | 手動適用 | Critical/Highが未解決でないこと |
| 医療機器該当性・法務確認 | リリース判断時 | 専門家確認 | 判断記録が必要 |

## レビュー重大度

- **Critical：** 根拠のない投薬許可、実投薬記録の消失・保存拒否、他家庭アクセス、無検知の同期上書き。
- **High：** 誤解を招くタイマー、訂正・監査履歴の欠落、危険な所属権限変更、未検証のSecurity Rules変更、健康情報のログ漏えい。
- **Medium/Low：** その他の正確性、操作性、耐障害性、保守性に関する問題。

AIの判定は**問題の発見支援**であり、自動的な安全性認証ではない。危険な変更を見抜けるかどうかの検証ケースは[AIレビューのレッドチーム試験](ai-review-red-team.md)を参照する。これらは実行していない限り「試験合格」とは扱わない。

## GitHubで別途設定が必要な項目

`main`への直接pushを制限し、Pull Requestと必要なCIチェックを必須にする。Flutter初期化前に存在しないFlutterジョブをマージ必須条件にしない。ブランチ保護／Rulesetはリポジトリ設定から管理する。

サードパーティGitHub Actionの固定SHA、Dependabotの更新方針も定期的に確認する。ロールバック・公開手順が決まるまでは自動マージやデプロイを導入しない。
