rows = int(input("Enter the number of rows: "))  

#Outer for loop executing in reverse order
for i in range(rows + 1, 0, -1):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(0, i - 1):  
            print("* ", end=" ")       
  
        #End line after each row  
        print()