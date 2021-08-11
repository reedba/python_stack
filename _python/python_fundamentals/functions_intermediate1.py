import random
def randInt(max=100,min=0):
    integer = max - min
    num = round(random.random()*integer+min)
    return num
    
		


print(randInt(max = 40, min=10))
print(randInt(max=50)) 	# should print a random integer between 0 to 50
print(randInt(min=50)) 	# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
