from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        self.max_gas_capacity = gas_capacity  
        self.gas_capacity = gas_capacity  
        self.gas_per_100km = gas_per_100km

    def fuel(self, f):
        if self.gas_capacity + f > self.max_gas_capacity:
            self.gas_capacity = 0
            raise Warning("Gas tank is overfilled")
        else: 
            self.gas_capacity += f
        return self.gas_capacity

    def get_gas_tank_status(self):
        return (self.gas_capacity, self.max_gas_capacity)

    def get_remaining_range(self):
        if self.gas_capacity == 0:
            return 0.0
        return self.gas_capacity / self.gas_per_100km * 100

    def drive(self, dist):
        required_fuel = dist * (self.gas_per_100km / 100)
        if required_fuel > self.gas_capacity:
            self.gas_capacity = 0.0
            raise Warning("Not enough fuel")
        self.gas_capacity -= required_fuel
        return self.gas_capacity







