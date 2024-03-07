class Rectangle:
    __counter = 0

    def get_count():
        return Rectangle.__counter
    
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height

            Rectangle.__counter += 1
            
            
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base
    
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__base * self.__height   


        
rec1 = Rectangle(7,8)
print(rec1.get_area())
print(rec1.get_base())
print(rec1.get_height())
print(rec1.get_perimeter())

rec2 = Rectangle(10,18)
print(rec2.get_area())
print(rec2.get_base())
print(rec2.get_height())
print(rec2.get_perimeter())

print("You have made", Rectangle.get_count(), "rectangles")