name = "Mahir"
# nameslice = name[starting index : excluding ending index]
nameslice = name[0 : 4] # output will be printed stating from 0 index and excluding till index 4
print(nameslice)
character = name[2] # will print only index 2 (h)
print(character)

# negative slicing

print(name[-4 : -1])
print(name[1 : 4])

# some different slicing

print(name[: 4]) # means same as print(name[0 : 4])
print(name[1 :]) # means same as print(name[1 : 5])

# string slicing with skip value

nameslice2 = "abcdefghijklmnopqrstuvwxyz"
print(nameslice2[1 : 8 : 3])
# lets clarify this step by step:
print(nameslice2[1 : 8]) # output will 'bcdefgh'
# then: 
print(nameslice2[1 : 8 : 3]) # output will 'beh'