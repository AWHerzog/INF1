from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        
        self.is_electric_mode = True

    def switch_to_combustion(self):
        return self.is_electric_mode == False

    def switch_to_electric(self):
        return self.is_electric_mode == True

    def get_remaining_range(self):
        if self.is_electric_mode == True:
            return ElectricCar.get_remaining_range()
        else:
            return CombustionCar.get_remaining_range()

    def drive(self, dist):
        if self.is_electric_mode:
            try:
                ElectricCar.drive(self, dist)
            except Warning:
                print("Battery depleted, switching to combustion mode")
                self.switch_to_combustion()
                CombustionCar.drive(self, dist)
        else:
            try:
                CombustionCar.drive(self, dist)
            except Warning:
                print("Fuel depleted, switching to electric mode")
                self.switch_to_electric()
                ElectricCar.drive(self, dist)

    def get_gas_tank_status(self):
        return CombustionCar.get_gas_tank_status(self)

    def get_battery_status(self):
        return ElectricCar.get_battery_status(self)



