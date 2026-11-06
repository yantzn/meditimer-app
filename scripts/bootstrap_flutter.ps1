# Windows PowerShell 5.1+ / PowerShell 7
# MEDI-31: 公式Flutter CLIでAndroid/iOSネイティブ雛形とpubspec.lockを生成する。
# Mac不要。ただしiOSのビルドと実機動作確認はここでは行わない。
$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
Set-Location $root

if (-not (Get-Command flutter -ErrorAction SilentlyContinue)) {
  throw "Flutter SDKがPATHにありません。WindowsにFlutter SDKを導入してください。"
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
  throw "GitがPATHにありません。"
}

$changes = git status --porcelain
if ($LASTEXITCODE -ne 0) { throw "git status に失敗しました。" }
if ($changes) {
  throw "作業ツリーがクリーンではありません。既存変更をコミットするなどしてから再実行してください。"
}
if ((Test-Path -LiteralPath "android") -or (Test-Path -LiteralPath "ios")) {
  throw "android/ または ios/ が既に存在します。意図しない上書きを防ぐため終了します。"
}

Write-Host "Flutter SDK:" -ForegroundColor Cyan
flutter --version
if ($LASTEXITCODE -ne 0) { throw "Flutter SDK の実行に失敗しました。" }

# dev.meditimer はPoC用の仮識別子。商用公開前にapplication/bundle IDを決定する。
# flutter createをリポジトリ直下で実行するとpubspec.yamlを更新する可能性があるため
# 一時ディレクトリで公式雛形を作成し、ネイティブディレクトリだけをコピーする。
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("meditimer-bootstrap-" + [guid]::NewGuid().ToString("N"))
try {
  $templateRoot = Join-Path $tempRoot "meditimer"
  flutter create --project-name=meditimer --org=dev.meditimer --platforms=android,ios --no-pub $templateRoot
  if ($LASTEXITCODE -ne 0) { throw "Flutterのネイティブ雛形生成に失敗しました。" }

  $sourceAndroid = Join-Path $templateRoot "android"
  $sourceIos = Join-Path $templateRoot "ios"
  if (-not (Test-Path $sourceAndroid) -or -not (Test-Path $sourceIos)) {
    throw "Flutterがandroid/とios/を生成できませんでした。"
  }

  Copy-Item -LiteralPath $sourceAndroid -Destination (Join-Path $root "android") -Recurse
  Copy-Item -LiteralPath $sourceIos -Destination (Join-Path $root "ios") -Recurse
}
finally {
  if (Test-Path -LiteralPath $tempRoot) {
    Remove-Item -LiteralPath $tempRoot -Recurse -Force
  }
}

flutter pub get --enforce-lockfile
if ($LASTEXITCODE -ne 0) { throw "固定済みlockfileを使った依存解決に失敗しました。" }

flutter analyze --fatal-infos
if ($LASTEXITCODE -ne 0) { throw "静的解析が失敗しました。" }

flutter test
if ($LASTEXITCODE -ne 0) { throw "Widget/Unitテストが失敗しました。" }

Write-Host ""
Write-Host "生成された android/、ios/、pubspec.lock の内容を確認してください。" -ForegroundColor Green
Write-Host "iOSのビルド・iPhoneでの検証は未実施です。GitHub ActionsのmacOS検証はMEDI-34で扱います。"
git status --short
