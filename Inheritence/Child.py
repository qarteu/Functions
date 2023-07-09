class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("Im barking for you...WWUUUFFF WUUUUFF ")


dog = Dog()
print(dog.alive)
dog.eat()
dog.bark()
