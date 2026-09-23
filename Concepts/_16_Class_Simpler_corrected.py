class Account:
    """Base class: owns ALL shared behavior. Subclasses only supply their own data."""

    def __init__(self, first_name, password, balance):
        self.first_name = first_name
        self.last_name = "L"
        self.password = password
        self.__balance = balance          # single source of truth for balance
        self.login = False
        self.__failed_attempts = 0        # tracks wrong passwords since last successful login

    def authenticate(self, entered_password):
        if entered_password == self.password:
            if self.__failed_attempts > 0:
                print(f"Welcome back, {self.first_name}. Note: {self.__failed_attempts} "
                      f"failed login attempt(s) were made on your account.")
            else:
                print(f"Welcome, {self.first_name}, to your account.")
            self.login = True
            self.__failed_attempts = 0
        else:
            self.__failed_attempts += 1
            print(f"Wrong password! ALERT: attempt {self.__failed_attempts} on "
                  f"{self.first_name}'s account.")
            self.login = False
        return self.login

    def check_balance(self):
        print("Current balance =", self.__balance)

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid positive amount.")
        elif amount > self.__balance:
            print("Oops, not enough balance to withdraw.")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Enter a valid positive amount.")
        else:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")

    def change_password(self, old, new):
        if old == self.password:
            self.password = new
            print("Password changed successfully.")
        else:
            print("Wrong current password — cannot change.")

    def menu(self):
        print("""
            press 1 - Display account details
            press 2 - Change account password
            press 3 - Display balance
            press 4 - Withdraw cash
            press 5 - Add cash
            press 0 - Logout
        """)
        menu_active = True                # separate from the OUTER session loop's flag
        while menu_active:
            choice = input("Enter your choice: ")
            if not choice.lstrip("-").isdigit():
                print("Please enter a valid number.")
                continue
            choice = int(choice)

            if choice == 1:
                print("Account holder:", self.first_name, self.last_name)
            elif choice == 2:
                old = input("Enter current password: ")
                new = input("Enter new password: ")
                self.change_password(old, new)
            elif choice == 3:
                self.check_balance()
            elif choice == 4:
                amount = int(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == 5:
                amount = int(input("Enter amount to add: "))
                self.deposit(amount)
            elif choice == 0:
                print("Thank you, have a great day!")
                menu_active = False
            else:
                print("Invalid choice, try again.")


class Father(Account):
    def __init__(self):
        # Subclass supplies ITS OWN data, but reuses the parent's __init__ logic entirely.
        super().__init__(first_name="Father", password="123", balance=25000)

    def withdraw(self, amount):
        # Example override: still delegates the real logic to the parent via super().
        print("[Father account activity]")
        super().withdraw(amount)


class Mother(Account):
    def __init__(self):
        super().__init__(first_name="Mother", password="1234", balance=10000)


class Son(Account):
    WITHDRAW_LIMIT = 500                  # class-level constant specific to Son

    def __init__(self):
        super().__init__(first_name="Son", password="12", balance=100)

    def withdraw(self, amount):
        # Polymorphism: Son has EXTRA restriction logic, then defers to the parent's version.
        if amount > self.WITHDRAW_LIMIT:
            print(f"Sons can withdraw at most {self.WITHDRAW_LIMIT} per transaction.")
        else:
            super().withdraw(amount)


# Create each account ONCE, so balances/passwords persist across multiple login sessions.
accounts = {
    "Father": Father(),
    "Mother": Mother(),
    "Son": Son(),
} 

print("Welcome, your honour.")
running = True
while running:
    name = input("\nEnter name (Father/Mother/Son): ")
    account = accounts.get(name)

    if account is None:
        print("No such account exists.")
    else:
        password = input("Enter password: ")
        if account.authenticate(password):
            account.menu()

    cont = input("Type 'end' to quit, anything else to continue: ")
    if cont.strip().lower() == "end":
        running = False