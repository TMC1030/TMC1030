void main() {
  Phone Motorola = Phone(24, "Hi, I'm a motorola");
  Phone Blackberry = Phone(13, "Hi, I was a blackberry");

  Network EE = Network();

  EE.addPhone(Motorola);
  EE.addPhone(Blackberry);

  print(Motorola.toString());
  print(Blackberry.toString());

  EE.broadcastMessage("Emergency The World is about to End");

  //print(Motorola.toString());
  //print(Blackberry.toString());
  print(EE.toString());

}

class Phone {
  late int iD;
  late String message;

  Phone(int ID, String message) {
    this.iD = ID;
    this.message = message;
  }

  String sendMessage() {
    return this.message;
  }

  void receiveMessage(String newMessage) {
    this.message = newMessage;
  }

  @override
  String toString() {
    return "Phone ID: ${this.iD} Message: ${this.message}";
  }
}

class Network {
  List<Phone> phones = [];
  void addPhone(Phone phone) {
    phones.add(phone);
  }

  // void addPhone(int ID, String message){
  //   Phone phone = Phone(ID, message);
  //   phones.add(phone)
  // }

  void broadcastMessage(String message) {
    for (Phone phone in phones) {
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