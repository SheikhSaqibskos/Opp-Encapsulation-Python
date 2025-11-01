# Opp-Encapsulation-Python
Class Work and Assignments

Encapsulation in Python – Assignment

Aim:
To understand and implement the concept of Encapsulation in Python using classes and private attributes.

Theory:
Encapsulation is one of the main principles of Object-Oriented Programming (OOP).
It means binding data and methods into a single unit (class) and restricting direct access to the data for security and integrity.
In Python, this is done using access modifiers:

Public → Accessible everywhere
Protected (_) → Accessible in class and subclasses (by convention)
Private (__) → Accessible only within the class

Encapsulation helps to:
Hide internal object details
Control how data is modified
Prevent accidental interference and misuse of data

Program:
# Encapsulation Example – Bank Account

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder   # Public attribute
        self.__balance = balance               # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    # Public method to check balance
    def check_balance(self):
        print(f"Current balance: {self.__balance}")

# Creating an object
acc = BankAccount("Saqib", 1000)

# Using public methods
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()

# Trying to access private data directly (will cause error)
# print(acc.__balance)  # ❌ Not allowed

# Access through name mangling (for demonstration only)
print(acc._BankAccount__balance)

Output:
Deposited: 500
Withdrawn: 200
Current balance: 1300
1300

Conclusion:
Encapsulation in Python helps protect object data by restricting direct access and providing controlled methods for modification.
It enhances security, data integrity, and code readability, making the program more reliable.
