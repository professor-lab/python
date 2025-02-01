class Student:

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        print("add new student in database")

s1=Student("professor",98)
print(s1.name,s1.mark)

s2=Student("teacher",97)
print(s2.name,s2.mark)