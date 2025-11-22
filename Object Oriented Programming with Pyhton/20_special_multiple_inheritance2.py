class A:
    def print_func(self):
        print("This is class A")
class B:
    def print_func(self):
        print("This is class B")
class C(A,B):
    def print_func(self):
        print("This is class C")
        super().print_func()

obj = C()
obj.print_func()