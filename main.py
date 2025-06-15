from bank import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, owner, withdrawal_limit=3000000.0):
        super().__init__(owner)
        self._withdrawal_limit = withdrawal_limit

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._log_transaction("Deposit", amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self._withdrawal_limit:
            print(f"Withdrawal amount exceeds the limit of {self._withdrawal_limit}.")
            return False
        if amount > self._balance:
            print("Insufficient balance.")
            return False

        self._balance -= amount
        self._log_transaction("Withdraw", amount)
        return True
