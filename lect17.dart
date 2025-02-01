void main(){
  Map<String, int> marks = {
    'Programming': 67,
    'Networks': 90,
    'Core Computing': 54
  };

  print(marks['Networks']);  // 90

  marks['Networks'] = 40;
  print(marks['Networks']);  // 40

  marks['Databases'] = 78;
  print(marks);
  // {Programming: 77, …, Database: 78}

}