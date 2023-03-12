class BankAccount:
    def __init__ (self,account_number,balance):
        self.account_number=account_number
        self.balance = balance
        
    def __del__(self):
        print("in destructor")
        
        
acc1=BankAccount(1001,10000)
