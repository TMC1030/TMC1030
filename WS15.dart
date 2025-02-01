import 'dart:io';
import 'dart:math';

void main(){
  sayName("Marshal");
  studentDetails();
  euro();
  temperature();
  circle();
  order();
  customers();
}

//Q1
void name() {
  sayName("Marshal");
}

void sayName(String name){
  print(name + " is a my name");
}

//Q2

void studentDetails() {
  print("My name is Marshal" + "\n My student number is 2245699" + "\n My student email address is up2245699@myport.ac.uk");
}

//Q3

double euroToPounds(double euros) {
  const double conversionRate = 0.86;
  return euros * conversionRate;
}  
void euro() {
  double eurosAmount = 20;
  double poundsAmount = euroToPounds(eurosAmount);
  print('$eurosAmount euros is equal to $poundsAmount pounds.');
}

//Q4

double fahrenheitToCelsius(double fahrenheit) {
  return (fahrenheit - 32) * 5/9;
}
void temperature(){
  double fahrenheitTemperature = 100;
  double celsiusTemperature = fahrenheitToCelsius(fahrenheitTemperature);
  print('$fahrenheitTemperature fahrenheit is the equalivent of $celsiusTemperature degree');
}

//Q5

void areaOfCircle(){
  print('Enter the radius of a circle:');
  String? radiusInput = stdin.readLineSync(); //stdun.readLineSync() means read a line of input from the user
  double radius = double.parse(radiusInput!); // double.parse isa a method used to convert a floating-point number into an 'double' data type
  double area = pi * pow(radius, 2);
  print('Area:${area.toStringAsFixed(2)}');  //toStringAsFixed(x) == round(number,2) in Python
}

void circumferenceOfCircle() {
  print('Enter the radius of a circle:');
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double circumference = 2 * pi * radius;
  print('Circumference: ${circumference.toStringAsFixed(2)}');
}

void circleInfo() {
  print('Enter the radius of a circle:');
  String? radiusInput = stdin.readLineSync();
  double radius = double.parse(radiusInput!);
  double area = pi * pow(radius, 2);
  double circumference = 2 * pi * radius;
  print('Area: ${area.toStringAsFixed(2)}');
  print('Circumference: ${circumference.toStringAsFixed(2)}');
}

void circle() {
  areaOfCircle();
  circumferenceOfCircle();
  circleInfo();
}

//Q6

void displayBurgerOrder(int numBurger , double pricePerBurger){
  double totalPrice = numBurger * pricePerBurger;

  String burgerEmoji = '';  //Code for EMOJI
  for(int i = 0; i < numBurger; i++){
    burgerEmoji += '🍔';
  }

  print('Your Order');
  print('Number of bruger:$burgerEmoji');
  print('The price of each bruger:$pricePerBurger');
  print('Total:${totalPrice.toStringAsFixed(2)}');
}
void order() {
  displayBurgerOrder(3, 5.89);
}

//Q7
void customers() {
  stdout.write("How much does a burger cost? ");
  String? userInputBurgerCost = stdin.readLineSync();
  stdout.write("How much pounds do you have saved? ");
  String? userInputSavingPounds =stdin.readLineSync();
  stdout.write("How many pennies do you have saved? ");
  String? userInputSavingPennies = stdin.readLineSync();
  int numberBurgers = howManyBurgers(userInputBurgerCost!, userInputSavingPounds!, userInputSavingPennies!);
  print("You can purchase $numberBurgers burgers!");
}

int howManyBurgers(String priceBurger, String userSavingPounds, String userSavingPennies) {
  int totalPennies = int.parse(userSavingPennies);
  int addToPounds = totalPennies ~/ 100;
  int totalPounds = int.parse(userSavingPounds);
  totalPounds = totalPounds + addToPounds;
  totalPennies = totalPennies - (100 * addToPounds);
  String totalSaving = "$totalPounds.$totalPennies";
  return double.parse(totalSaving) ~/ double.parse(priceBurger);
}