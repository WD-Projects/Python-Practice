# def generate(a, b):
#     return a + b

# print(generate(2, 4))

"or"

generate =  lambda a, b : a + b
print(generate(2, 4))

'''
❗ Error Explanation

A lambda in Python can only contain one expression, not statements like:

1. for loops
2. while loops
3. if statements with blocks
4. assignments

So Python will throw a SyntaxError.
'''