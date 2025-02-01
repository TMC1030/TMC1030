void main(List arguments){
  double num1 = double.parse(arguments[0]);
  String operation = arguments[1];
  double num2 = double.parse(arguments[2]);
  print(calculator(num1, num2, operation));
}

//Q9
double calculator(double num1, double num2, String operation){
 double result = 0;
  switch(operation){
    case == "add":
      result = num1 + num2;
    case == "subtract":
      result = num1 - num2;
    case == "multiply":
      result = num1 * num2;
    case == "divide":
      result = num1 / num2;
    default:
      print("Invalid");
  }
  return result;
}