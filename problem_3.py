def order(): #define a function
    stack=[]  #use of stack 
    a=int(input("enter the number of item")) #user input
    for i in range(1,a+1):
        b=input("enter the order") #total items
        stack.append(b) #appending item to the list
    
    for i in stack:
        print("Preparing your order",i) #printing the outcome
        
    print("The following order have been despatched")    #printing the outcome
    for j in stack:   
        print(j) #print 
order()
