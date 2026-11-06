import 'package:flutter/material.dart';

void main() {
  runApp(const MediTimerApp());
}

/// 技術検証用の最小アプリ。記録、投薬判定、同期機能は未実装。
class MediTimerApp extends StatelessWidget {
  const MediTimerApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MediTimer',
      locale: const Locale('ja'),
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF237C8C)),
      ),
      darkTheme: ThemeData(
        useMaterial3: true,
        brightness: Brightness.dark,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF73D7E6),
          brightness: Brightness.dark,
        ),
      ),
      home: const Scaffold(
        appBar: MediTimerAppBar(),
        body: Center(
          child: Padding(
            padding: EdgeInsets.all(24),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: <Widget>[
                Icon(Icons.assignment_outlined, size: 48),
                SizedBox(height: 16),
                Text(
                  '発熱・服薬の記録を準備しています',
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 8),
                Text(
                  '現在は技術検証用の画面です。記録・同期はできません。',
                  textAlign: TextAlign.center,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class MediTimerAppBar extends StatelessWidget
    implements PreferredSizeWidget {
  const MediTimerAppBar({super.key});

  @override
  Size get preferredSize => const Size.fromHeight(kToolbarHeight);

  @override
  Widget build(BuildContext context) {
    return AppBar(title: const Text('MediTimer'));
  }
}
