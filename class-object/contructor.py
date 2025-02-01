class Student:

    def __init__(self,name):
        self.name=name
        print("add new student in database")

s1=Student("professor")
print(s1.name)

s1=Student("teacher")
print(s1.name)