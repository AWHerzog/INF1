
class Order:
    def __init__(self,items,cost):
        self.items = items
        self.cost = cost

    def __eq__(self, other):
        if not isinstance(other, Order):
            return NotImplemented
        
        return sorted(self.items) == sorted(other.items) and self.cost == other.cost

print( Order(["Beer", "Wine", "Beer"], 14.50) == Order(["Wine", "Beer", "Beer"], 14.50) )
print( Order(["Beer", "Wine", "Beer"], 14.50) != Order(["Wine", "Beer"], 14.50) )
print( Order(["Beer", "Pretzels"], 14.50) == "Healthy meal" )