
class Currency:
    def __init__(self, name, amount, rate):
        self.name = name
        self.amount = amount
        self.rate = rate
    
    def __eq__(self, other):
        if not isinstance(other, Currency):
            return NotImplemented
        This = self.amount * self.rate
        That = other.amount * other.rate

        return This == That

print( Currency("EUR", 15, 0.5) == Currency("GBP", 10, 0.75) )
print( Currency("EUR", 15, 0.5) != Currency("GBP", 15, 0.75) )
print( Currency("GBP", 1, 0.75) == Currency("GBP", 10, 0.75) )
print( Currency("CHF", 1.50, 0.78) == "Enough to buy a coffee" )