class Car:
    color = None

def changeColor(car,color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()

changeColor(car1,"Blue")
changeColor(car2,"Red")
changeColor(car3,"Green")

print(car2.color)
print(car1.color)
print(car3.color)