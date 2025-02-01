

void exam(){
  //examReminder("John", 19);

  print(!(5 > 2) && 3 > 1);
}

void greet(String? name) => print("Hello, $name");
 
void examReminder( name, int date){
  print("Dear $name,\n"
          "Don't forget your EXAM ON the ${date}th! ");
}

void main(){
double score = 9;
  switch (score) {
    case 10:
      print('A');
    case 9:
    case 8:
      print('B');
    case 7 || 6:
      print('C');
    // additional cases
    default:
      print('F');

  }

  }

String boolToString(bool? value) {
  switch (value) {
    case true:
      return 'yes';
    case false:
      return 'no';
    default:
      return 'It was null';
  }
}

