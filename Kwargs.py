# **kwargs = parameter that will pack all arguments into a dictionary
#            Useful so that a function can accept a varying amount of keyword arguments


def hello(**kwargs):
    print("hello", end=" ")
    for key,value in kwargs.items():
            print(value,end = " ")

hello(title = "Mr." ,first = "Bro" , middle = "dude", last = "Code")
