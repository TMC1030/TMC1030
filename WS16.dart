import 'dart:math';

//Q1
void main(){
  print(maxNumbers(4,3));
  print(daysInMonth(2));
  heartMonitor(21, 160);
  basicCalculator(10, 2, "Add");
  isPrime(3);
}

int maxNumbers(int num1, int num2){
//  if (num1 >= num2){
//    return num1;
//  } else {
//    return num2;
//  }
      return max(num1, num2);
}

//Q2
List<int> thirtyOneDays = [1,3,5,7,8,10,12];
List<int> thirtyDays = [4,6,9,11];

int daysInMonth(int month){
  if (thirtyOneDays.contains(month)){
    return 31;
  } else if(thirtyDays.contains(month)){
    return 30;
  } else {
    return 28;
  }
}

//Q3
void sayName(String name) => print(name);

double euroToPounds(double euros) => euros * 0.86;

double fahrenheitToCelsius(double fahrenheit) => (fahrenheit - 32) * 5/9;

//Q4
void heartMonitor(int age, int bpm){
  switch(age){
    case <= 20:
      if(bpm > 170){
        print('High heart rate for 20-40!');
      }
    case <= 40:
      if(bpm > 155){
        print('High heart rate for 21-40!');
      }
    case <= 60:
      if(bpm > 140){
        print('High heart rate for 41-60!');
      }
    case <= 80:
      if(bpm > 130){
        print('High heart rate for 61-80!');
      }
    case >= 60:
      if(bpm > 100){
        print('High heart rate for 81+!');
      }
    default:
        print('High heart rate for $age year old!');
  }
}

//Q5
double basicCalculator(double num1, double num2, String operation){
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

//Q6
bool isPrime(int num){
  for (int i = 2; i < num; i++){
    if (num % i == 0){
      return false;
    } else{
      
    }
  }
  return true;
}

//Q7
int gcd(int num1, int num2){
  int a = num1;
  int b = num2;

  while (a != b){
    if (a > b){
      a = a - b;
    }else{
      b = b - a;
    }
  }
  return a;
}

//Q8
void customisedGreeting(int time){
  switch(time){
    case > 600 && <= 1200:
      print('Have a great morning!');
    case > 1200 && <= 1800:
      print('Have a great afternoon!');
    case > 1800:
      print('Have a great evening!');
  }
}

//Q9(calculator)

//Q10(game)