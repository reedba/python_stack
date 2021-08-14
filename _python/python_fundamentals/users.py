


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

    def make_deposit(self, amount):
        self.display_user_balance+=amount


user_one = User("Brandon", "Blonde", "Blue")
user_two = User("Noah","Blonde","Blue")
user_three = User("Jackie", "Brown", "Blue")
user_one.make_deposit(500)
user_one.make_deposit(300)
user_one.make_deposit(200)
user_one.make_withdrawal(900)
user_two.make_deposit(300)
user_two.make_deposit(300)
user_two.make_withdrawal(200)
user_two.make_withdrawal(200)
user_three.make_deposit(2000)
user_three.make_withdrawal(2000)
user_three.make_withdrawal(500)
user_three.make_withdrawal(200)
print(user_one.name)
print(user_two.name)
print(user_three.name)
print(user_one.display_user_balance)
print(user_two.display_user_balance)
print(user_three.display_user_balance)