import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'node.dart';
import 'dart:core';

List<Node> decisionMap = [
  Node(1,2,3,"Style of play","Choose Tactics","Attack","Defense"),
  Node(2,4,5,"Attack","Ball Possession","Pass","Run"),
  Node(4,8,9,"Opponent Presses","Response","Successfully evade","Get tackled"),
  Node(5,10,11,"Opponent Tackles","Response","Penalty awarded","Loss of possesion"),
  Node(6,12,13,"Opponent Fall back","Response","Create space","Get marked"),
  Node(7,14,15,"Shot on Goal","Direction","Left","Right"),
  Node(8,16,7,"Pass to teammate","Type of pass","Long pass","Short pass"),];


void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  String csv = "sheet1.csv"; // Path to CSV file

  try {
    String fileData = await rootBundle.loadString(csv);
    print(fileData);

    List<String> rows = fileData.split("\n");
    for (int i = 0; i < rows.length; i++) {
      String row = rows[i].trim(); // Trim whitespace
      if (row.isEmpty) continue;  // Skip empty rows

      List<String> itemInRow = row.split(",");
      if (itemInRow.length < 7) {
        print("Skipping invalid row: $row");
        continue; // Skip rows with insufficient data
      }

      try {
        Node node = Node(
          int.parse(itemInRow[0].trim()),
          int.parse(itemInRow[1].trim()),
          int.parse(itemInRow[2].trim()),
          itemInRow[3].trim(),
          itemInRow[4].trim(),
          itemInRow[5].trim(),
          itemInRow[6].trim(),
        );
        decisionMap.add(node);
      } catch (e) {
        print("Error parsing row: $row. Exception: $e");
        continue;
      }
    }
  } catch (e) {
    print("Error loading CSV file: $e");
  }

  runApp(
    const MaterialApp(
      home: MyFlutterApp(),
    ),
  );
}

class MyFlutterApp extends StatefulWidget {
  const MyFlutterApp({Key? key}) : super(key: key);
  @override
  State<StatefulWidget> createState() {
    return MyFlutterState();
  }
}

class MyFlutterState extends State<MyFlutterApp> {
  late int id;
  late int nextID;
  String description = "Style of play";
  bool isServerConnected = false;

  @override
  void initState() {
    super.initState();
    initializeServer();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (isServerConnected) {
        setState(() {
          Node current = decisionMap.first;
          id = current.iD;
          nextID = current.nextID1;
          description = current.description;

        });
      }
    });
  }

  void initializeServer() {
    Future.delayed(const Duration(seconds: 2), () {
      setState(() {
        isServerConnected = true; // Simulate server connection
      });
    });
  }

  void buttonHandler() {
    print("Next ID: $nextID, Description: $description");
    setState(() {
      for (Node nextnode in decisionMap) {
        if (nextnode.iD == 1) {
          nextID = nextnode.nextID1;
          description = nextnode.description;
    
          break;
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff3e87c5),
      body: Center(
        child: SizedBox(
          width: MediaQuery.of(context).size.width * 0.8,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                description,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontWeight: FontWeight.w400,
                  fontSize: 34,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 20),
              Text(
                description,
                textAlign: TextAlign.center,
                style: const TextStyle(
                  fontSize: 14,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 40),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  ElevatedButton(
                    onPressed: buttonHandler,
                    child: const Text("Attack"),
                  ),
                  ElevatedButton(
                    onPressed: buttonHandler,
                    child: const Text("Defense"),
                  ),

                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
