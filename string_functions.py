name = "mahir"
print(len(name))
print(name.endswith('ir')) # true
print(name.startswith('ir')) # false
print(name.capitalize()) # Mahir
print(name.upper()) # MAHIR
print(name.count('i')) # 1

full_name = "akib hossain mahir"
print(full_name.replace("hossain", "mahir")) # akib mahir mahir
print(full_name.count('i')) # 3
print(full_name.count(' ')) # 2