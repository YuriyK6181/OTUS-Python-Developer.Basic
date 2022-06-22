from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    """
    класс `Plane`, наследник `Vehicle`
    """
    cargo = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False
        self.max_cargo = max_cargo

    def show_info(self, opername=""):
        if opername != "":
            oper_str = "after "+opername
        else:
            oper_str = ""
        print(self.__class__.__name__, "Info", oper_str, ": ODO=", self.odo, "km, Started=", self.started,
              ", Cargo =", self.cargo, "Tonns, Fuel left=", self.fuel, "L")

    def load_cargo(self, cargo):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
            self.show_info("Load Cargo")
        else:
            raise CargoOverload("Cargo Overload!")

    def remove_all_cargo(self):
        res = self.cargo
        self.cargo = 0
        self.show_info("Remove All Cargo")
        return res


def test():
    p = Plane(15000, 500, 3, 1000)
    p.load_cargo(50)
    p.remove_all_cargo()
    p.load_cargo(120)

    p.fuel_tank = 10000
    p.refuel(5000)
    p.start()
    p.move(100)


if __name__ == "__main__":
    test()
