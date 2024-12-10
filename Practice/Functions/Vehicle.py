from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, door):
        super().__init__(make, model)
        self.door = door
    
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Doors: {self.door}"

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Capacity: {self.capacity}"


v = Vehicle("Generic", "ModelX")
print(v)  # Expected Output: "Make: Generic, Model: ModelX"

c = Car("Toyota", "Corolla", 4)
print(c)  # Expected Output: "Make: Toyota, Model: Corolla, Doors: 4"

t = Truck("Ford", "F-150", 3)
print(t)  # Expected Output: "Make: Ford, Model: F-150, Capacity: 3 tons"
