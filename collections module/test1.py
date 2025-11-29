import collections 
# print(dir(collections))
# print(collections.__doc__)

fruits = ["Apple", "Banana", "Cherry", "Banana"]
# print(fruits.count("Banana"))
print(collections.Counter(fruits)) #Counter({'Banana': 2, 'Apple': 1, 'Cherry': 1})
print(collections.Counter(fruits).most_common(2)) #[('Banana', 2), ('Apple', 1)]

word_dict = collections.defaultdict(list)
word_dict["Python"].append("Programming Language")
print(word_dict)