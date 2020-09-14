# bank account - kind of account - methods - return new balance

# Write a BankAccount class.
#   Bank accounts should be created with the kind of account (like "savings" or "checking").
 #  Each account should keep track of its current balance.
  # Each account should have access to a deposit and a withdraw method.
#   Each account should start with a balance set to zero.
#  return the amount withdrawn, for convenience

class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.fees = 0

    def balance(self):
        self.amount = self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
         self.balance -= amount
         if (self.balance < 0):
            self.fees += 69
         return amount

hank_bank = BankAccount(100)
print(hank_bank.balance())