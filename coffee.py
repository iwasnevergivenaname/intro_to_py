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
        self.amount -= amount
        if (self.amount == 0):
            self.amount = 0
            print("this bitch empty yeet")

# number argument is capacity
han_cup = CoffeeCup(8)
gerard_cup = CoffeeCup(18)
bert_cup = CoffeeCup(2)
pete_cup = CoffeeCup(3)

bert_cup.empty()

han_cup.fill()
gerard_cup.fill()
bert_cup.fill()
pete_cup.fill()

gerard_cup.drink(6)

print(han_cup.amount)
print(gerard_cup.amount)
print(bert_cup.amount)
print(pete_cup.amount)

print(f"han only has {han_cup.amount} oz of coffee left")