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

