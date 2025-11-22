#Has a relationship between two classes but not so strong
#Suppose in this code if the add_department() function is not called, the two classes will be considered as separated.

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department_obj):
        self.departments.append(department_obj)
    
    def show_department(self):
        return [department.name for department in self.departments]
    
university1 = University("Souteast University")
department1 = Department("CSE")
department2 = Department("Physics")
department3 = Department("Pharmacy")
university1.add_department(department1)
university1.add_department(department2)
university1.add_department(department3)
print(university1.show_department())
