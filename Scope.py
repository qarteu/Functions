#scope = region that a varibale is recognized

name = "Kartik" #global scope
def display_name():
    name = "kartik" #local scope only in this method
    print(name)

print(display_name())