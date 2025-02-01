import 'dart:io';
import 'dart:math';

void main(){
  guessingGame();
}

void guessingGame(){
  var intValue = Random().nextInt(100);
  int guess = 0;
  
  while(guess != intValue){
    print('Guess a number:');
    String? estnumber = stdin.readLineSync();
    int number = int.parse(estnumber!);
    if (number > intValue){
      print('Number too High'); 
    } else if (number < intValue){
      print('Number too Low');
    } else {
      print('Good guess! Correct!');
      break;
    } 
  } 
}