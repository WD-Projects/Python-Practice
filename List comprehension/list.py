a = [1,2,3,4,5,6]
new_list = [i for i in a if i%2 == 0] #If there is only if statement, the if will be after for loop
print(new_list)

b = [1,2,3,4,5,6]
new_list2 = [i**2 if i%2 == 0 else i for i in b] #If there is both if and else statement, the if and else will before for loop
print(new_list2)