
from abc import ABC, abstractmethod

class Driver:
<<<<<<< HEAD
    pass
=======
    unique_id = 1001    
    def __init__(self, name):
        self.name = name
        self.number = Driver.unique_id
        Driver.unique_id += 1   
>>>>>>> f47629c7d0073300213d72edab644a1ffb566cff

class Transport:
    pass

<<<<<<< HEAD
class Shuttle:
    pass

class Taxi:
    pass

class DiscountTaxi:
    pass

=======
    def trip(self, km):
        self.trips.append(km)
    
    @abstractmethod
    def total_cost(self):
        pass

    def __repr__(self):
        return f"Transport revenue: {self.total_cost():.2f} (driver: {self.driver.name})"

class Shuttle(Transport):
    def __init__(self, driver, fee):
        super().__init__(driver)
        self.fee = fee
    
    def total_cost(self):
        return self.fee

class Taxi(Transport):
    def __init__(self, driver, trip_fee, km_fee):
        super().__init__(driver)
        self.trip_fee = trip_fee 
        self.km_fee = km_fee 
    
    def total_cost(self):
        return len(self.trips) * self.trip_fee + sum(self.trips) * self.km_fee

class DiscountTaxi(Taxi):
    
    def total_cost(self):
        return super().total_cost() * 0.8
>>>>>>> f47629c7d0073300213d72edab644a1ffb566cff

driver = Driver("Travis Bickle")
driver = Driver("Korben Dallas")
print(driver.number)

taxi = Taxi(driver, 2.00, 0.10)
taxi.trip(10)
taxi.trip(50)
print(taxi.trips)
print(type(taxi.trips))
print(taxi.total_cost()) # (2.00+10*0.10 + 2.00+50*0.10)
print(taxi)

dtaxi = DiscountTaxi(driver, 2.00, 0.10)
dtaxi.trip(10)
dtaxi.trip(50)
print(dtaxi.trips)
print(dtaxi.total_cost()) # (2.00+10*0.10 + 2.00+50*0.10) * 0.8

shuttle = Shuttle(driver, 250)
shuttle.trip(10)
shuttle.trip(50)
print(shuttle.trips)
print(shuttle.total_cost())