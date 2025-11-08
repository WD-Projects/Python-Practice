class Person:
    name = "Akib Hossain Mahir"

    @classmethod
    def changeName(cls, name):
        cls.name = name

obj = Person()
obj.changeName("Mahir")
print(obj.name) #Mahir
print(Person.name) #Mahir



# class Person:
#     name = "Akib Hossain Mahir"

#     def __init__(self, name):
#         self.name = name

# obj = Person("Mahir")
# print(obj.name) #Mahir
# print(Person.name) #Akib Hossian Mahir




# class Person:
#     name = "Akib Hossain Mahir"

#     def __init__(self, name):
#         self.__class__.name = name

# obj = Person("Mahir")
# print(obj.name) #Mahir
# print(Person.name) #Mahir
