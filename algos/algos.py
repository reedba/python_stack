import random
import math

#Fundamentals to do 1

#def mult_three():
#    for i in range(-300,0,3):
#        if i == -3 or i == -6:
#            pass
#        else:
#            print(i)
#
#mult_three()
#
#def whil():
#    i = 2000
#    while i < 5280:
#        i += 1
#        print(i)
#
#whil()
#
#def dojo_way(x,y):
#    for i in range(x,y):
#        if i%10 == 0:
#            print('Dojo')
#        elif i%5 == 0:
#            print('Coding')
#        else:
#            print(i)
#        
#
#dojo_way(1,100)

#def flex_count(low, high, mult):
#    for i in range(high, low, -mult):
#        print(i)
#
#flex_count(2,9,3)

#Fundamentals to do 2

#def countdown(num):
#    arr = []
#    for i in range(num,0,-1):
#        arr.append(i)
#        
#    print(len(arr))
#    return arr

#countdown(20)

#def sum_arr(arr):
#    for i in arr:
#        sum = arr[0] + len(arr)
#    return sum
#
#sum_arr([1,2,6,9,10,11])

#def val_greater(arr):
#    count = 0
#    for num in range(0,len(arr)):
#        num1 = arr[num]
#        num2 = arr[num+1]
#        if num1 < num2:
#            count+=1
#        print(arr[num])
#        print(arr[num+1])
#        print('-------------------------')
#        else:
#                continue
#    print(count)     
    

#val_greater([9,3,10,20,33,1,2,4])


#Arrays to do 1
#def shuf(arr):
#    newarr = []
#    for i in range(0, len(arr)):
#            i=random.randint(1,len(arr))
#            if arr[i] not in newarr: 
#                newarr.append(arr[i])
#                arr.pop()
#    
#    print(newarr)
#
#shuf([20,16,5,41,3,2,1])


#def sky_hi(arr):
#    #loop throug the array
#    #check if the number next to it is
#    pass

# String to do 1

def remove_blanks(str):
    print(str.join(""))
    

remove_blanks(" Pl ayTha tF u nkyM usi c ")


