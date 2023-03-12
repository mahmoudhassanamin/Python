class BankAccount :
    __balance=None
    def __init__(self,balance):
        self.__balance=balance
        
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        self.__balance-=amount
    def get_balance(self):
        return self.__balance
    
acc1=BankAccount(10000000)

acc1.deposit(9000)
print(f'your balance now : {acc1.get_balance()} E.P')
acc1.withdraw(3000)
print(f'your balance now : {acc1.get_balance()} E.P')

