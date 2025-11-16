#map() traverse the each element and return some value.
#map() applies a function to every item in an iterable (list, tuple, etc.).
#map(ki korte cacchi, kake korte cacchi)

nums = [2, 3, 4, 5]
result = list(map(lambda x : x*x, nums))
print(result)