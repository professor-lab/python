rows = int(input("Enter the number of rows: "))  

#Outer for loop to handle number of rows  
for i in range(1, rows+1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(1, i + 1):  
            print(j, end=" ")       
  
        #End line after each row  
        print()