class BankAccount:

# Class attribute: belongs to the class and is shared as
# the default value until an instance gets its own attribute.
    __balance = 20000
    _pin = 234

    def __init__(self):
        print("Welcome to ABC Bank")

    def deposit(self, amount):
        # Inside the class, __balance refers to the mangled name.
        # This creates/updates an INSTANCE attribute on self.
        self.__balance += amount
        print("Amount succefully deposited")

    def get_balance(self):
        # Getter method: returns the instance balance if it exists;
        # otherwise, Python can find the class attribute.
        return self.__balance

Person1 = BankAccount()

print(Person1.get_balance())  # 20000

Person1.deposit(2000)
print(Person1.get_balance())  # 22000

Person1.__balance = 50000  # creates a new attribute of class it doesn't change the original

# IMPORTANT:

# The above statement creates an instance attribute named

# "__balance". It does NOT modify "_BankAccount__balance".

print(Person1.__balance)   # 50000: the new instance attribute
print(Person1.get_balance())  # 22000: the original mangled balance
print(Person1._pin)