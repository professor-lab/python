rows = int(input("Enter the number of rows: "))  

#Outer for loop to handle number of rows  
for num in range(rows+1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for i in range(num):  
            print(num, end=" ")       
  
        #End line after each row  
        print()