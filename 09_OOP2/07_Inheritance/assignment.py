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

    def __str__(self) -> str:
        return "Rectangle of base:", self.__base , " height:", self.__height

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.__side = side
    def get_side(self)-> float:
        return self.__side

    def __str__(self) -> str:
        return "Square with side length:" + str(self.__side)


        
        
square1 = Square(8)
print(square1)
print("The area of sqaure1 is", square1.get_area())
print("The perimeter of sqaure1 is", square1.get_perimeter())
print("The side length of sqaure1 is", square1.get_side())

