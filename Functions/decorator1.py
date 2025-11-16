# def flavour(func):
#     def wrapper():
#         print("There is cream above the cake")
#         func()
#         print("There is chocolet under the cake")
#     return wrapper


# def cake():
#     print("Cake is in the middle")

# x = flavour(cake)
# x()
# 'or'
# cake = flavour(cake)
# cake()


def flavour(func):
    def wrapper(): #a function is execute when it is called. Here wrapper() is not called so i will be simply returned.
        print("There is cream above the cake")
        func()
        print("There is chocolet under the cake")
    return wrapper

@flavour #this is same as "cake = falvour(cake)"
def cake():
    print("Cake is in the middle")

cake()