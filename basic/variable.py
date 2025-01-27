def counter():
    num=0
    def increment():
        nonlocal num
        num+=1
        print(num)
        return num
    return increment
c=counter()
c()
c()
c()