# Flutterアーキテクチャ規約

参考：[Flutter公式アーキテクチャガイド](https://docs.flutter.dev/app-architecture/recommendations)

- UI（Widget・画面・ViewModel）とデータ層（Repository・Service）の責務を分離する。Widgetの`build()`にDBアクセスや投薬業務ロジックを書かない。
- 一方向データフロー、明示的な状態遷移、不変データモデル、依存性注入、Repository抽象を原則とする。
- 経過時間の計算、投薬イベント照合、日時処理は単体テスト可能な純粋ロジックに分離する。`DateTime.now()`を業務ロジックに直接埋め込まず、Clockを注入する。
- 実投与日時`occurredAt`と記録入力日時`recordedAt`は区別する。タイムゾーン・日付跨ぎ・時計補正を検証する。
- 機能ごとに責務を分ける。構成例は`lib/features/<feature>/{data,domain,presentation}`。過度な抽象化は避け、実際のPoCを踏まえて採用する。
- 非同期処理ではキャンセル、例外通知、再試行、リソース解放を明示し、DBや同期エラーを黙って握りつぶさない。
- P1以降の画面では、DBに永続化されたデータの代わりにデモ用状態を正本として扱わない。
- iOS/Android双方でアクセシビリティ、大きな操作領域、読み上げ、夜間表示、オフライン画面、ローカルPDFを検証する。
- ロジックはUnit Test、画面はWidget Test、重要な記録フローはIntegration Testを用意する。正常系だけでなくクラッシュ・データ消失をテストする。
- 状態管理・DI・ナビゲーション・永続化パッケージは、PoC後にADRへ採用理由を記録する。AIが独断で固定しない。
