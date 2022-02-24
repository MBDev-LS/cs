import math

class Shape():

    nextShape = 1

    @staticmethod
    def getTotalShapes():
        return Shape.nextShape - 1

    def __init__(self, colour) -> None:
        self.colour = colour

        self.shapeNumber = Shape.nextShape
        Shape.nextShape += 1
    
    def __str__(self) -> str:
        return f'Shape {self.shapeNumber}: {self.colour} '
    
    def setColour(self, colour):
        self.colour = colour
    
    def getShapeNumber(self):
        return self.shapeNumber

class Circle(Shape):
    def __init__(self, colour, radius) -> None:
        super().__init__(colour)
        self.radius = radius
    
    def __str__(self) -> str:
        return super().__str__() + 'circle'

    def setRadius(self, radius):
        self.radius = radius
    
    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, colour, sideLenth) -> None:
        super().__init__(colour)
        self.sideLenth = sideLenth
    
    def __str__(self) -> str:
        return super().__str__() + 'square'

    def setSideLenth(self, sideLenth):
        self.sideLenth = sideLenth
    
    def getSideLenth(self):
        return self.sideLenth
    
    def getArea(self):
        return self.sideLenth ** 2

square1 = Square('red', 2)

print(square1)
print(square1.getArea())
