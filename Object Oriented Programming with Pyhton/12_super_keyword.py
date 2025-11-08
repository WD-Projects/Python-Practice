class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

class Toyota(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        super().stop()

obj = Toyota("Corolla", "Hybrid")
print(f"Name: {obj.name}, Type: {obj.type}")