# bank_account.py

class BankAccount:
    def _init_(self, initial_balance=0):
        """Initialize account with optional starting balance (default is 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to account balance."""
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds are available."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Display current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

