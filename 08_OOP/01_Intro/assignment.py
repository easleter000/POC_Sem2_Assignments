import math


class RightTriangle: 
    def __init__(self, base, height):
        self.base = base
        self.height = height
        

    def area(self):
        return (1/2 * self.base * self.height)
    
    
    

triangle_1 = RightTriangle(3, 4)
print("The area of triange_1 is", triangle_1.area())
 
tri2 = RightTriangle(5, 5)
print("The base of tri2 is", tri2.base)
print("The height of tri2 is", tri2.height)
print("The area of tri2 is", tri2.area())
