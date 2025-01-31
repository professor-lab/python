rows = int(input("Enter the number of rows: "))  
num = 1
stop = 2

#Outer for loop to handle number of rows  
for i in range(rows):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(1, stop):  
            print(num, end=" ")     
            num += 1  
  
        #End line after each row  
        print() 
        stop += 2
