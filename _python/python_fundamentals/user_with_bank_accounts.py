class BankAccount:
	
    def __init__(self, int_rate, account): 
        self.account = account
        self.int_rate = int_rate
        self.interest = 0
        self.balance = 0
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    
    def deposit(self, amount):
        self.balance+= amount
        return self
	
    
    def yield_interest(self):
        if self.balance > 0:
            self.interest += self.balance * self.int_rate
            self.deposit(self.interest)
        else:
            self.balance -= 5.00

Brandon = BankAccount(.003,1)

Brandon.account
Brandon.deposit(500).withdraw(200).deposit(500).yield_interest()
print(Brandon.balance)

class User:

    def __init__(self, Name):
        self.Name = Name
        self.interest = 0
        self.balance = 0

    def make_deposit(self, bankaccount = BankAccount("default","default")):
        self.balance += BankAccount.balance



Checking = User("Brandon")
