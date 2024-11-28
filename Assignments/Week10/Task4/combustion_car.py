from car import Car

class CombustionCar(Car):

    def __init__(self, gas_capacity, gas_per_100km):
        self.gas_capacity = gas_capacity
        self.gas_per_100km = gas_per_100km
        self.current_gas = gas_capacity

    def fuel(self, f):
        if f < 0:
            raise Warning("Invalid fuel amount")
        self.current_gas += f
        if self.current_gas > self.gas_capacity:
            raise Warning("Gas tank overfilled")
            self.current_gas = 0

    def get_gas_tank_status(self):
        return (self.current_gas, self.gas_capacity)

    def get_remaining_range(self):
        return (self.current_gas / self.gas_per_100km) * 100

    def drive(self, dist):
        if dist < 0:
            raise Warning("Invalid distance")
        required_gas = (dist / 100) * self.gas_per_100km
        if required_gas > self.current_gas:
            raise Warning("Fuel depleted")
            self.current_gas = 0
        else:
            self.current_gas -= required_gas







