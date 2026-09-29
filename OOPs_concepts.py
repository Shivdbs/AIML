class BankAccount:
    def __init__(self,name,balance,account):
        self.name=name   #public
        self.__balance=balance
        self._account=account

    def get_balance(self):  #getter function
        return self.__balance

    def set_balance(self,newBalance):   #setter function
        self._
acc1=BankAccount("Rahul Kumar",100_000)
print(acc1.name,acc1.balance)