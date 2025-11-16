"""
1. *args → allows a function to accept any number of positional arguments.

✔ Meaning:
*args collects extra positional arguments into a tuple.

✔ When do we use it?

When we don’t know how many arguments the user will pass.
When we want to pass multiple values without defining many parameters.
"""

def add(*args):
    print(args) #(1, 2, 3, 5, 7)
    return sum(args)

result = add(1, 2, 3, 5, 7)
print(result)