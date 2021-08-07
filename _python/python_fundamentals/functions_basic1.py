##1
#def a():
#    return 5
#print(a())
#
##The output should be 5
#
##2
#def a():
#    return 5
#print(a()+a())
#
##The output should be....
##10
#
##3
#def a():
#    return 5
#    return 10
#print(a())
#
##The output should be...
##5 due to the algo stopping at the first return statement
#
##4
#def a():
#    return 5
#    print(10)
#print(a())

#The output should be...
#10
#5
# I got this one incorrect due to forgetting the problem stops at the first return statement

#5
#def a():
#    print(5)
#x = a()
#print(x)

#The output should be...
#5
# I got it wrong, why does it say none?

#6
#def a(b,c):
#    print(b+c)
#print(a(1,2) + a(2,3))
#because the function is not returning any value it will print...
#3
#5
#but will catch an error with print(a(1,2) + a(2,3))

#7
#def a(b,c):
#    return str(b)+str(c)
#print(a(2,5))

#8
#def a():
#    b = 100
#    print(b)
#    if b < 10:
#        return 5
#    else:
#        return 10
#    return 7
#print(a())

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

