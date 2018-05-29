# -*- coding: utf-8 -*-
"""Vehicles module"""

import parts as prt
import fuels as fu


class Car(object):
    """CAR class"""

    def __init__(self, price, engine=prt.ICEngine(fuel=fu.Gasoline, consumption=8, resource=200000), tank=prt.Tank(60), price_drop=0.01, owner=None):
        assert price > 0
        assert isinstance(tank, prt.Tank)
        assert isinstance(engine, prt.Engine)

        self._origin_price = price
        self._engine = engine
        self._tank = tank
        self._price_drop = price_drop
        self._tachograph = prt.Tachograph()

        # self._run_to_overhaul = run_to_overhaul
        # self._next_overhaul = run_to_overhaul

        self._owner = owner
        self._last_overhaul_distance = 0

        # logger.info("[CREATE CAR] {}".format(self))

    @property
    def origin_price(self):
        return self._origin_price

    @property
    def price_drop(self):
        return self._price_drop

    @property
    def distance(self):
        return self._tachograph.distance

    @property
    def price(self):
        return self.origin_price - self.price_drop * self.distance

    @property
    def fuel(self):
        return self._engine.fuel

    @property
    def tank(self):
        return self._tank

    @property
    def owner(self):
        return self._owner

    @property
    def engine(self):
        return self._engine

    @property
    def last_overhaul_distance(self):
        return self._last_overhaul_distance

    @property
    def next_overhaul_distance(self):
        return self.last_overhaul_distance + self.engine.resource

    @property
    def left_overhaul_distance(self):
        return self.next_overhaul_distance - self.distance

    def run(self, distance):
        self._tachograph.run(distance)

    def refuel(self, fuel_station):
        fuel_station.refuel(self)

    def overhaul(self, service_station):
        service_station.overhaul(self)


