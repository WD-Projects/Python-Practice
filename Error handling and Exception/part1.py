try:
    nums = [1, 2, 3, 4, 5]
    print(nums[5])
    # x = abc
    # print(x)
except IndexError as e:
    print("IndexError: ", e)
except ValueError:
    print("ValueError")
except Exception as e:
    print("Exception", e)
else: #it will run when the try block will be executed.
    print("Code run successfully")
finally:
    print("Always will run")


#"raise" keyword (throwing a custom error message):
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative")
else:
    print(age)