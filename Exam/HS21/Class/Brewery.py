class Brewery:
    def __init__(self, name):
        self.name = name
        self.resources = {}

    @staticmethod
    def to_gram(v, foo):
        if foo == "t":
            return v * 1000000
        if foo ==  "kg":
            return v * 1000
        if foo == "g":
            return v
    def add_stock(self, name, amount, unit):
        if name not in self.resources:
            self.resources[name] = 0
        grams = Brewery.to_gram(amount, unit)
        self.resources[name] += grams


    def show_stock(self, resource):
        if resource not in self.resources:
            return 0
        return self.resources[resource]
    
    def brew(self, recipe):
        for name, grams in recipe.items():
            if self.resources[name] < grams or name not in self.resources:
                raise LookupError
        for name, grams in recipe.items():  
            self.resources[name] -= grams
            if self.resources[name] == 0:
                del(self.resources[name])



assert Brewery.to_gram(1, "t") == 1000000
assert Brewery.to_gram(1, "kg") == 1000
assert Brewery.to_gram(1, "g") == 1
b = Brewery("KegOverflow")

assert b.show_stock("Syrup") == 0
b.add_stock("Malt", 5, "kg")
b.add_stock("Malt", 5, "kg")
b.add_stock("Water", 50, "kg")
b.add_stock("Hops", 30, "g")
assert b.show_stock("Malt") == 10000

b.brew({"Malt": 8000, "Water": 40000, "Hops": 20})
assert b.show_stock("Malt") == 2000
b.brew({"Water": 10000})
assert b.show_stock("Water") == 0