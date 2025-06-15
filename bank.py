

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self._balance = 0.0
        self._transactions = []

    def _log_transaction(self, transaction_type, amount):
        self._transactions.append({
            'type': transaction_type,
            'amount': amount,
            'balance': self._balance
        })

    def get_balance(self):
        return self._balance

    def get_transactions(self):
        return self._transactions
