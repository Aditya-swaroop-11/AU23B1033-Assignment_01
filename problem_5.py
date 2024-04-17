def call():
    x = 2 
    x = 5 - x / 2  #x=2 hence oveall x=5-2/2= 4
    print(x) #call() is always 4 as output
def caller():
    x = 1 #x initiate from here
    while x < 20 :
        print ("x="+ str(x) ) 
        call() #call function is called by caller
        x =x * 2 #x will change as caller value
        print("x = " + str(x))
print(caller())

#In this code, there are two functions ,one is call() and another is caller(),  first caller() function is called and in caller() -function call()- function is called.
#The value of caller() is 16 now, after this step it will be 32  which is greater then 20.hence none will print or it will end .
