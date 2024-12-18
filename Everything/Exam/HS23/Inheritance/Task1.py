from abc import ABC, abstractmethod

class Restaurant:
    def __init__(self, name):
        self.name = name

class Staff(ABC):
    unique_id = 101
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.number = Staff.unique_id
        Staff.unique_id += 1
        self.shifts = []
    
    @abstractmethod
    def salary(self):
        pass

    def work(self, amount):
        self.shifts.append(amount)
    
    def __str__(self):
        return f"Staff working at {self.restaurant.name} with salary {self.salary()}"
    
    

class Server(Staff):
    def __init__(self, restaurant, bsalary, hsalary):
        super().__init__(restaurant)
        self.bsalary = bsalary
        self.hsalary = hsalary
    
    def salary(self):
        return self.bsalary + sum(self.shifts) * self.hsalary 
    

class Dishwasher(Server):
    def __init__(self, restaurant, bsalary, hsalary):
        super().__init__(restaurant, bsalary, hsalary)

    def salary(self):
        return Server.salary(self) * 0.9

class Cook(Staff):
    def __init__(self, restaurant, payment):
        super().__init__(restaurant)
        self.payment = payment
    
    def salary(self):
        return self.payment


restaurant = Restaurant("Mc Ronalds")

cook = Cook(restaurant, 3200)
cook.work(10)
cook.work(50)
print(cook.number)
print(cook.shifts)
print(type(cook.shifts))
print(cook.salary())
print(cook)

server = Server(restaurant, 100, 9.50)
server.work(10)
server.work(50)
print(server.number)
print(server.shifts)
print(server.salary()) # (100 + 60*9.50)

washer = Dishwasher(restaurant, 100, 9.50)
washer.work(10)
washer.work(50)
print(washer.number)
print(washer.shifts)
print(washer.salary()) # (100 + 60*9.50) * 0.9