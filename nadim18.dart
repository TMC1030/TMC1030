void main(){

  Phone phone1 = Phone(34343, 'This is my first phone');
  Phone phone2 = Phone(6, 'This is my second phone');

//print(phone1.toString());
//print(phone2.toString());

  Network EE = Network();
  EE.addPhone(phone1);
  EE.addPhone(phone2);

  print(EE);

  EE.broadcastMessage("Leave The World Behind");

  print(EE);

}

class Phone{
  int ID;
  String message;

  Phone(this.ID,this.message);
  
  String sendMessage(){
    return this.message;
  }

  void receiveMessage(String newMessage){
    this.message = newMessage;
  }

  @override
  String toString() {
    return "Phone ID: ${this.ID} Message: ${this.message}";
  }

}

class Network{
  List<Phone> phones = [];

  void addPhone(Phone phone){
    phones.add(phone);
  }

  void broadcastMessage(String message){
    for(Phone phone in phones){
      phone.receiveMessage(message);
    }
  }

  @override
  String toString() {
    String result = "";
    for (Phone phone in phones) {
      result +=  phone.toString() + "\n"; //"Phone ID: ${phone.iD} Message: ${phone.message}";
    }
    return result;
  }
}