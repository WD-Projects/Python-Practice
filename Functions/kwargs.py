"""
✔ Meaning:
**kwargs collects keyword arguments into a dictionary.

✔ When do we use it?
When we need to accept dynamic named parameters.
Useful when writing flexible functions or working with configs/settings.
"""

def my_func(**kwargs):
    print(kwargs)
    print(f"My name is {kwargs["first_name"]} {kwargs["last_name"]}. I am {kwargs["age"]} years old. I live in {kwargs["city"]}.")

my_func(last_name = "Mahir", first_name = "Akib Hossain", city = "Dhaka", age = 24)