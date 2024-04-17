def get_name(): #defining a function 
    a=input("Enter your name:") #user input of name
    return a
def get_tshirt(): #defining another function
    user=get_name() #calling the first function
    brand_name=input("Enter the brand name you are searching for:") #user input for searching
    brand=["nike","adidas","hrx","puma","Peter England","Rebook"] #Brand available in store
    for i in brand: 
        if brand_name==i: #cheaking for the brand
            print("Hi" ,user, ",the brand you are looking for is available in our store ")
            break
    else:
        print("Hi" ,user,",Unfortunately the brand you are looking for is not available in our store")

get_tshirt() 