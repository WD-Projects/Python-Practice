a = list(range(0, 11))
result = {i:"Even" if i%2 == 0 else "odd" for i in a} #structure: <value_if_true> if <condition> else <value_if_false>

print(result)