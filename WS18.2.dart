void main() {
  Person alice = Person('Alice', 20);
  alice.age = 21;
//  print('Alice is ${alice.age} years old');

//  print('Next year, Alice will be ${alice.ageNextYear()} years old');
//  print('Alice has a valid name: ${alice.hasValidName()}');
//  print('Is Adult:${alice.isAdult()}');

//  print(alice);
//  print(alice.runtimeType);

  Rectangle rec1 = Rectangle(0, 0, 5, 10);
//  print(rec1.getArea());
//  print(rec1.getPerimeter());
//  print(rec1);

  Student student = Student('Steve', 20, '01234567890');
//  print(student);

  Product product = Product('Ribeye', 7.32, true);
  Product product1 = Product('Eggs', 1.5, false);

  product.discountedPrice();
  print(product);
  print(product1);

}

class Person {
  String name = 'unknown';
  int age = 0;

  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }

  int ageNextYear() {
    return age + 1;
  }

  bool isAdult() => age > 18;

  bool hasValidName() {
    if (name.length > 2 && name.length < 100) {
      return true;
    } else {
      return false;
    }
  }

  String toString() {
    return 'Person(name: $name, age: $age)';
  }
}

class Student extends Person {
//  String? name;
  int level = 4;
  String? _phoneNumber;

  Student(String name, int age, this._phoneNumber) : super(name, age);

  void graduate() {
    level++;
  }

  String greet() => 'Hello, $name!';

  String get phoneNumber {
    String lastFourDigits = _phoneNumber!.substring(6);
    return '***-***-$lastFourDigits';
  }

  void set phoneNumber(String phoneNumber) {
    if (phoneNumber.length == 10) {
      _phoneNumber = phoneNumber;
    }
  }

  String toString(){
    return '${super.toString()},level:$level,phone number:$phoneNumber,is student:${isAdult()}';
  }
}

class Module {
  String name;
  int credits;

  Module(this.name, {this.credits = 20});
}

class Course {
  String name;
  List<Module> modules = [];
  int totalCredits = 0;
  int _maxCredits = 120;

  Course(this.name);

  void addModule(Module module) {
    if (totalCredits + module.credits <= maxCredits) {
      modules.add(module);
      totalCredits += module.credits;
    }
  }

  int get maxCredits => _maxCredits;

  String toString() {
    String output = 'Course name: $name, Modules:\n';
    for (Module module in modules) {
      output += '  ${module.name} (${module.credits} credits)\n';
    }
    output += 'Total credits: $totalCredits';
    return output;
  }
}

class Shape {
  double x = 0.0;
  double y = 0.0;

  Shape(this.x, this.y);

  void move(double dx, double dy) {
    x += dx;
    y += dy;
  }

  String toString() => 'x: $x, y: $y';
}

class Circle extends Shape {
  double radius = 0.0;

  // Circle(double x, double y, double radius) : super(x, y) {
  //   this.radius = radius;
  // }

  Circle(double x, double y, this.radius) : super(x, y);

  String toString() => '${super.toString()}, radius: $radius';
}

class Rectangle extends Shape{
  double width = 0.0;
  double length = 0.0;

  Rectangle(double x, double y, this.width, this.length):super(x,y);

  double getArea(){
    return width * length;
  }

  double getPerimeter(){
    return (width + length) * 2;
  }

  String toString() => '${super.toString()}, width: $width, length: $length';

}

class Product{
  String name = '';
  double price = 0.0;
  bool? clubcardItems = false;

  Product(this.name, this.price, this.clubcardItems);

  double discountedPrice() => price * 0.85;

  String toString() => ' name:$name, price:$price, clubcardItems:$clubcardItems';
}