#1
numlist = []
def countdown(num):
    for num in range(num, -1, -1):
        numlist.append(num)
        print(numlist)
countdown(10)

#2
def print_and_return(list):
    print(list[0])
    return list[1]

print_and_return([4,6])

#3
def first_plus_length(list2):
    print(list2[0]+len(list2))

first_plus_length([7,2,3,4,5])

#4
new_list = []
def  values_greater_than_second(list3):
    for x in list3:
        if list3[1] < x:
            new_list.append(x)
            print(new_list)

values_greater_than_second([1,2,5,0,3])

#5
def length_and_value(a,b):
    for x in range(0, b, 1 ):
        print(a)

length_and_value(1,20)