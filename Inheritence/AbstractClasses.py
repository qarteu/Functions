# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class \
# abstract calss = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motercycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

#vehicle = Vehicle() cant do this


car = Car()
motercycle = Motercycle()
car.go()
car.stop()
motercycle.go()



