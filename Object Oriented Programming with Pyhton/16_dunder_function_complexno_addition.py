
'''
In Python, dunder functions (short for “double underscore” functions) are special, built-in methods that start and end with double underscores — like __init__, __len__, or __str__.

They are also known as magic methods or special methods because they let you define how your objects behave with Python’s built-in operations — such as printing, addition, comparison, or using len().
'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def show_number(self):
        print(f"{self.real} + {self.img}i")

    #dunder function
    def __add__(self, c2):
        newreal = self.real + c2.real
        newimg = self.img + c2.img
        return Complex(newreal, newimg)
    
    def __sub__(self, c2):
        newreal = self.real - c2.real
        newimg = self.img - c2.img
        return Complex(newreal, newimg)
    

c1 = Complex(3, 4)
c1.show_number()

c2 = Complex(1, 2)
c2.show_number()

# c3 = c1.add(c2)
# c3.show_number()

c3 = c1 + c2 #Python is trying to do "c3 = c1.add(c2)"
c3.show_number()

c3 = c1 - c2
c3.show_number()
