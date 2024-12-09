
from abc import ABC, abstractmethod

class Driver:
    pass

class Transport:
    pass

class Shuttle:
    pass

class Taxi:
    pass

class DiscountTaxi:
    pass


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