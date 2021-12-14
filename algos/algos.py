from random import randint
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
#    n =len(arr)
#    for i in range(n):
#        rand = randint(i, n-1)
#
#        arr[i], arr[rand] = arr[rand], arr[i]
#
#    print(arr)
#
#shuf([20,16,5,41,3,2,1])


#def sky_hi(arr):
#    for i in range(len(arr)):
#        if arr[i] > 0:
#            num = arr[i]
#    new_arr = [num]
#    for i in range(1, len(arr)):
#        if num < arr[i]:
#            num = arr[i]
#            new_arr.append(num)
#    print(new_arr)
#sky_hi([-1,2,3,1,1,2])


#def zip_it(arr1, arr2):
#    new_arr = []
#    for i in range(0,len(arr1)):
#        new_arr.append(arr1[i])
#    for i in range(0, len(arr2)):
#        new_arr.append(arr2[i])
#
#    sorted_numbers = sorted(new_arr)
#    print(sorted_numbers)
#
#zip_it([1,3,4,7,9], [20,40,60,80])


#String to do 1

#def remove_blanks(str):
#    print(str.replace(" ", ""))
#    
#
#remove_blanks(" Pl ayTha tF u nkyM usi c ")


