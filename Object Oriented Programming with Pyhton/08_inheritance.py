class Father:
    def cook(self):
        print("I can cook...")

class Mother:
    def eat(self):
        print("I can eat...")

class Child(Father, Mother):
    @staticmethod
    def write():
        print("I can write...")

c1 = Child()
c1.cook()
c1.eat()
Child.write()