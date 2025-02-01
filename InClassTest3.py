class BankAccount:
    def __init__(self):
        self.balance = 100

    def getBalance(self):
        return self.balance

    def processTransaction(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("You are no longer in credit. Please see the bank manager")

def testBankAccount():
    standardCharted = BankAccount()
    standardCharted.processTransaction(70)
    print(standardCharted.getBalance())
    standardCharted.processTransaction(40)
    print(standardCharted.getBalance())

testBankAccount()

#Task 2

class BankAccount2:
    def __init__(self):
        self.balance = 100
        self.overdraftUsed = 0

    def getBalance(self):
        return self.balance

    def processTransaction(self, amount):
        self.balance -= amount
        if self.balance < 0 or self.balance < -50:
            print("You are no longer in credit. Please see the bank manager")
        else:
            print("Payment not authorised. You do not have enough money fo that")

    def aarangeOverdraft(self):
        self.overdraftUsed = True

def testBankAccount2():
    standardCharted = BankAccount2()
    #standardCharted.processTransaction(70)
    #print(standardCharted.getBalance())
    #standardCharted.processTransaction(40)
    #print(standardCharted.getBalance())

    print(standardCharted.aarangeOverdraft())
    standardCharted.processTransaction(40)
    print(standardCharted.getBalance())


testBankAccount2()