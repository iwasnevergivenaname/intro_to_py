class CoffeeCup():
# __init__ - constructor - special method whenever new coffeecup is created
# self refers to classes in python
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def fill(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0

    def drink(self, amount):
        self.mount -= amount
        if (self.amount == 0):
            self.amount = 0
            print("this bitch empty yeet")