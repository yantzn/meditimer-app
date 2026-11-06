# MediTimer：GitHub Copilot向け開発指示

開発指示の正本は[AGENTS.md](../AGENTS.md)です。変更前に対象のJira `MEDI`チケット、`AGENTS.md`、関係する`.agents/rules/*.md`を確認してください。汎用的な薬剤知識でMediTimerの確定要件を書き換えないでください。

- Flutterの開発では`.agents/rules/flutter-architecture.md`に従う。
- 投薬、時間、薬剤プリセット、画面文言の変更では`.agents/rules/medication-safety.md`に従う。アプリは**投薬実績を記録**するものであり、投薬を許可しない。
- 認証、同期、保存、ログでは`.agents/rules/security.md`に従う。
- PRレビューでは必要に応じて`.agents/skills/`内の4つのレビュースキルを利用する。
- レビューは日本語で、重大度・ファイル:行・根拠・再現方法・不足テスト・実行結果を報告する。指示ファイルを置いただけでAIレビューが自動実行されたとはみなさない。
- Jira受入基準を満たす最小限の変更を選ぶ。Critical/Highの未解決指摘を残したままマージしない。
