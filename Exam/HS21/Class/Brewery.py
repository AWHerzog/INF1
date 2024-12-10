
class Brewery:
    def __init__(self, name):
        self.name = name
        self.__stock = {}

    @staticmethod
    def to_gram(amount, src_unit):
        factor = 0
        if src_unit == "kg":
            return amount * 1000
        if src_unit == "t":
            return amount * 1000 * 1000
        return amount

    def add_stock(self, resource, amount, unit):
        if resource not in self.__stock:
            self.__stock[resource] = 0
        grams = Brewery.to_gram(amount, unit)
        self.__stock[resource] += grams

    def show_stock(self, resource):
        if resource not in self.__stock:
            return 0
        return self.__stock[resource]

    def brew(self, recipe):
        for resource, amount in recipe.items():
            if (resource not in self.__stock or
                self.__stock[resource] < amount):
                raise LookupError
        for resource, amount in recipe.items():
            self.__stock[resource] -= amount
            if self.__stock[resource] == 0:
                del(self.__stock[resource])