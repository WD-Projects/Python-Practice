#In Python, the @property decorator is used to make a method act like an attribute — meaning you can access it without parentheses while still running code behind the scenes.

class Student:
    def __init__(self, physics, chemistry, math):
        self.physics = physics
        self.chemistry = chemistry
        self.math = math
    
    @property
    def percentage(self):
        p = f"{(self.physics + self.chemistry + self.math) / 3 } %"
        return p

p1 = Student(98, 97, 99)
print(p1.percentage)

p1.physics = 95
print(p1.percentage)