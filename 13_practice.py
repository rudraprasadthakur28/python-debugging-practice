class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
            return self.balance
        else:
            print("Insufficient balance")
            return self.balance


account = BankAccount(5000)

new_balance = account.withdraw(1500)

print("Balance:", new_balance)