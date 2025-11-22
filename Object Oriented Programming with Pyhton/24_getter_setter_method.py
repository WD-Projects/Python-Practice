class Student:
    def __init__(self, age):
        self._age = age   # private variable

    @property
    #The method name should be same as variable name i.e _age
    def age(self):        # getter method
        return self._age

    @age.setter
    def age(self, value):   # setter method
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

s = Student(20)

print(s.age)     # calls getter -> s.age = s.age()
s.age = 25       # calls setter -> age(25)
print(s.age)

s.age = -3       # calls setter → raises error