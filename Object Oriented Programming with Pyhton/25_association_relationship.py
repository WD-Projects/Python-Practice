#We use it when two classes are need to be connected.

class Student:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

class Laptop:
    def __init__(self, laptop_obj):
        self.laptop_var = laptop_obj

student1 = Student("Mahir", "Lenovo")
laptop = Laptop(student1)
print(f"{student1.name} has purchased a laptop which brand is {laptop.laptop_var.brand}")