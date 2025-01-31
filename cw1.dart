import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:core';

List<Node> decisionMap = [
  Node(1,2,3,"Style of play","Choose Tactics","Attack","Defense"),
  Node(2,4,5,"Attack","Ball Possession","Pass","Run"),
  Node(4,8,9,"Opponent Presses","Response","Dribble","Go straight the opponent"),
  Node(5,10,11,"Opponent Tackle","Lost the ball","",""),
  Node(8,16,17,"Pass to teammate","Type of pass","Long pass","Short pass"),
  Node(7,14,15,"Shot on Goal","Direction","Left","Right"),
  Node(16,-1,-1,"Long pass","Bad pass", "",""),
  Node(17,-1,-1,"Short pass","Good pass","",""),
  Node(9,-1,-1,"Go straight the opponent","Lost the ball","", ""),
  Node(10,-1,-1,"Penalty awarded","","", ""),
  Node(11,-1,-1,"Loss of possession","","", ""),
  Node(14,-1,-1,"Goal","1-0", "", ""),
  Node(15,-1,-1,"Miss","0-0", "", ""),];
  
class Node {
  final int iD;
  final int nextID1;
  final int nextID2;
  final String question;
  final String description;
  final String option1;
  final String option2;

  // Constructor for the Node class
  Node(
    this.iD,
    this.nextID1,
    this.nextID2,
    this.question,
    this.description,
    this.option1,
    this.option2,
  );
}


void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  String csv = "sheet1.csv"; // Path to CSV file

  try {
    String fileData = await rootBundle.loadString(csv);
    print(fileData);

    List<String> rows = fileData.split("\n");
    for (int i = 0; i < rows.length; i++) {
      String row = rows[i].trim(); 
      if (row.isEmpty) continue; 

      List<String> itemInRow = row.split(",");
      if (itemInRow.length < 7) {
        print("Skipping invalid row: $row");
        continue; 
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
  String question = "";
  String option1 = "";
  String option2 = "";
  String description = "Choose Tactics";
  bool isServerConnected = false;

  @override
  void initState() {
    super.initState();

    Node current = decisionMap.first;
    id = current.iD;
    nextID = current.nextID1;
    question = current.question;
    option1 = current.option1;
    option2 = current.option2;

    initializeServer();
  }

  void initializeServer() {
    Future.delayed(const Duration(seconds: 2), () {
      setState(() {
        isServerConnected = true; 
      });
    });
  }

  void buttonHandler(bool isAttack) {
    setState(() {
      for (Node node in decisionMap) {
        if (node.iD == nextID) {
          nextID = isAttack ? node.nextID1 : node.nextID2;
          question = node.question;
          option1 = node.option1;
          option2 = node.option2;
          description = node.description;
          break;
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    // Ensure decision map is connected
    if (!isServerConnected || decisionMap.isEmpty) {
      return Scaffold(
        backgroundColor: const Color(0xff3e87c5),
        body: Center(
          child: CircularProgressIndicator(),
        ),
      );
    }

    return Scaffold(
      backgroundColor: const Color(0xff3e87c5),
      body: Center(
        child: SizedBox(
          width: MediaQuery.of(context).size.width * 0.8,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                question,
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
                    onPressed: () => buttonHandler(true), // Attack
                    child:Text(option1),
                  ),
                  ElevatedButton(
                    onPressed: () => buttonHandler(false), // Defense
                    child:Text(option2),
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
