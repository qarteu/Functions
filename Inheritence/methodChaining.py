#method chaining --> calling multiple methods esequentially each call performs an actipn on the same object and return self

class Car:
    def drive(self):
        print("This car is driving")
        return self

    def turnOn(self):
        print("Car has turned on")
        return self


car = Car()
car.turnOn().drive()