

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
        count = 0
        runner = self.head
        while(runner != None):
            count+=1
            runner = runner.next
        return count

    def contains(self, val):
        runner = self.head 
        while(runner):
            if runner.data == val:
                return True
            runner = runner.next
        else:
            return False

    def add_back(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            runner = self.head
            while runner.next != None:
                runner = runner.next
        runner.next = Node(value)
        return self
    
    def display_values(self):
        if self.head == None:
            print("no values")
        else:
            runner = self.head
            while runner != None:
                print(runner.data)
                runner = runner.next
        return self 


        
            

            
list1 = SLL() #We are setting a variable to the Singly Linked List Function

list1.add_front(5)
#list1.add_front(20)
#list1.add_front(50)
#list1.add_front(45)
#
#
#print(list1.length())
#print(list1.contains(5))


list1.add_back(4).add_back(20).add_back(30).add_back(23)

list1.display_values()


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







