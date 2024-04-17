def get_name(): #create a function
    a=input("Enter your name:") #user input in function
    return a
def get_tshirt(): # creating another function
    user=get_name() #calling the first function
    brand_name=input("Enter the brand name you are searching for:") # brand name
    brand=["nike","adidas","hrx","puma","peter england","rebook"] #brand available in the store
    
    for i in brand: #loop for cheaking for brand
        if brand_name==i: #condition
            print("Hi" ,user, ",The brand you are looking for is available in our store ")
            break
    else: #else condition
        print("Hi" ,user,",Unfortunately the brand you are looking for is not available in our store")
    
    for i in brand: # condition loop of brand is available or not for size of tshrt
        if brand_name==i: #if brand is availabele then only take the user input of size of tshirt
            size=input("Enter the size of your t-shirt") #user input
            size_=["S","M","L","XL","XXL"] #size available for tshirt
            for i in size_: #loop for size
                if size==i: #condition 
                    print("Hi" ,user, ",The size you are looking for is available in our store ")
                    break
            else: #else condition
                print("Hi" ,user, ",Unfortunately the size you are looking for is not available in our store")

get_tshirt()