#Takes only true value.
#filter used in for fulfil condition
nums = [2, 3, 4, 5]
result = list(filter(lambda x : x%2 == 0 , nums))
print(result)