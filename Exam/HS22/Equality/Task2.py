
class Currency:
    def __init__(self, name, amount, rate):
        self.__name = name
        self.__amount = amount
        self.__rate = rate

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        
        this = self.__amount * self.__rate
        that = other.__amount * other.__rate
        return this == that


print( Currency("EUR", 15, 0.5) == Currency("GBP", 10, 0.75) )
print( Currency("EUR", 15, 0.5) != Currency("GBP", 15, 0.75) )
print( Currency("GBP", 1, 0.75) == Currency("GBP", 10, 0.75) )
print( Currency("CHF", 1.50, 0.78) == "Enough to buy a coffee" )