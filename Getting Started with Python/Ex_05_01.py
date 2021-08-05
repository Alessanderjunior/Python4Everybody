# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and 
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        for itervar in num:
            if largest is None : 
                largest = itervar
            elif itervar > largest:
                largest = itervar    
        for itervar2 in num:        
            if smallest is None: 
                smallest = itervar
            elif itervar <  smallest:
                smallest = itervar
        break
    else:
        try:
            num = float(num) and num != 'done'
        except:
            print("Invalid input")    
            exit()
        
        
                 
        print(largest, smallest)
        
       
    
    

 

  


 