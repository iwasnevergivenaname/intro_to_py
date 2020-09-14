# bank account - kind of account - methods - return new balance

# Write a BankAccount class.
#   Bank accounts should be created with the kind of account (like "savings" or "checking").
 #  Each account should keep track of its current balance.
  # Each account should have access to a deposit and a withdraw method.
#   Each account should start with a balance set to zero.
#  return the amount withdrawn, for convenience

class BankAccount():
    def __init__(self, kind, pin):
        self.kind = kind
        self.balance = 0
        self.fees = 0
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin_from_user):

        if (self.pin == pin_from_user):

              if (self.balance < amount):
                print("sorry yr too broke")
                return
              elif (self.balance == amount):
                self.balance -= amount
                print(f"yr at zero, be careful")
              else:
                self.balance -= amount
                print(f"current balance is {self.balance}")
        else:
            print("the pin you have entered is incorrect")

    def change_pin(self, pin):
        self.pin = pin
        print(f"your new pin is {self.pin}")




han_bank = BankAccount("checking", 69)
print("my new account is a {} account".format(han_bank.kind))

han_bank.deposit(69000)
print("my current balance is ${}".format(han_bank.balance))

han_bank.withdraw(690000, 698)
print("my current balance is ${}".format(han_bank.balance))

han_bank.change_pin(6978)

