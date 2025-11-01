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

# Create an account
acc = BankAccount("Saqib", 1000)

# Accessing public methods
acc.deposit(500)
acc.withdraw(200)
acc.check_balance()

# Direct access
# print(acc.__balance)   # ❌ Not allowed
print(acc._BankAccount__balance)  # ✅ Name mangling trick (not recommended)
