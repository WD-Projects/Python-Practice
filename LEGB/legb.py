"""
L = local
E = enclosing
G = global
B = built in scope
"""

n = "global"
def outer():
    n = "enclosing"
    def inner():
        # nonlocal n
        # global n
        n = "local"
        print(n)
    inner()
    print(n)
outer()
print(n)

#global keyword --> can change global, not enclosing
#nonlocal keyword --> can change enclosing, not global