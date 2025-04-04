import 'package:flutter/material.dart';
import 'screens/home.dart';
import 'screens/calculator.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'My App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: '/',  // Define the initial route
      routes: {
        '/': (context) => const HomePage(),  // First screen
        '/calculator': (context) => const VisitorsCalculator(), // Second screen
      },
    );
  }
}
