"""
📌 Purpose

1. Used to construct complex objects step by step.
2. Useful when object creation involves many steps or optional parts.

📌 When to Use Builder

Use it when:
1. The object has many optional parameters.
2. Object structure is complex or created in steps.
3. The same construction process can create different types of objects.

Examples:
1. Building a computer (CPU, RAM, GPU, SSD)
2. Creating an HTTP request
3. Creating a custom Pizza order

⚙️ Workflow

1. Builder → Handles each step of construction.
2. Director → Calls the builder methods in sequence.
3. Product → Final built object.
"""

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}, Storage: {self.storage}"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def add_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def add_ram(self, ram):
        self.computer.ram = ram
        return self

    def add_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer

# Build the computer (Client)
builder = ComputerBuilder()
computer = builder.add_cpu("Intel i7").add_ram("16GB").add_storage("512GB SSD").build()
print(computer)