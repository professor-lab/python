rows = int(input("Enter number of rows: "))

ascii_value = 65

#Outer for loop to handle number of rows  
for i in range(rows):
    #Inner for loop to handle number of columns  
    #values change according to the outer loop  
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print()