# super() = Function used to give access to the methods of a parent class returns a temproyr object of a parent class when used

class Rectangle:

    def __init__(self,length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self,length, width):
        super().__init__(length,width)

    def area(self):
        return self.length*self.width
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.height*self.width

square = Square(4,4)
cube = Cube(3,4,5)
print(cube.volume())
print(square.area())
