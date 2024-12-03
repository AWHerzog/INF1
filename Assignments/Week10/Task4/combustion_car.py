from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity: float, gas_per_100km: float):
        
        self.gas_capacity = gas_capacity
        self.gas_per_100km = gas_per_100km
        self.current_gas = gas_capacity

        if not isinstance(self.gas_capacity, float):
            raise Warning("Wrong input type")
        if not isinstance(self.gas_per_100km, float):
            raise Warning("Wrong input type")
        if not isinstance(self.current_gas, float):
            raise Warning("Wrong input type")
        if self.gas_capacity <= 0:
            raise Warning("Cannot be empty an empty tank/ charge")
        if self.gas_per_100km <= 0:
            raise Warning("Range cannot be less or equal to zero")

    def fuel(self, f):
        if not isinstance(f, (float)):
            raise Warning("Not an int or float")
        
        if f < 0:
            raise Warning("Invalid fuel amount")
        self.current_gas += f
        if self.current_gas > self.gas_capacity:
            raise Warning("Gas tank overfilled")
            

    def get_gas_tank_status(self):
        return (self.current_gas, self.gas_capacity)

    def get_remaining_range(self) -> float:
        return float((self.current_gas / self.gas_per_100km) * 100)

    def drive(self, dist: float):
        if not isinstance(dist, (float)):
            raise Warning("Not an int or float")
        
        if dist < 0:
            raise Warning("Invalid distance")
        
        max_distance = (self.current_gas / self.gas_per_100km) * 100

        
        if dist > max_distance:
            self.current_gas = 0
            raise Warning("Not enough fuel")
            
        else:
            required_gas = (dist / 100) * self.gas_per_100km
            self.current_gas -= required_gas
        return self.get_remaining_range()   







