class Account:
    first_name = ""
    last_name = "L"
    password = ""
    __balance = ""
    login = False
    def __init__(self):
        name = input("Enter name: ")
        p = input("Enter password: ")
        if p == self.password:
            self.login = True
            self.menu()
            self.check(name, p)
        else:
            print("Wrong password entered!")
            self.login = False
    def menu(self):
        print("""
                press 1 - To display account details
                press 2 - To change account password
                press 3 - To display balance
                press 4 - To withdraw cash
                press 5 - To add cash
                press 0 - To end
            """)
        c = True
        while c:
            ch = int(input("Enter your choice"))
            if ch == 1:
                print("Account holder's name: ", self.first_name, " ", self.last_name)
            elif ch == 2:
                n = input("Enter current password: ")
                while self.password!=n:
                    n = input("Enter current password: ")
                if self.password == n:
                    new = input("Enter new password")
                    self.password = new
                else:
                    print("Wrong password")
            else:
                print("Thank You have a great day!")
                c = False
        
    def check(self, name, p):
        obj = ""
        if name == "Father" and p == self.password:
            obj = Father()
        elif name == "Mother" and p == self.password:
            obj = Mother()
        elif name == "Son" and p == self.password:
            obj = Son()
            

    def withdraw(self, amount, balance):
        if balance < amount:
            return "Oops not enough balance to withdraw"
        else:
            self.__balance -= amount
            return f"Withdrawn {amount} from your account"

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount} to your account"

class Father(Account):
    first_name = "Father"
    password = "123"
    __balance = 25000
    def __init__(self):
        super().__init__()
        if self.login:
            print(f"Welcome ${self.first_name} to your account")

    def withdraw(self, amount, balance):
        super().withdraw()

    def deposit(self, amount, balance):
        super().deposit()

    def check_balance(self):
        print("self.balance = ", self.__balance)

class Mother(Account):
    first_name = "Mother"
    __balance = 10000
    password = "1234"
    def __init__(self, p):
        super().__init__()
        if p == self.password:
            print(f"Welcome ${self.first_name} to your account")

    def withdraw(self, amount, balance):
        super().withdraw()

    def deposit(self, amount, balance):
        super().deposit()

    def check_balance(self, p):
        print("self.balance = ", self.__balance)

class Son(Account):
    first_name = "Son"
    __balance = 100
    password = "12"
    def __init__(self, p):
        super().__init__()
        if p == self.password:
            print(f"Welcome ${self.first_name} to your account")

    def withdraw(self, amount, balance):
        super().withdraw()

    def deposit(self, amount, balance):
        super().deposit()

    def check_balance(self, p):
        print("self.balance = ", self.__balance)

c = True
while c:
    obj = Father()
    ch = input("Enter end to continue else press any key")
    if ch == "end":
        c = False
        break
    
    

