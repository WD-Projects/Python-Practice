'''
@abstractmethod

This one comes from the abc module (Abstract Base Class).
It’s used to force subclasses to implement a particular method
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # subclasses must override this

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

# s = Shape()  #can't instantiate abstract class
c = Circle(5)
print(c.area())
