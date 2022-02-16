

class Node: # Singly Linked List Node Class
    def __init__(self, num):
        self.data = num #holds the value for the node
        self.next = None #Pointer to the next node


class SLL: #Singly Linked list class itself
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

    def max(self):
        if self.head == None:
            print('No values')
        else:
            runner = self.head
            max = self.head.data
            while runner.next != None:
                if runner.next.data > max:
                    max = runner.next.data
                runner = runner.next
            print(max)
            return self

    def min(self):
        if self.head == None:
            print('No values')
        else:
            runner = self.head
            min = self.head.data
            while runner.next != None:
                if runner.next.data < min:
                    min = runner.next.data
                runner = runner.next
            print(min)
            return self


    def avg(self):
        sum = 0
        count = 0
        runner = self.head
        while(runner):
            sum+=runner.data
            count+=1
            runner = runner.next
        average = sum/count
        print(average)
        return self

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
    
    def back(self):
        if self.head == None:
            print('No Values')
            return self
        if self.head.next == None:
            print('you only have one node in the list')
            return self
        else:
            runner = self.head
            while runner.next:
                runner = runner.next
            print(runner.data)
            return runner.data

    def remove_back(self):
        if self.head == None:
            print('No Values')
            return self
        if self.head.next == None:
            print('You only have one node in the list')
            return self
        else:
            runner = self.head
            while runner.next.next:
                runner = runner.next
            runner.next = None
            return self






        
            

            
list1 = SLL() #We are setting a variable to the Singly Linked List Function


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







