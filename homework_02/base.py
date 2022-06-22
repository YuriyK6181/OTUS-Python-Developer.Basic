from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 1800
    started = False
    fuel = 0
    fuel_consumption = 12
    fuel_tank = 60
    odo = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def show_info(self, opername=""):
        if opername != "":
            oper_str = "after "+opername
        else:
            oper_str = ""
        print(self.__class__.__name__, "Info", oper_str, ": ODO=", self.odo, "km, Started=",
              self.started, ", Fuel left=", self.fuel, "L")

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                self.show_info("Engine Start")
            else:
                raise LowFuelError("Low Fuel!")

    def refuel(self, volume):
        if self.fuel + volume > self.fuel_tank:
            raise ValueError("The fuel tank can only hold ", self.fuel_tank)
        else:
            self.fuel += volume
            self.show_info("Refuel "+str(volume)+" L")

    def get_distance_limit(self):
        res = 0
        if self.fuel_consumption > 0:
            if self.fuel > 0:
                # res = self.fuel / self.fuel_consumption * 100
                res = self.fuel / self.fuel_consumption
        return res

    def get_fuel_for_distance(self, distance):
        res = 0
        if self.fuel_consumption > 0:
            if distance > 0:
                res = self.fuel_consumption * distance
        return res

    def move(self, distance):
        # if self.started:
        if distance is None:
            distance = 0
        if distance <= 0:
            raise ValueError('Distance is incorrect!')
        limit_km = self.get_distance_limit()
        if distance > limit_km:
            raise NotEnoughFuel(
                "Not Enough Fuel for distance " + str(distance) + " km, maximum distance is " + str(limit_km) + " km")
        else:
            self.fuel -= self.get_fuel_for_distance(distance)
            self.odo += distance
            self.show_info("Moving on " + str(distance) + "km")
        # else:
        #    print('Engine not started!')


def test():
    v = Vehicle(1500, 200, 10)
    print("Vehicle odo=", v.odo, "started=", v.started, "fuel=", v.fuel, "fuel_consumption=", v.fuel_consumption)
    v.start()
    print("Vehicle odo=", v.odo, "started=", v.started, "fuel=", v.fuel, "fuel_consumption=", v.fuel_consumption)
    # print("Limit, km=", v.get_distance_limit())
    v.move(10)
    print("Vehicle odo=", v.odo, "started=", v.started, "fuel=", v.fuel, "fuel_consumption=", v.fuel_consumption)


if __name__ == "__main__":
    test()
