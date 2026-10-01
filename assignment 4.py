#1. BankAccount Class

class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        # initialize the three attributes here
    #Store the received account_number inside this particular object's account_number
        self.account_number = account_number
        self.owner_name=owner_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("Amount deposited: ",amount)

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print("Amount withdrawn: ",amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("current balance: ",self.balance)

acc1=BankAccount(101,"Shivam",self.balance)

acc1.check_balance()
acc1.deposit(1000)
acc1.withdraw(2000)
acc1.check_balance()
acc1.deposit(3000)
acc1.withdraw(4000)