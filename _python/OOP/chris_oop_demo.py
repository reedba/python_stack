
class Bootcamp:
    def __init__(self, name, max_students ):
        self.name = name
        self.max_students = max_students 
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return self.students[len(self.students)-1].name
        
        else:
            return "Full House!!, no more spots available"

    def display(self):
        for student in self.students:
            print(student.name)
            

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def sayHello(self):
        print("Hello")
        return self

    def get_grade(self):
        print(f"My name is: {self.name} My grade is: {self.grade}")
        return self

    





        

student_one = Student("Brandon Reed", 34, 99)
student_two = Student("Noah Reed", 3.5, 100)
student_three = Student("Jackie Reed", 33, 105)
#student_three = Student("Jacqueline Reed", 33, 85)
#print(student_two.name)
#print(student_one.age)
#print(student_one.get_grade())
bootcamp_one = Bootcamp("Coding Dojo", 2)
bootcamp_two = Bootcamp("Ninja Dojo", 2)
print(bootcamp_one.add_student(student_one))
print(bootcamp_one.add_student(student_two))
print(bootcamp_one.add_student(student_three))
bootcamp_one.display()