"""
📌 Purpose

1. Ensures that only one object of a class is created throughout the entire program.

📌 When to Use Singleton

Use it when:
1. You need only one instance of a class.
2. The instance is shared globally throughout the application.

Examples:
1. Database connection class
2. Logger class
3. Configuration manager
4. Cache manager

⚙️ Workflow
1. Class checks whether an instance already exists.
2. If not, it creates the object.
3. If it exists, returns the same object instead of creating a new one.
"""

class Principle:
    instance = 0

    def __new__(cls):
        if cls.instance == 0:
            cls.instance = super().__new__(cls)
            cls.instance.name = "Mahir"
        return cls.instance
    
obj1 = Principle()
obj2 = Principle()
print(obj1 is obj2) #True
print(obj1.instance) #<__main__.Principle object at 0x000001A8F5BC70E0>