import random
# help(random)
# print(dir(random))
print(random.random()) #This will generate a random float number between 0-1
print(random.randint(1, 10)) #This will generate a random integer number between 1-10 
print(random.uniform(1, 10)) #This will generate a random float number between 1-10 

fruits = ["Apple", "Banana", "Cherry"]
print(random.choice(fruits))

random.shuffle(fruits)
print(fruits)