#1
new_list1 = []
def biggie_size(list1):
    for x in list1:
        if x > 0:
            new_list1.append("big")
        else :
            new_list1.append(x)
            print(new_list1)

biggie_size([-1, 3, 5, -5])

#2
def count_positives(list2):
        count_two = 0
        for x in list2:
            if x > 0:
                count_two+=1
        list2[-1]=count_two
        print(list2)

count_positives([-1,6,-1,-2,4,1])

#3
def sum_total(list3):
    total = 0
    for x in list3:
        total+=x
        print(total)

sum_total([6,3,-4])

#4
def average(list4):
    total = 0
    for x in list4:
        total+=x
        continue
    avg = total/len(list4)
    print(avg)

average([1,2,3,8])

#5
def length(list5):
    print(len(list5))

length([37,2,1,-9,20])
length([])

#6
def minimum(list6):
    num = 0
    for x in list6:
        if x < num:
            num = x
    print(num)

minimum([37,-2,1,-9])

#7
def maximum(list7):
    num = 0
    for x in list7:
        if x > num:
            num = x
        if x == []:
            print("false")
    print(num)
        #need help with aquiring false

maximum([37,2,40,-9])
maximum([]) 

#8
def ultimate_analysis(list8):
        sumTotal = 0
        average = 0
        minimum = 0
        maximum = 0
        length = len(list8)
        for x in list8:
            sumTotal+=x
            average = sumTotal/len(list8)
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x

        newList = [sumTotal, average, minimum, maximum, length]
        print(newList)


ultimate_analysis([37,2,40,-9])

#9
def reverse_list(list9):
    list9.reverse()
    print(list9)

reverse_list([1,2,3,4,5])
