

class Node: # Singly Linked List Node Class                                   ////////Build the Node first
    def __init__(self, num):
        self.data = num #holds the value for the node
        self.next = None #Pointer to the next node


class SLL: #Singly Linked list class itself                                   ////////Build the list second---------make sure to set tis to a variable
    def __init__(self): #This will start with no nodes
        self.head=None #Head points to the first node

        #All the methods built into the class are below

    
    #Returns the node at the front
    def front(self):
        if self.head == None:#This will return none if the list is empty
            return None
        else:   #else it will return the value at the head if there is data
            return self.head.data


    #This will add a value to the front of the list
    def add_front(self, number):
        new_node = Node(number) #This will create the new_node in the list
        new_node.next = self.head # Connects the new node to the list
        self.head = new_node #The head of the list will now become this new node
        return self.head #This will return the value at the head node


    #This will remove a node from the front of the list
    def remove_front(self):
        if self.head == None: #If the list is empty there is nothing to remove and will return None
            return self.head
        remove_node = self.head #this variable holds the node we will remove
        self.head = remove_node.next #Moves the head of the list to the second node
        remove_node.next = None # This will make the next node in the list None
        return self.head

    def length(self):
        count = 0 #This starts the count at 0
        runner = self.head #runner will be equal to the head first
        while(runner != None): #while runner is not equal to none keep going, once it equals none it will stop
            count+=1 # Every time that the while loop runs it will add 1 to count
            runner = runner.next #Then the nunner will move to the next value
        return count # This will return the count

    def contains(self, val):
        runner = self.head # This will start the runner at the head
        while(runner):#This will continue the while loop while there is a runner
            if runner.data == val: # If the runner is the same as the val argument it will return true 
                return True
            runner = runner.next #This will mmove to the next value in the while loop, If there is no return value yet
        else:
            return False # If the value is not in the list it will return false

    def add_back(self, value): #This function will add a vbalue to the back o the 
        if self.head == None: # If the value at the head id None, then set self.head to the new Node value
            self.head = Node(value)
        else:
            runner = self.head # Or else runner will equal self.head
            while runner.next: #This will start the while loop. While there is a runner.next is not equal to none
                runner = runner.next #This will continue for the runner to be the next value
            runner.next = Node(value) #Once runner.next equals none runner.next will be the next node value submitted
        return self #Then make sure to return self
    
    def display_values(self): #This method will display all the values in the list
        if self.head == None: #If the head of the list has no value then print 'no values'
            print("no values")
        else:
            runner = self.head #or else the runner will be equal to self.head
            while runner != None: #While the runner is not equal to none print the runner data
                print(runner.data)
                runner = runner.next #Then runner will be the next value in the list
        return self #return self so the values will be returned

    def max(self):# This method will find teh max
        if self.head == None:# if the ehad is equla to none print no values
            print('No values')
        else:
            runner = self.head #or else runner is set to the head node
            max = self.head.data #the max variable is set to the head data value
            while runner.next != None: #while loop -> runner.next is not equal to none run the loop
                if runner.next.data > max: # if the runner next data is greater than the max
                    max = runner.next.data # tyhe max varianle will be set to this value
                runner = runner.next #then we will run to the next runner in the list
            print(max)
            return self #make sure to return self

    def min(self):
        if self.head == None: #sets the case to if no value is in the ehad node print no values
            print('No values')
        else:
            runner = self.head # else start the runner at the head node
            min = self.head.data #set the min value to the self . head data value
            while runner.next != None: #while there is a next runner and it is not equal to none run this loop
                if runner.next.data < min: #if the runner data value is less than min
                    min = runner.next.data #set it to the mi variable
                runner = runner.next #move to the next runner in the list
            print(min) #print min variable
            return self #return self


    def avg(self): #This will return the average in the list
        sum = 0 # sum variable equals 0
        count = 0 # The count is equal to 0
        runner = self.head #set the runner to the head node
        while(runner): # while there is a runner run the loop
            sum+=runner.data # add the runner data value to the sum variable
            count+=1 # every time the loop runs add 1, this counts how many nodes are in the list
            runner = runner.next # Move to the next node in the list
        average = sum/count # this variable stores the average
        print(average) # print average
        return self # return itself

    def remove_dups(self):
        new_values = [self.head.data]
        if self.head == None:
            print('no values')
            return self
        if self.head.next == None:
            print('Cant be a duplicate of a single node')
            return self
        else:
            runner = self.head
            while runner.next != None:
                if runner.next.data not in new_values:
                    new_values.append(runner.next.data)
                else:
                    while runner.next.data in new_values:
                        runner.next = runner.next.next
                print(new_values)
                runner = runner.next
            return self
    
    def back(self): #this will return the last node in the list
        if self.head == None: #edge case self.head has no value return no values/self
            print('No Values')
            return self
        if self.head.next == None: #if the next node is equal to none return you only have one node in the list
            print(f'you only have one node in the list {self.head}')
            return self
        else:
            runner = self.head #first set the runner to the ehad node/// aka the start
            while runner.next: #while there is a runner.next or node next to the ehad node 
                runner = runner.next #runner will the equal the next runner in the list /// this will run til you get to the last node in the list
            print(runner.data) #you will then print the last node in the list
            return runner.data #return the runner value in the list

    def remove_back(self): #This will rmove the last node value in the list
        if self.head == None: #if self.head is equal to none /// aka no first node return/print no values
            print('No Values')
            return self
        if self.head.next == None: #if the next node to the first node is equal to none then return you only have one node in the list
            print('You only have one node in the list')
            return self #return the print statement/ self
        else:
            runner = self.head #else set the runner at the first node in the list
            while runner.next.next: #run this while there is a runner next value next value
                runner = runner.next #mov the runner to the next node
            runner.next = None #when it reaches the last node set the last node to equal none
            return self #return itself






        
            

            
list1 = SLL() #We are setting a variable to the Singly Linked List Function so thatwe can call on it with OOP


#list1.add_front(20)
#list1.add_front(50)
#list1.add_front(45)
#
#
#print(list1.length())
#print(list1.contains(5))


list1.add_back(4).add_back(20).add_back(100).add_back(100).add_back(40).add_front(33)
list1.add_back(10)
list1.remove_back()
#list1.display_values().min()

list1.back()





########## Clinks Singly Linked List Lecture






#class Student:
#    def __init__(self, nameInput = "default", gradeInput = "12th"):
#        self.name = nameInput
#        self.grade = gradeInput
#        self.sickDays = 0
#    
#    def homeSick(self, numOfDays):
#        self.sickDays+=numOfDays
#
#    def __repr__(self):
#        return self.name + self.grade + self.sickDays
#
#
#student1 = Student("William")
#
#
#student1.homeSick(7)
#
#print(student1.name)
#







