from abc import ABC

class Vehicle:
    color = "White"
    def __init__(self, max_speed = 10, mileage = 0):
        self.max_speed = max_speed
        self.mileage = mileage
        self._private_var1 = "PV1"
        self.__private_var2__ = "PV2"

    def show_info(self):
        print(f"Max speed is {self.max_speed}, Mileage is {self.mileage}")

class Bus(Vehicle):
    def __init__(self, max_speed = 10, mileage = 0, seating_capacity=50):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def show_info(self):
        super().show_info()
        print("Overridden function")

    def show_bus_info(self):
        print(f"Bus max speed is {self.max_speed}, Bus mileage is {self.mileage}, Seating capacity is {self.seating_capacity}, color is {self.color}")


car_model = Bus()
import Tuples
print(__name__)


# print(car_model.show_info())
# print(car_model._private_var1)
# print(dir(car_model))
# print(car_model.__private_var2__)
# car_model.show_bus_info()
# print(type(car_model))


