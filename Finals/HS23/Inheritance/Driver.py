from abc import ABC, abstractmethod

class Driver:
    counter = 1001
    def __init__(self, name):
        self.name = name
        self.number = Driver.counter
        Driver.counter += 1
   
class Transport(ABC):
    def __init__(self, driver):
        self.driver = driver
        self.trips =[]

    def trip(self, km):
        self.trips.append(km)

    @abstractmethod
    def total_cost(self):
        pass

    def __str__(self):
        return f"Transport revenue: {self.total_cost()} (driver: {self.driver.name})"

class Shuttle(Transport):
    def __init__(self, driver, flat_fee):
        super().__init__(driver)
        self.flat_fee = flat_fee

    def total_cost(self):
        return self.flat_fee

class Taxi(Transport):
    def __init__(self, driver, trip_fee, small_fee):
        super().__init__(driver)
        self.trip_fee = trip_fee
        self.small_fee = small_fee

    def total_cost(self):
        return self.trip_fee * len(self.trips) + sum(self.trips) * self.small_fee
class DiscountTaxi(Taxi):
    def total_cost(self):
        return super().total_cost() * 0.8

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