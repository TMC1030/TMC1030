class BankAccount {
  String owner;
  double _balance = 0.0;

  BankAccount(this.owner);

  double get balance{
    return _balance;
  }

  void set balance(double amount){
    if (amount >= 0){
      _balance = amount;
    }
  }
}
