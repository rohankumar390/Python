

from abc import ABC,abstractclassmethod, abstractmethod
from cmath import rect
 

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
class Rectangle(Shape):
    type="REctangle"
    side=4
    def __init__(self):
        self.lenght=8
        self.breadth=7
        
    def printarea(self):
        return self.lenght*self.breadth
    
rect1= Rectangle()
print(rect1.printarea())