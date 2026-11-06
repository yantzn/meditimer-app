# MediTimer

小児発熱・服薬セーフティロガー（MediTimer）は、iOS・Android向けの**オフラインファーストの発熱・投薬記録支援アプリ**です。

> 現在は開発準備段階です。本アプリは投薬の可否・推奨用量・薬剤の併用安全性を医学的に判定しません。

## プロジェクト資料

- [Jira：MEDIプロジェクト](https://yantzn.atlassian.net/jira/core/projects/MEDI/board)
- [システム要件定義書 v0.4（Confluence）](https://yantzn.atlassian.net/wiki/spaces/MFS/pages/14745601)
- [画面モックと差分一覧](https://yantzn.atlassian.net/wiki/spaces/MFS/pages/14778369)
- [開発ロードマップ](https://yantzn.atlassian.net/wiki/spaces/MFS/pages/14778427)

## フェーズごとの開発範囲

- **P0：** Flutter・ローカルDB・家族同期のPoC、医療安全と法的論点、継続的な運用原価の検証
- **P1：** オフラインでの児童・薬剤・体温・症状・投薬実績記録、間隔の経過時間表示、受診用PDF
- **P2：** iOS/Android混在の家族間同期、手動の関連薬グループ、競合・未同期状態の表示
- **P3：** 有料プランの権利管理、両ストアでの公開と運用

Flutter、ローカルDB、クラウドサービス、課金ライブラリは**P0技術検証で採否を決定する候補**です。事前に確定した技術として扱わないでください。

## AI・開発品質の基本方針

変更前に[AGENTS.md](AGENTS.md)を読み、変更内容に応じて[Flutter設計規約](.agents/rules/flutter-architecture.md)、[投薬安全規約](.agents/rules/medication-safety.md)、[セキュリティ規約](.agents/rules/security.md)を確認してください。

`.agents/skills/`には、コードレビュー、セキュリティ、投薬安全、テスト設計の手順を置いています。**AIによるレビューは補助**であり、自動テスト・開発者レビュー・医療専門家や法務の判断を代替しません。

### 現在のCIの状態

MEDI-31でFlutterの最小画面とWidgetテストを追加しました。GitHub Actionsでは次の検査を行う構成です（合否はCI実行結果を参照）。

- `Repository policy`：リポジトリ規約の構造を検証する
- `Flutter format, analyze, test`：整形・静的解析・Unit/Widget Testを実行する
- `Android debug APK build`：公式CLIでAndroid/iOS雛形を生成し、AndroidデバッグAPKをビルドする

`flutter_lints`、`lib/main.dart`、`test/`、`pubspec.lock`は追加済みです。`android/`、`ios/`の公式Flutter生成物は別途検証し、後続コミットで管理対象に追加する必要があります。手順は[Windows初期構築ガイド](docs/windows-flutter-setup.md)を参照してください。

## 開発運用

- Jiraキー：`MEDI`
- ブランチ例：`feature/MEDI-123-description`、`fix/MEDI-123-description`、`docs/MEDI-123-description`、`spike/MEDI-123-description`
- PRタイトル例：`[MEDI-123] Implement medication preset`
- Critical/Highの投薬安全・家族間認可に関する指摘は、解消・再検証するまでマージしない
- 実際の子ども・保護者・薬剤・健康情報をリポジトリ、スクリーンショット、テストデータ、CIログに含めない

具体的な実行方法と公開前の確認事項は[品質ゲート](docs/quality-gates.md)を参照してください。

初期画面は技術検証用で、投薬・体温の記録や家族同期は**未実装**です。Androidエミュレーターでの画面操作確認は別途必要です。
