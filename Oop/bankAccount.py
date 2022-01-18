class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self. balance = balance
    def deposit(self, value):
        self.balance +=float(value)
        return self.balance
    def withdraw(self, value):
        self.balance -=float(value)
        return self.balance

c = BankAccount("Jeff")
print(c.owner)
print(c.balance)
print(c.deposit(801))

print(c.withdraw(501))