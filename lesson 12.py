class Account:
    def __init__(self, full_name, acc_num, phone, balance):  # method/function constructor --> set up info
        self.full_name = full_name
        self.acc_num = acc_num
        self.phone = phone
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully to account ${self.acc_num}.")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds. Balance is ${self.balance}.")
        else:
            self.balance -= amount
            print(f"Amount ${amount} withdrawn successfully from account ${self.acc_num}.")

    def check_balance(self):
        print(f"Balance for account {self.acc_num} is ${self.balance}")

kevo_acc = Account("Kevin Maina", "0001", "0712345678", 1000)
sara_acc = Account("Sara Hassan", "002", "0755555555", 1000)
willy_account = Account("Will Jones", "003", "0744556677", 5000)

kevo_acc.deposit(2000)
kevo_acc.check_balance()
kevo_acc.withdraw(500)
kevo_acc.check_balance()

sara_acc.deposit(1000)
sara_acc.check_balance()
sara_acc.withdraw(700)
sara_acc.check_balance()

willy_account.deposit(1000)
willy_account.check_balance()
willy_account.withdraw(3000)
willy_account.check_balance()
