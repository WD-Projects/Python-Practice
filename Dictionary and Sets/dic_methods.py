marks = {
    "Mahir" : 34,
    "Muniya" : 32,
    "Niha" : 34.6,
    "List" : [3, "Banana", 32.4]
}
print(marks.items()) #dict_items([('Mahir', 34), ('Muniya', 32), ('Niha', 34.6), ('List', [3, 'Banana', 32.4])])
print(marks.keys()) #dict_keys(['Mahir', 'Muniya', 'Niha', 'List'])
print(marks.values()) #dict_values([34, 32, 34.6, [3, 'Banana', 32.4]])

marks.update({"Mahir" : 90, "Fari" : 89})
print(marks) #{'Mahir': 90, 'Muniya': 32, 'Niha': 34.6, 'List': [3, 'Banana', 32.4], 'Fari': 89}

#by default these two look like same but:
print(marks["Mahir"]) #90
print(marks.get("Mahir")) #90

#the difference is:
print(marks.get("Mahir2")) #this will return None
print(marks["Mahir2"]) #this will give an error