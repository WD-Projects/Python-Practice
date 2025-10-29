marks = {
    "Mahir" : 34,
    "Muniya" : 32,
    "Niha" : 34.6,
    "List" : [3, "Banana", 32.4]
}
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Mahir" : 90, "Fari" : 89})
print(marks)

#by default these two look like same but:
print(marks["Mahir"])
print(marks.get("Mahir"))

#the difference is:
print(marks.get("Mahir2")) #this will return None
print(marks["Mahir2"]) #this will give an error