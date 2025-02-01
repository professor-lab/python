class Student:

    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def get_avg(self):
        sum=0
        for val in self.mark:
            sum+=val
        print("hi",self.name,"your ave score is : ",sum/3)

s1=Student("Loky",[99,98,97])

s1.get_avg()
        