from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    """
    класс `Car`, наследник `Vehicle`
    """
    engine: Engine

    def __init__(self, weight, fuel, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.odo = 0
        self.fuel = fuel
        self.weight = weight
        self.started = False
        self.fuel_consumption = fuel_consumption

    def set_engine(self, engine):
        if not isinstance(engine, Engine):
            raise TypeError("Expected type Engine")
        else:
            self.engine = engine


def test():
    c = Car(1800, 0, 2)
    c.fuel_tank = 600
    print("New Car Info: ODO=", c.odo, "Started=", c.started,
          ", Fuel left=", c.fuel, "L, Fuel Consumption (L/km)=", c.fuel_consumption)

    eng = Engine(volume=2500, pistons=6)
    c.set_engine(eng)
    print("Car Engine1 V=", c.engine.volume, "cm3, Pistons=", c.engine.pistons)

    eng2 = Engine(volume=1500, pistons=4)
    c.set_engine(eng2)
    print("Car Engine2 V=", c.engine.volume, "cm3, Pistons=", c.engine.pistons)

    c.refuel(200)
    c.start()

    c.move(20)
    c.refuel(340)

    c.move(100)

    c.refuel(130)
    c.refuel(150)

    c.move(250)
    c.refuel(200)
    c.start()
    c.move(100)


if __name__ == "__main__":
    test()
