
class Product:
    def __init__(self, name, cost, profit): 
        self.name = name
        self.cost = cost
        self.profit = profit

    def sales_price(self):
        return self.cost * (1 + self.profit)
    
    def __str__(self):
        return f"{self.name} sells for {self.sales_price():.2f}" 
    
    def __repr__(self) -> str:
        return f"Product({self.name}, {self.cost:.2f}, {self.profit:.2f})"
        
















p = Product("Smartphone", 1000, 0.1)
print( p.sales_price() )
print( p )
print( [p, Product("Dumbphone", 100, 0.2)])