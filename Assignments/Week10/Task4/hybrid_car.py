from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(CombustionCar, ElectricCar):
    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.electric = True

    def switch_to_combustion(self):
        self.electric = False

    def switch_to_electric(self):
        self.electric = True


    def get_remaining_range(self):
        return CombustionCar.get_remaining_range(self) + ElectricCar.get_remaining_range(self)

    def drive(self, dist):
        if not isinstance(dist, (float)):
            raise Warning("Not an int or float")
        
        if self.electric:
            remaining_electric_range = ElectricCar.get_remaining_range(self)
            if remaining_electric_range >= dist:
                ElectricCar.drive(self, dist)
            else:
                ElectricCar.drive(self, remaining_electric_range)
                self.switch_to_combustion()
                remaining_distance = dist - remaining_electric_range
                remaining_combustion_range = CombustionCar.get_remaining_range(self)
                
                if remaining_combustion_range >= remaining_distance:
                    CombustionCar.drive(self, remaining_distance)
                else:
                    CombustionCar.drive(self, remaining_combustion_range)
                    raise Warning("Both fuel and battery are depleted")
        
        else:
            remaining_combustion_range = CombustionCar.get_remaining_range(self)
            if remaining_combustion_range >= dist:
                CombustionCar.drive(self, dist)
            else:
                CombustionCar.drive(self, remaining_combustion_range)
                self.switch_to_electric()
                remaining_distance = dist - remaining_combustion_range
                remaining_electric_range = ElectricCar.get_remaining_range(self)

                if remaining_electric_range >= remaining_distance:
                    ElectricCar.drive(self, remaining_distance)
                else:
                    ElectricCar.drive(self, remaining_electric_range)
                    raise Warning("Both fuel and battery are depleted")



