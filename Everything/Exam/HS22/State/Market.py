
class Market:
    def __init__(self):
        self.vendors = []
        self.hour = 0
        self.profits = 0
    
    def add_vendor(self, fee):
        self.vendors.append(fee)
    
    def stats(self):
        return {
            "number of vendors": len(self.vendors),
            "hour": self.hour,
            "hourly profit": sum(self.vendors),
            "total profit": self.profits
        }

    def progress_hour(self):
        self.profits += sum(self.vendors)
        self.hour += 1
    
    def remove_vendor(self, fee):
        if fee not in self.vendors:
            raise Warning
        return self.vendors.remove(fee)

m = Market()
print(m.stats())
m.add_vendor(30)
m.add_vendor(5)
m.add_vendor(5)
print(m.stats())
m.progress_hour()
m.progress_hour()
m.progress_hour()
print(m.stats())
try:
    m.remove_vendor(11)
except:
    print("No vendor with that fee exists")
m.remove_vendor(5)
print(m.stats())
m.progress_hour()
print(m.stats())
