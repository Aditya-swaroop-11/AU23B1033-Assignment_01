def scoop_size():
    scoop_size=int(input("Enter the scoop size "))
    return scoop_size
def toppings():
    topping=input("Enter the name of topping")
    return topping
def make_shake():
    choice=input("Enter your choice of shake")
    return choice
#import ice_cream
def add_topping():
    size=scoop_size()
    topping=toppings()
    choice=make_shake()
    print("The size of your scoop is",size,"ml")
    print("Your added topping is:",topping)
    print("Your choice of shake is:",choice,"shake")
add_topping()
