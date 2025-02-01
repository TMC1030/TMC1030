

void main(){
  print(isValidEmail("up1234567@myport.ac.uk"));
  //print(checkExpress([9,1,5,1,9],10));

  List<double> a = [10.0,12.5,14.0,16.5,15.0,12.0];
  List<double> b = [11.5,12.0,14.0,16.0,15.5,12.0,10.5];

  print(weatherDifference(a));
  print(weatherDifference(b));
}

//Q1
bool isValidEmail(String email){
  if(email.endsWith("@myport.ac.uk")){
    return true;
  }else{
    return false;
  }
}

//Q2
bool checkExpress(List<double> expenditures, double limit){
  for(int i = 0; i < expenditures.length; i++){
    if (expenditures[i] > limit){
      return false;
    }
  }
  return true;
}

//Q3
double weatherDifference(List<double> temperatures){
  if (temperatures.last > temperatures.first){
    return(temperatures.last - temperatures.first);
  }else{
    return(temperatures.first - temperatures.last);
  }
}