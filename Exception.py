#exception = break up flow of program
try:
    numerator = int(input("Enter a number to divide"))
    denom = int(input("Enter a number to divide by: "))
    result = numerator/denom
except ZeroDivisionError as e:
    print(e)
    print("Cant divide")
except ValueError as e:
    print(e)
    print("Enter only numbers please!")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")

