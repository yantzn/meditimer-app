# MEDI-31：MacなしでFlutterを初期構築する

> この文書は**手順書**です。手元のWindows PC・Android Emulatorでの動作を実施・確認した結果ではありません。

## 前提

- Windows 10/11、Git、PowerShell。
- Flutter公式SDKを導入し、`flutter`をPATHへ追加する。
- Android Studio、Android SDK／SDK Command-line Tools、Android Emulator、必要に応じて仮想化支援を設定する。
- `flutter doctor -v`でFlutter・Android toolchainの状態と未解決警告を確認する。
- `flutter doctor --android-licenses`で必要なライセンスを確認する（ライセンス内容を読んで同意する）。
- iOSのビルドにはmacOSとXcodeが必要。WindowsでiOSをビルドしたと報告しない。

公式資料：[FlutterのWindows導入](https://docs.flutter.dev/get-started/install/windows/mobile) ／ [Android開発環境](https://docs.flutter.dev/platform-integration/android/setup)。

## 初回生成

リポジトリの`feature/MEDI-31-flutter-bootstrap`をチェックアウトし、Gitの作業ツリーをクリーンにした後：

```powershell
.\scripts\bootstrap_flutter.ps1
```

このスクリプトは**公式Flutter CLI**で`android/`・`ios/`を生成し、`pubspec.lock`も作成します。既存ディレクトリや未コミットの変更がある場合は停止し、`--overwrite`を使いません。

`dev.meditimer`はPoCの仮パッケージ識別子です。商用公開前にAndroid Application ID／iOS Bundle IDを確定します。

## Androidエミュレーターでの確認

Android StudioのDevice ManagerからAVDを作成・起動してから：

```powershell
flutter devices
flutter run
```

画面に`MediTimer`と「現在は技術検証用の画面です。記録・同期はできません。」が表示されることを確認してください。実際の服薬記録は使用しません。

```powershell
dart format --output=none --set-exit-if-changed lib test
flutter analyze --fatal-infos
flutter test
flutter build apk --debug
```

`flutter run`で複数デバイスが見つかる場合は`flutter devices`のIDを確認して`flutter run -d <device-id>`を使用します。Android実機を持たない場合もAVDで検証できますが、実機QAの代替にはなりません。

## GitHub Actions

PRではLinuxのGitHub ActionsがFlutter解析・Widgetテスト・Androidデバッグビルドを実行します。ローカルのエミュレーター起動・操作は自動化されておらず、手元での結果をPRに記録してください。

CIがネイティブ雛形とlockfileをその場で生成することは、**それらのファイルがGitにコミット済みであることを意味しません**。Flutter初期化の完了には公式CLIで生成したファイルを後続コミットで管理対象へ反映する必要があります。

iOSのmacOSランナー・Simulatorスモークは[MEDI-34](https://yantzn.atlassian.net/browse/MEDI-34)、実機検証は[MEDI-36](https://yantzn.atlassian.net/browse/MEDI-36)で扱います。
