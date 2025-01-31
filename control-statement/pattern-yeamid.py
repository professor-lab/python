#Outer for loop to handle number of rows  
for i in range(0, rows):  
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
        for j in range(0, i + 1):  
            print("* ", end=" ")       
  
        #End line after each row  
        print()