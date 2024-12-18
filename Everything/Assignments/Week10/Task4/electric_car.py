from car import Car

class ElectricCar(Car):

    def __init__(self, battery_size, battery_range_km):
        
        self.battery_size = battery_size
        self.battery_range_km = battery_range_km
        self.current_charge = battery_size 

        if not isinstance(self.battery_size, float):
            raise Warning("Wrong input type")
        if not isinstance(self.battery_range_km, float):
            raise Warning("Wrong input type")
        if not isinstance(self.current_charge, float):
            raise Warning("Wrong input type")
        if self.battery_size <= 0:
            raise Warning("Cannot be empty an empty tank/ charge")
        if self.battery_range_km <= 0:
            raise Warning("Range cannot be smaller or equalt to 0")

    def charge(self, kwh):
        if not isinstance(kwh, (float)):
            raise Warning("Not an int or float")
        if kwh < 0:
            raise Warning("Invalid charge amount")
        self.current_charge += kwh
        if self.current_charge > self.battery_size:
            raise Warning("Battery overcharged")
            self.current_charge = 0

    def get_battery_status(self):
        return (self.current_charge, self.battery_size)
    
    def get_remaining_range(self) -> float:
        return float((self.current_charge / self.battery_size) * self.battery_range_km)

    def drive(self, dist):
        if not isinstance(dist, (float)):
            raise Warning("Not an int or float")
        if dist < 0:
            raise Warning("Invalid distance")
        
        
        required_charge = (dist / self.battery_range_km) * self.battery_size
        if required_charge > self.current_charge:
            self.current_charge = 0
            raise Warning("Battery depleted")
            
        else:
            
            self.current_charge -= required_charge
        return self.get_remaining_range()


    

    
