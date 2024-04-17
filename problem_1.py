def get_name():
    a=input("Enter your name:")
    return a
def get_tshirt():
    user=get_name()
    brand_name=input("Enter the brand name you are searching for:")
    brand=["nike","adidas","hrx","puma","Peter England","Rebook"]
    for i in brand:
        if brand_name==i:
            print("Hi" ,{user}, "the brand you are looking for is available in our store ")
            break
    else:
        print("Hi" ,{user},"Unfortunately the brand you are looking for is not available in our store")

get_tshirt()