
class Circle:
    PI = 3.14159
    def __init__(self,radius):
        self.radius = radius
        
    
    def area(self):
        return self.radius ** 2 * Circle.PI
    
    def perimeter(self):
        return 2 * Circle.PI * self.radius



c = Circle(5)
print(c.area())      # Expected output: 78.53975
print(c.perimeter()) # Expected output: 31.4159

c.radius = 10
print(c.area())      # Expected output: 314.159
print(c.perimeter()) # Expected output: 62.8318
