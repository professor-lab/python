class Attribute:
    college_name="abc college"
    def __init__(self,name):
        self.name=name
        print(name)
s1=Attribute("professor")
print(s1.college_name)