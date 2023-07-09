# function --> calling
# returning values

def repeat(name):
    print("hello " + name)


repeat("bro")


def multiply(num1, num2):
    result = num1 * num2
    return result


print(multiply(3, 4))


# argument order matters unles you do this
# keyword arguments
def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


hello(last="Malunjkar", middle="Sanjay", first="Kartik")

print(round(abs(float(input("Enter a whole positive number:")))))
