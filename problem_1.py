def get_tshirt(x):
    shirt=["p","c","j"]
    for i in (shirt):
        if(i==x):
            get_name()
            print("Hi" ,name,"Brand you looking for is available in our store")
            break
        else:
            get_name()
            print("Hi" ,name,"Unfortunately Brand you looking for is not available in our store")
            break

def get_name():
    name=input("enter the name")
    
a=input("enter the brand")
get_tshirt(a)