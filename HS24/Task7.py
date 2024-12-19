
from abc import ABC

class MonthlyContract(ABC):
    def __init__(self, months, mcost):
        self.months = months
        self.mcost = mcost
    
    def total_cost(self):
        return self.mcost * self.months
    

class FlatRateContract(MonthlyContract):
    def __init__(self, rate):
        self.rate = rate
    
    def total_cost(self):
        return self.rate

class BundleContract(FlatRateContract):
    def __init__(self, months, mcost, rate):
        super().__init__(months, mcost, rate)
        
    
    def total_cost(self):
        return sum(self.mcost, self.months, self.rate)


m = MonthlyContract(3, 2500)
print(m.total_cost())
f = FlatRateContract(10000)
print(f.total_cost())
b = BundleContract([m, f])
print(b.total_cost())
project = BundleContract([b, FlatRateContract(1500)])
print(project.total_cost())