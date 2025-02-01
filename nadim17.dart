import 'dart:io';
import 'dart:math';

void main(){

  String space = ' ';

//print("x" + space * 8 + "y");
print("x\t\t\ty");
  print("------------------");
   
  for (double x = -10; x <= 10; x += 0.5){
    double y = gety(x);
    print("${x.toStringAsFixed(2)}\t\t ${y.toStringAsFixed(2)}");
  }
}

double gety(double x){
  return 3 * x + 2;
}