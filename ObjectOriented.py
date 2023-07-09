from ObjectCar import Car

car_1 = Car("chevy", "Corvette",2021,"blue")
print(car_1.make)

car_1.wheels = 4

print(car_1.wheels)
car_1.drive()
car_1.stop()