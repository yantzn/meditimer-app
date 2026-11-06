# 品質ゲート

## 初期状態とCIの意味

MEDI-31でFlutterの最小ソースとWidgetテストを追加しました。Flutterのネイティブ雛形とlockfileは公式CLIで生成・コミットする必要があります。

PRごとに`repo-policy`が構造を検査し、`Flutter format, analyze, test`がDart解析とWidget Testを実行し、`Android debug APK build`が公式CLI生成のAndroid雛形でビルドを実施します。CIが成功したことはWindowsエミュレーターや実機で動いたことの証拠ではありません。

規約の構造検証をローカルで実行：

```bash
python3 scripts/validate_quality_policy.py
```

Flutter SDKを導入した環境で：

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

## MEDI-31で残る作業

`pubspec.lock`は公式Flutter SDK 3.47.9のCI実行結果から生成・コミット済みです。CIで`--enforce-lockfile`を使って依存関係を固定します。`android/`・`ios/`の公式生成物は、GitHub Actionsの成果物またはWindowsの`scripts/bootstrap_flutter.ps1`で生成後、検証してリポジトリにコミットする必要があります。

Windowsでのエミュレーター手順：[初期構築ガイド](windows-flutter-setup.md)。iOS Simulator検証はMEDI-34、iOS／Android実機受入はMEDI-36。Android APKビルドが成功してもエミュレーター上での操作確認やiOS実機動作は未実施である。
