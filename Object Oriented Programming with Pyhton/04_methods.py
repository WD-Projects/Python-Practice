#Methods are functions which are called inside a class.
#The first parameter of methods will be self.

class Student:
    varsity_name = "SEU" 

    def __init__(self, name, ID, mark):
        self.name = name 
        self.ID = ID
        self.mark = mark

    def hellow(self):
        print("Welcome ", self.name)

    def get_marks(self):
        return self.mark
    
s1 = Student("Mahir", 193, 97)
s2 = Student("Akib", 232, 45)

print(f"Name: {s1.name}, ID: {s1.ID}")
print(f"Varsity name: {Student.varsity_name}")
print(f"Mark: {s1.get_marks()}")
s1.hellow()

print(f"Name: {s2.name}, ID: {s2.ID}")
print(f"Varsity name: {Student.varsity_name}")
print(f"Mark: {s2.get_marks()}")
s2.hellow()