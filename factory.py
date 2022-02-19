from abc import abstractmethod


class Shape:
    def __init__(self) -> None:
        pass
    @abstractmethod
    def calac_area(self):
        pass
    @abstractmethod
    def clac_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self,height:float,width:float) -> None:
        self.height=height
        self.width=width
    def calac_area(self):
        return self.height*self.height
    def clac_perimeter(self):
        return 2(self.height+self.width)

class Square(Shape):
    def __init__(self,width:float) -> None:
        self.width=width    
    def clac_perimeter(self):
        return 4*self.width
    def calac_area(self):
        return self.width**2

class Circle(Shape):
    def __init__(self,radius:float) -> None:
        self.radius=radius    
        self.__pi=3.14
    def clac_perimeter(self):
        return 2*self.__pi*self.radius
    def calac_area(self):
        return self.__pi*(self.radius**2)

