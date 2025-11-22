class A:
    def print_func(self):
        print("This is class A")
class B:
    def print_func(self):
        print("This is class B")
class C(A,B): #class C inherits from right to left means at first class B then class A will be inherited.This is the rules for multiple inheritance(the inheritance starts from right to left).
    pass

obj = C()
obj.print_func()