container = ['Mahir', 'Akib', 4, 34.04, 'Hossain', 'Apple'] #any values of different data types
container[2] = 6 #lists are mutable
print(container[2])
print(container[1 : 3]) #['Akib', 6], same as string slicing

#some methods of lists:

"""
l1.sort(): updates the list to [1,2,7,8,15,21] 
l1.reverse(): updates the list to [15,21,2,7,8,1] 
l1.append(8): adds 8 at the end of the list 
l1.insert(3,8): This will add 8 at 3 index 
l1.pop(2): Will delete element at index 2 and return its value. 
l1.remove(21): Will remove 21 from the list.
"""