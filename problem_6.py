def ROI(): #defineing a function
    asp=int(input("Enter the Annual Site Profit: "))  #user input
    icr=int(input("Enter the Improved Conversion Rate: "))
    ccr=int(input("Enter the Current Conversion Rate: "))
    epl=int(input("Enter the Expected Project Life: "))
    ic=int(input("Enter the Improvemenet Cost: "))
    i=0.05 # i value
    fgi=asp*(icr/ccr)-asp*((1+i)**epl-1) / ((i-ic)*(1+i)**epl) #formula
    return fgi #return parameter
def FGI(): #defining the main function
    fgi=ROI() #calling the function
    print(fgi) #printing the output
FGI()  
