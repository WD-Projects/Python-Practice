#Has a strong relationship

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.power = Engine(horsepower)

    def show_power(self):
        print(f"{self.brand} has {self.power.horsepower} HP")

car1 = Car("BMW", 1500)
car1.show_power()