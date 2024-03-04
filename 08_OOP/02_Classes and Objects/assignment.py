import math


class RightTriangle: 
    def __init__(self, base, height):
        self.base = base
        self.height = height
       

    def area(self):
        return (1/2 * self.base * self.height)
    def hypotenuse(self):
        return(math.sqrt(self.base ** 2 + self.height ** 2))
    def perimeter(self):
        return(self.base + self.height, + tri2.hypotenuse())
    
    
    

tri2 = RightTriangle(5, 5)
print("The base of tri2 is", tri2.base)
print("The height of tri2 is", tri2.height)
print("The area of tri2 is", tri2.area())
print("The hypotenuse of tri2 is", tri2.hypotenuse())
print("The perimeter is", tri2.perimeter)
