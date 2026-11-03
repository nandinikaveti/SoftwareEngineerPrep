class BankAccount:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print("Deposit successful")
        else:
            print("Invalid deposit")

    def withdraw(self, amt):
        if self.balance > amt and amt > 0:
            self.balance -= amt
            print("Withdrawal successful")
        else:
            print("Invalid withdrawal")
        

a1 = BankAccount("Nandini", 2700)
a1.deposit(500)
a1.withdraw(8000)
print(a1.balance)

