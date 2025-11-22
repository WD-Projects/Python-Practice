#In python, the constructor is called by a function called def __init__().
#All the classes have a function called which is called when an object is created.
#def __init__(self) --> this function takes a parameter called self which is mainly the copy of object and points to that object.
#self --> The self parameter is the reference to the current instance of the class and it is used access variables that belongs to that class.
class Student:

    #Default constructor
    def __init__(self):
        pass

    #Parameterized constructor
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID

s1 = Student("Mahir", 193)
print(s1.name, s1.ID)

s2 = Student("Akib", 194)
print(s2.name, s2.ID)