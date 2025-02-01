class Student:

    def __init__(self,name):
        self.name=name
    def hello(self):
        print("hello",self.name)

s1=Student("professor")
s1.hello()        

s2=Student("teacher")
s2.hello()