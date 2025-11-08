class Car:
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

class Corolla(Toyota):
    def __init__(self, type):
        self.type = type

obj = Corolla("Electric")
print(obj.type)
obj.start()
obj.stop()