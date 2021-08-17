


#class User:
#    def _init_(self, name, email):
#        self.name = name
#        self.email = email
#        self.account_balance = 0
#
#    def make_deposit(self, amount):
#        self.account_balance+=amount
#
#guido = User()
#monty = User()
#guido = User("Guido van Rossum", "guido@python.com")
#print(guido.name)	# output: Guido van Rossum

#class User:		# declare a class and give it name User
#    def __init__(self):
#        self.name = "Michael"
#        self.email = "michael@codingdojo.com"
#        self.account_balance = 0
#
#    def make_deposit(self, amount):
#        self.account_balance += amount
#
#    def make_withdrawal(self, amount):
#        self.account_balance -= amount
#
#
#guido = User()
#monty = User()
#
#print(guido.name)
#print(monty.name)
#
#guido.name = "Guido"
#monty.name = "Michael"
#
#print(guido.name)
#print(monty.name)
#
#guido.make_deposit(100)
#guido.make_withdrawal(50)
#monty.make_deposit(100)
#print(guido.account_balance)	# output: 300
#print(monty.account_balance)	# output: 50

class User:
    def __init__(self,name, hair_color, eye_color):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.display_user_balance = 0
        
        
    def make_withdrawal(self,amount):
        self.display_user_balance -= amount
        return self

    def make_deposit(self, amount):
        self.display_user_balance+=amount
        return self

    def make_transfer(self, transfer_amount, user2):
        self.make_withdrawal(transfer_amount)
        user2.make_deposit(transfer_amount)
        return self
        
        


Brandon = User("Brandon", "Blonde", "Blue")
Noah = User("Noah","Blonde","Blue")
Jackie = User("Jackie", "Brown", "Blue")



Brandon.make_deposit(100).make_deposit(11000).make_deposit(300).make_withdrawal(50).make_transfer(10000, Jackie)
Jackie.make_transfer(1000,  Noah).make_deposit(300).make_withdrawal(200)
Noah.make_withdrawal(200).make_deposit(100).make_withdrawal(100).make_withdrawal(50)
Brandon.make_deposit(500).make_transfer(10000,Noah)
Noah.make_deposit(1000).make_transfer(5000,Jackie)

print(Jackie.display_user_balance)
print(Brandon.display_user_balance)
print(Noah.display_user_balance)





