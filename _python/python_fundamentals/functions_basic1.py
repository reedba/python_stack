#1
def a():
    return 5
print(a())

#The output should be 5

#2
def a():
    return 5
print(a()+a())

#The output should be....
#10

#3
def a():
    return 5
    return 10
print(a())

##The output should be...
##5 due to the algo stopping at the first return statement

#4
def a():
    return 5
    print(10)
print(a())

#The output should be...
#10
#5
# I got this one incorrect due to forgetting the problem stops at the first return statement

#5
def a():
    print(5)
x = a()
print(x)

#The output should be...
#5
# I got it wrong, why does it say none?

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#because the function is not returning any value it will print...
#3
#5
#but will catch an error with print(a(1,2) + a(2,3))

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#This will display 25 in the console

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# will print....
#-100
#-10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#This will print.....
#-7
#-14
#-None + None>Its actually 21-this algo returned a value

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#This will return to the console....
#-8 

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#This will print...
#-500
#-500
#-300
#-500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#-500
#-300-This one is 500, I got this one is incorrect
#-300
#-500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#-500
#-500
#-300>This print does not show up, It just stores the value to the b variable
#-300>This print does not show up, It just stores the value to the b variable
#-300
#-300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#-1
#-3
#-2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#-1
#-3
#-5
#-10



