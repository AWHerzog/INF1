from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        self.max_battery_capacity = battery_size  
        self.battery_level = battery_size  
        self.battery_range_km = battery_range_km  

    def charge(self, kwh):
        if self.battery_level + kwh > self.max_battery_capacity:
            self.battery_level = 0  
            raise Warning("Battery is overfilled")
        else:
            self.battery_level += kwh  
        return self.battery_level

    def get_battery_status(self):
        return (self.battery_level, self.max_battery_capacity)

    def get_remaining_range(self):
        if self.battery_level == 0:
            return 0.0
        return (self.battery_level / self.max_battery_capacity) * self.battery_range_km

    def drive(self, dist):
        required_charge = dist * (self.max_battery_capacity / self.battery_range_km)

        if required_charge > self.battery_level:
            self.battery_level = 0.0  
            raise Warning("Not enough charge")

        self.battery_level -= required_charge

        return self.battery_level


    

    
