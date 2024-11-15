from abc import ABC, abstractmethod

class Restaurant:
    def __init__(self, name):
        self.name = name

class Staff(ABC):
    counter = 101
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.shifts = []
        self.number = Staff.counter
        Staff.counter += 1

    def work(self, hours):
        self.shifts.append(hours)
    
    @abstractmethod
    def salary(self):
        pass
    def __str__(self):
        return f"Staff working for {self.restaurant.name} with salary {self.salary()}"

class Server(Staff):
    def __init__(self, restaurant, base_salary, hourly_salary):
        super().__init__(restaurant)
        self.base_salary = base_salary
        self.hourly_salary = hourly_salary
    
    def salary(self):
        return self.base_salary + sum(self.shifts) * self.hourly_salary

class Dishwasher(Server):
    
    def salary(self):
        return super().salary() * 0.9

class Cook(Staff):
    def __init__(self, restaurant, base_salary):
        super().__init__(restaurant)
        self.base_salary = base_salary

    def salary(self):
        return self.base_salary

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
print(washer.salary())