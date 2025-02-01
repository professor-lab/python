class Student:

    def __init__(self,name,course):
        self.name=name
        self.course=course
    def hello(self):
        print("hello",self.name)
    def get_course(self):
        print(self.name,"Course Is",self.course)

s1=Student("professor","BCA")
s1.hello()   
s1.get_course()     

s2=Student("teacher","BA")
s2.hello()
s2.get_course()