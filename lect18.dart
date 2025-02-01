import 'bank.dart';

void main() {
  BankAccount account = BankAccount('Alice');
  print(account.balance); // 0.0
  account.balance = -50.0;
  print(account.balance); // -50.0
}
