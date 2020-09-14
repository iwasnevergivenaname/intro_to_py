class Band():
    def __init__(self, name, genre, members):
        self.name = name
        self.members = members
        self.genre = genre
        self.cost = 10000

    def add_member(self, new_members):
        self.members = new_members

    def new_price(self, new_price):
        self.cost = new_price

    def change_genre(self, genre):
        self.genre = genre




mcr = Band("mcr", "whooopwhoop", "gerard")
print(f"this band is called {mcr.name}")

mcr.change_genre("alt")
print(f"this band is of the {mcr.genre} genre")
