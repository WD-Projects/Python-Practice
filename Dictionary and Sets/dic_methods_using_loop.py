a = {
    "Mahir" : 90,
    "Akib" : 56,
    1 : ["Apple", "Banana", "Cherry"]
}

for item in a:
    print(item)

print("-------")

for value in a.values():
    print(value)

print("--------")

for key, value in a.items():
    print(f"key : {key}, Value: {value}")