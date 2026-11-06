import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:meditimer/main.dart';

void main() {
  testWidgets('アプリ名と開発中の注意文言を表示する', (WidgetTester tester) async {
    await tester.pumpWidget(const MediTimerApp());

    expect(find.text('MediTimer'), findsOneWidget);
    expect(find.text('発熱・服薬の記録を準備しています'), findsOneWidget);
    expect(find.text('現在は技術検証用の画面です。記録・同期はできません。'), findsOneWidget);
  });

  testWidgets('暗色テーマでも初期画面の内容を表示する', (WidgetTester tester) async {
    tester.platformDispatcher.platformBrightnessTestValue = Brightness.dark;
    addTearDown(tester.platformDispatcher.clearPlatformBrightnessTestValue);

    await tester.pumpWidget(const MediTimerApp());

    expect(find.text('MediTimer'), findsOneWidget);
    expect(find.text('現在は技術検証用の画面です。記録・同期はできません。'), findsOneWidget);
  });
}
