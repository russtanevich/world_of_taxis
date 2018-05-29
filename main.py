# -*- coding: utf-8 -*-
"""TEST module"""
import random
from world_of_taxis import cars, settings
from world_of_taxis import organizations as org
from world_of_taxis import fuels as fu
from world_of_taxis import parts as prt
from world_of_taxis.settings import logger


class Cub(cars.Car):
    """The special class for homework"""

    _DIST_CHANGE_FUEL = 50000
    _counter = 0
    _price = 10000
    _engines = {
        "gasoline": {"fuel": fu.AI92, "consumption": 8, "resource": 100000},
        "diesel": {"fuel": fu.Diesel, "consumption": 6, "resource": 150000}
    }
    _price_drop = {
        "gasoline": 9.5 / 1000,
        "diesel": 10.5 / 1000
    }

    def __init__(self):
        Cub._counter += 1
        price = Cub._price

        engine = prt.ICEngine(**Cub._engines["diesel"]) if (Cub._counter % 3 == 0) else prt.ICEngine(**Cub._engines["gasoline"])
        tank = prt.Tank(volume=75) if (Cub._counter % 5 == 0) else prt.Tank(volume=60)
        price_drop = Cub._price_drop["diesel"] if (Cub._counter % 3 == 0) else Cub._price_drop["gasoline"]

        super(Cub, self).__init__(price=price, engine=engine, tank=tank, price_drop=price_drop)

    def run_by_chunk(self, distance):
        super(Cub, self).run(distance)

    def run(self, distance):
        distance_left = distance
        while distance_left > 0:

            distance_all_fuel = self.tank.level / self.fuel_consumption * 100
            distance_to_overhaul = self.left_overhaul_distance

            if self.fuel is fu.AI92 and self.after_overhaul_distance < type(self)._DIST_CHANGE_FUEL:
                distance_to_change_fuel = type(self)._DIST_CHANGE_FUEL - self.after_overhaul_distance

                distance = min(distance_all_fuel, distance_to_overhaul, distance_to_change_fuel, distance_left)
            else:
                distance = min(distance_all_fuel, distance_to_overhaul, distance_left)

            self.run_by_chunk(distance)
            distance_left -= distance

            if self.tank.level <= 0:
                org.FuelStation().refuel(self)
                logger.info("[REFUEL] {}".format(self))
            elif self.left_overhaul_distance <= 0:
                org.ServiceStation().overhaul(self)
                logger.info("[OVERHAUL] {}".format(self))
            elif self.engine.fuel is fu.AI92 and self.after_overhaul_distance == type(self)._DIST_CHANGE_FUEL:
                self.engine.set_gasoline(fu.AI95)
                logger.info("[CHANGE FUEL] {}".format(self))


if __name__ == "__main__":

    autos = [Cub() for _ in range(200)]
    company = org.TaxiCompany(balance=200*20000)
    company.buy_cars(*autos)

    for auto in autos:
        auto.run(random.randint(55000, 286000))

    for auto in autos:
            format_string = "{car}"
            format_line = {
                "car": auto
            }
            settings.statistic.info(format_string.format(**format_line))
