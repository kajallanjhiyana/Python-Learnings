#Encapsulation is an OOP concept that combines data (variables
# ) and the methods (functions) that work on that data inside 
# a single class, while controlling how that data is accessed 
# or modified.


class BankAccount:
    __balance = 20000
    def __init__(self):
        print("Welcome to ABC Bank")
    def deposit(self, amount):
        self.__balance += amount
        print("Amount succefully deposited")
    def get_balance(self):
        return self.__balance

Person1 = BankAccount()
print(Person1.get_balance())
Person1.deposit(2000)
print(Person1.get_balance())
Person1.__balance = 50000 #creates a new attribute of class it doesn't change the original
print(Person1.__balance)
print(Person1.get_balance())

