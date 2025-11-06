#Class attributes is same for all objects and it is called by class (i.e Student.name).
#Object attributes is different for every object (i.e s1.name).
#If object attributes and class attributes are same --> precedence: obj attr > class attr

class Student:
    varsity_name = "SEU" #class attribute

    def __init__(self, name, ID):
        self.name = name #object attribute
        self.ID = ID #object attribute

s1 = Student("Mahir", 193)
s2 = Student("Akib", 232)

print(s1.name, s1.ID)
print(Student.varsity_name)

print(s2.name, s2.ID)
print(Student.varsity_name)