from abc import ABC, abstractmethod
from math import pi


class GeometricObject(ABC):

    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def volume(self):
        pass


class Cube(GeometricObject):
    def __init__(self, color, filled, side_length):
        super().__init__(color, filled)
        self.side_length = side_length

    def area(self):
        return round(6 * (self.side_length) ** 2, 2)
        

    def volume(self):
        return round((self.side_length) ** 3, 2)
        


class Cylinder(GeometricObject):
    def __init__(self, color, filled, radius, height):
        super().__init__(color, filled)
        self.radius = radius
        self.height = height

    def area(self):
        return round((2 * pi * (self.radius) * (self.height)) + (2 * pi * (self.radius) ** 2), 2)
        
    def volume(self):
        return round(pi * (self.radius) ** 2 * (self.height), 2)
        

class Cone(GeometricObject):
    def __init__(self, color, filled, radius, vertical_height, slant_height):
        super().__init__(color, filled)
        self.radius = radius
        self.vertical_height = vertical_height
        self.slant_height = slant_height

    def area(self):
        return round((pi * (self.radius) ** 2) + (pi * self.radius * self.slant_height), 2)
         

    def volume(self):
        return round((1 / 3) * pi * ((self.radius) **2) * (self.vertical_height), 2)
        
    

# Create first cone object
cone_1 = Cone("red", True, 2, 4, 2)
print(f"Color of the Cone is {cone_1.color}")

# Create another cone object
cone_2 = Cone("black", False, 5.64, 4.2, 8.7)

# Create a cube object
cube = Cube("white", True, 7.2)
print(f"Color of the cube object is: {cube.color}")

#Update cube color
cube.color = "yellow"

#See if the color of cube object is changed
print(f"Color of the cube object is: {cube.color}")

#See the area and volume of the cone_1
print(f"cone_1 area is: {cone_1.area()} cone_2 volume is: {cone_1.volume()}")

# Testing the classes
cube = Cube("red", True, 3)
print("Cube area:", cube.area())       # Should return formatted area of the cube
print("Cube volume:", cube.volume())   # Should return formatted volume of the cube

cylinder = Cylinder("blue", False, 2, 5)
print("Cylinder area:", cylinder.area())     # Should return formatted area of the cylinder
print("Cylinder volume:", cylinder.volume()) # Should return formatted volume of the cylinder

cone = Cone("green", True, 2, 5, 5.39)
print("Cone area:", cone.area())        # Should return formatted area of the cone
print("Cone volume:", cone.volume())    # Should return formatted volume of the cone
