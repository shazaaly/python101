class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        if value > self._balance:
            raise ValueError
        self._balance -= value


account = BankAccount(1500)
print(account)
print(account._balance)
