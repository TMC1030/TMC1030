import 'dart:math';

void main(){

  double gradient;
  double yIntercept = 2;
  double y;

  for(double x = -2.001; x < 5; x += .01){
      //y = getY(gradient, yIntercept, x);
      //print('(${x.toStringAsFixed(2)},${y.toStringAsFixed(2)})');
      y = getY2(x);
      gradient = gradientFunction(x);
      print("x = ${x.toStringAsFixed(2)} | y = ${y.toStringAsFixed(2)} | gradient = ${gradient.toStringAsFixed(2)}");
  }

  //double y = getY(gradient, yIntercept, x);
  //print("y = $y");

}

//y=3x+2

double getY(double gradient, double yIntercept, double x){
  double y = gradient * x + yIntercept;
  return y;

}

double getY2(double x){
  //3x^2 + x - 5;
  return 3* pow(x, 2) + x - 5;
}

double gradientFunction(double x){
  //6x + 1
  return 6 * x + 1;
}