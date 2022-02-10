import random
import math


#def two_fivefive():
#    for i in range(1,256,1):
#        print(i)
#
#two_fivefive()

#def odd(x,y,z):
#    for i in range(x,y,z):
#        print(i)
#
#odd(1,1000,2)   

# Print Sum
#Write a program that would print the sum of all the odd numbers from 1 to 5000

#def sum_odd(x,y,z):
#    sum = 0
#    for i in range(x,y,z):
#        if i % 2 != 0:
#            sum = sum + i
#        print(i)
#    print(sum)
#
#sum_odd(1,5000,2)

#Iterating Through the Array
#Given an array X say [1,3,5,7,9,13], write a program that would iterate through each member of the array and print each value on the #screen.  Being able to loop through each member of the array is extremely important. Do this over and over (under 2 minutes) before #moving on to the next algorithm challenge.

#def array(arr):
#    for i in arr:
#        print(i)
#
#
#array([1,3,5,7,9,13])

#Assignment: Find Max
#Given an array with multiple values (e.g. [-3, 3, 5, 7]), write a program that prints the maximum number in the array. (The best way #to do this is to have the computer go through each number, one at a time, and to update the value in a variable called 'maximum' (or #whatever you want to name the variable);  imagine that if I gave you no number and asked you what a maximum number is.  What would #you say?  Say the first number I gave you was -3 and asked you what a maximum number is.  What would you say? Say the next number I #gave you was 3 and asked you again what a maximum number now is.  What would you say?  Have the computer imitate this behavior of #updating the maximum number as you iterate through each number in the array).  Again you're not to use any of the pre-built #functions 


#def find_max(array):
#    max = 0
#    for i in array:
#        if max < i:
#            max = i
#    print(max)
#
#find_max([-3, 3, 5, 4])

#Find Average
#Given an array with multiple values (e.g. [1,3,5,7,20]), write a program that prints the average of the values in the array.  Again #you're not to do this by using of any of the pre-built functions in Javascript.  Again iterate through each number in the array and #update the 'average' as the program retrieves each number in the array.#


#def find_average(array):
#    sum = 0
#    for i in array:
#        sum+=i
#    avg = sum / len(array)
#    print(avg)
#
#find_average([1,3,5,7,20])

# Array With Odd Numbers
#Write a program that creates an array 'Y' that contains all the odd numbers between 1 to 255. When the program is done, 'y' should #have the value of [1, 3, 5, 7, ... 255]. Again, make sure you come up with a simple base case and write instructions to solve that #base case first and then test your instructions for other complicated cases. (you can do this using a simple for loop.  You are #allowed to use .push method)


#def arr_odd(x,y,z):
#    a = []
#    for i in range(x,y+1,z):
#        a.append(i)
#    print(a)
#        
#
#arr_odd(1,255,2)

#Greater Than Y
#Write a program that takes an array and returns the number of values in that array whose value is greater than y. For example, if #array = [1,3, 5, 7] and y = 3, after your program is run it will print 2 (since there are two values in the array whose value is #greater than 3).  Again make sure you come up with a simple base case and write instructions to solve that base case first and then #test your instructions for other complicated cases. You can use a count function with this assignment.

#def greater_y(y, arr):
#    count = 0
#    for i in arr:
#        if i > y:
#            count+=1
#    print(count)
#
#greater_y(3,[1,3, 5, 7])

#Square the Values
#Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that squares each value in the array.  When the program is done x should have values that have been squared (e.g. [1, 25, 100, 4]).  You're not to use any of the pre-built function in Javascript.  You could for example square the value by saying x[i] = x[i] * x[i];
#

#def square(arr):
#    newarr = []
#    for i in arr:
#        num = i * i
#        newarr.append(num)
#    print(newarr)
#
#
#square([1, 5, 10, -2])

#Eliminate Negative Numbers
#Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that replaces any negative number with the value #of 0.  When the program is done x should have no negative values (e.g. [1, 5, 10, 0]).


#def elim_neg(arr):
#    newarr = []
#    for i in arr:
#        if i < 0:
#            newarr.append(0)
#        else:
#            newarr.append(i)
#    print(newarr)
#
#elim_neg([1,5, 10, -2])

#Max, Min, and Average
#Given an array x (e.g. [1,5, 10, -2]), create an algorithm (sets of instructions) that prints the maximum number in the array, #minimum value in the array as well as the average values in the array. 


#def max_min_avg(arr):
#    max = 0
#    min = 0
#    count = 0
#    for i in arr:
#        count+=i
#        if i < min:
#            min = i
#        if i > max:
#            max = i
#    avg = count / len(arr)
#    print(max)
#    print(min)
#    print(avg)
#
#max_min_avg([1,5, 10, -2])

#Shifting the values in the array
#Given an array x (e.g. [1,5, 10, 7, -2]), create an algorithm (sets of instructions) that shifts each number by one (to the front).  #For example when the program is done x (assuming it was [1,5,10,7,-2]) should become [5,10,7,-2, 0]. 
#

#def shift(arr):
#    for i in range(0,len(arr)-1):
#        arr[i] = arr[i+1]
#    
#    arr[len(arr)-1] = 0
#    print(arr)
#
#
#shift([1,5, 10, 7, -2])

#Number to String
#Write a program that takes an array of numbers and replaces any number that's negative to a string called 'Dojo'. For example if array = [-1, -3, 2] after your program is done array should be ['Dojo', 'Dojo', 2].
#

#def num_to_string(arr):
#    newarr = []
#    for i in range(0, len(arr)):
#        if arr[i] < 0:
#            newarr.append('Dojo')
#        else:
#            newarr.append(arr[i])
#    print(newarr)
#
#
#num_to_string([-1, -3, 2])

#Random Array
#Create an array X and fill the array with 10 values, each value being a random integer between 0 to 100.  For example when your program is done, X could be something like this: [35, 15, 3, 39, 53, 93, 25, 39, 59, 21].
#

#def rand_arr(x,y):
#    newarr = []
#    for i in range(x,y):
#        newarr.append(math.floor(random.random()*100))
#    print(newarr)
#
#rand_arr(0, 10)

#Swapping two values
#Write a program that takes an array of numbers and returns an array where the first and last numbers in the array have been switched.For example say x = [2, 3, 5, 7, 6]. By the end of the program x, should be [6, 3, 5, 7, 2]. Do this without creating an empty array.
#   


#def swap(arr):
#    temp = arr[0]
#    arr[0]= arr[len(arr)-1]
#    arr[len(arr)-1] = temp
#    print(arr)
#
#swap([2, 3, 5, 7, 6])

#Reversing
#Given an array X of multiple values (e.g. [-3,5,1,3,2,10]), write a program that reverses the values in the array.  Once your program is done X should be in the reserved order.  Do this without creating a temporary array.  Also, do NOT use the reverse method but find a way to reverse the values in the array (HINT: swap the first value with the last; second with the second to last and so forth).
#

#def reverse(arr):
#    for i in range(0, 3):
#        temp = arr[i]
#        arr[i] = arr[len(arr)-1-i]
#        arr[len(arr)-1-i] = temp
#        print(arr)
#
#reverse([-3,5,1,3,2,10])

#Insert X in Y
#Write a program that inserts a new number X at an index Y. For example if array = [1, 3, 5, 7] and X = 10, and Y = 2, by the end of your program array should be [1, 3, 10, 5, 7] (in other words we added '10' on index 2). Check the output of your array once your program is completed to make sure it's working correctly.
#

#def insert(x,y,arr):
#    arr.append(0)
#    for i in range(len(arr)-1,y, -1):
#        arr[i] = arr[i-1]
#    arr[y] = x
#    print(arr)
#
#insert(10, 2, [1, 3, 5, 7])

#Removing Negatives
#Given an array of multiple values (e.g. [0, -1, 2, -3, 4, -5, 6]), write a program that removes any negative values in that array.  Once your program is done, the array should be composed of only the non-negative numbers, in their original order.  Do this without creating a temporary array; only use the pop() method to remove values from the array.
#



#def remove(arr):
#    for num in arr:
#        if num < 0:
#            arr.remove(num)
#    print(arr)
#
#remove([0, -1, 2, -3, 4, -5, 6])


#def count(x,y):
#    for i in range(x,y):
#        print(i)
#
#count(1,256)
#
#
#def odd_num(x,y,z):
#    for i in range(x,y,z):
#        print(i)
#
#odd_num(1,1000,2)


#def add_odd(x,y,z):
#    count = 0
#    for i in range(x,y,z):
#        count+=i
#    print(count)
#
#add_odd(1,5000,2)

#def iterate_arr(arr):
#    for i in arr:
#        print(i)
#
#iterate_arr([1,3,5,7,9,13])

#def max(arr):
#    max = arr[0]
#    for i in arr:
#        if i > max:
#            max=i
#    print(max)
#
#max([-3, 3,9, 5, 7])

#def avg(arr):
#    count = 0
#    for i in arr:
#        count+=i
#    avg = count/len(arr)
#    print(avg)
#
#avg([1,3,5,7,20])

#def odd_arr(x,y,z):
#    new_arr = []
#    for i in range(x,y,z):
#        new_arr.append(i)
#    print(new_arr)
#
#odd_arr(1,256,2)

#def greater(y,arr):
#    count = 0
#    for i in arr:
#        if i > y:
#            count+=1
#    print(count)
#
#greater(3,[1,3, 5, 7])

#def squared(arr):
#    for i in range(0,len(arr)):
#        arr[i] = arr[i]*arr[i]
#    print(arr)
#
#squared([1,5, 10, -2])

#def elim_neg(arr):
#    for i in range(0, len(arr)):
#        if arr[i] < 0:
#            arr[i] = 0
#    print(arr)
#
#elim_neg([1,5, 10, -2])

#def max_min_avg(arr):
#    min = arr[0]
#    max = arr[0]
#    sum = 0
#    for i in range(0,len(arr)):
#        if min > arr[i]:
#            min = arr[i]
#        if max < arr[i]:
#            max = arr[i]
#        sum+=arr[i]
#        avg = sum/len(arr)
#    print(min, max, avg)
#
#
#
#max_min_avg([1,5, 10, -2])

#def shift(arr):
#    temp = arr[0]
#    arr[0]=arr[len(arr)-1]
#    arr[len(arr)-1]=temp
#    print(arr)
#
#shift([1,5, 10, 7, -2])


#def num_string(arr):
#    new_arr = []
#    for num in arr:
#        if num < 0:
#            new_arr.append('Dojo')
#        else:
#            new_arr.append(num)
#    print(new_arr)
#
#num_string([-1, -3, 2])


#def ran(x,y):
#    new_arr = []
#    for i in range(x,y+1):
#        rand_num = math.floor(random.random()*100)
#        new_arr.append(rand_num)
#    print(new_arr)
#
#
#ran(1,10)


#def mult_three():
#    for i in range(-300, 0, 3):
#        if i == -3 or i == -6:
#            pass
#        else:
#            print(i)
#
#mult_three()

#def integers():
#    i = 2000
#    while i < 5280:
#        i += 1
#        print(i)
#
#integers()


#def dojo(x,y):
#    for i in range(x, y):
#        if i % 10 == 0:
#            print('Dojo')
#        elif i % 5 == 0:
#            print('Coding')
#        else:
#            print(i)
#
#
#dojo(1,100)

#def mult(low, high, mult):
#    for i in range(high, low, -mult):
#        print(i)
#
#mult(2,9,3)

#def element(arr):
#    for i in range(len(arr)-1, 0, -1):
#        print(i)
#        
#
#element([5,8,1,3,2,0])

#def sum_first(arr):
#    print(arr[0]+len(arr))
#
#sum_first(['What?',8,1,3,2,0])

#def val_greater(arr):
#    count = 0
#    for i in range(len(arr)-1,-1, -1):
#        if len(arr) > 1:
#            num1 = arr[i-1]
#            num2 = arr[i]
#            if num1 < num2:
#                count+=1
#                print(arr[i])
#        else:
#            print('not long enough')
#    print(f'count = {count}')
#
#
#val_greater([9,3,21,20,33,1,2,4])

#def fit_value(arr):
#    if arr[0] == len(arr):
#        print('Just Right')
#    elif arr[0] < len(arr):
#        print('Too Small')
#    else:
#        print('Too Big')
#    
#
#fit_value([4,5,1])

#def fahrenheight(ftemp):
#
#    num1 = ftemp - 32
#    num2 = 5/9
#    celsius = num1*num2
#    print(celsius)
#
#fahrenheight(23)

#def biggie(arr):
#    for i in range(0, len(arr)):
#        if arr[i] < 0:
#            arr[i] = 'big'
#    print(arr)
#
#biggie([-1,3,5,-5])


#def low_high(arr):
#    num1 = 0
#    num2 = 0
#    for i in range(0, len(arr)):
#        if arr[i] > num1:
#            num1 = arr[i]
#        if arr[i] < num2:
#            num2 = arr[i]
#    print(f'lownum is {num2}')
#    return num1
#    
#
#
#low_high([-1,3,5,-5])

#def this(arr):
#    print(arr[len(arr)-2])
#    for i in range(0, len(arr)):
#        if arr[i]%2 != 0:
#            print(arr[i])
#            return arr[i]
#
#
#this([2,2,2,1,2,2,1])

#def double(arr):
#    for i in range(0, len(arr)):
#        arr[i] = arr[i] + arr[i]
#
#    return arr
#
#
#double([2,2,2,1,2,2,1])

#def count_pos(arr):
#    count = 0
#    for i in range(0, len(arr)):
#        if arr[i] > 0:
#            count+=1
#    arr[len(arr)-1] = count
#    print(arr)
#    return arr
#
#count_pos([-1,9,3,5,-5,10])

#def even_odd(arr):
#    odd_count = 0
#    even_count = 0
#    for i in range(0, len(arr)):
#        if arr[i]%2 != 0:
#            odd_count+=1
#            if odd_count == 3:
#                print('Thats Odd')
#        else:
#            odd_count = 0
#        if arr[i]%2 == 0:
#            even_count+=1
#            if even_count == 3:
#                print('Thats Even More So')
#        else:
#            even_count = 0
#        
#        print(f'odd count is {odd_count}')
#        print(f'even count is {even_count}')
#        
#
#
#even_odd([2,2,2,5,5,-5,10,10,10])


def zip_it(arr):
    # Loop through the array the first time
    for i in range(0, len(arr)):
        #Loop through the array the second time starting at index of 1 (Hence i+1) => meaning it keeps 1 ahead of the original index number
        for j in range(i+1, len(arr)):
            #If the first number at I is greater than J
            if arr[i] > arr[j]:
                #Swap Values in the array
                arr[i], arr[j] = arr[j], arr[i]
                #print the original array
                print(arr)
    
zip_it([7,6,5,4,3,2,1])


def sky_high(arr):
    new_arr = []
    num = 0
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > 0 and arr[i] > num:
                num = arr[i]
                new_arr.append(arr[i])
    print(new_arr)
    

sky_high([0,4,1,9,3,3,3,10])






