#When an attribute should be decleard as private follow this format --> __attribute_name, then it will be private.
#Same rule for method.

class Account:
    def __init__(self, name, account_no, balance):
        self.name = name
        self.__account_no = account_no
        self.__balance = balance

    def debit(self, amount):
        self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance
    
a1 = Account("Mahir", 23245231, 20000)
print(a1.get_balance())
a1.debit(1000)
print(a1.get_balance())