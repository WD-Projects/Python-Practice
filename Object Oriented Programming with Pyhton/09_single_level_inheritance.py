class A:
    @staticmethod
    def a():
        print("Welcome to class A...")
    
class B(A):
    pass

obj = B()
obj.a()