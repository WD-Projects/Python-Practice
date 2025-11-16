from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)

"""
Explanation:
1 * 2 = 2
2 * 3 = 6
6 * 4 = 24
"""