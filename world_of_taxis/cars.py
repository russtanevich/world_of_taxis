# -*- coding: utf-8 -*-
"""Vehicles module"""

import parts as prt


class Car(object):
    """CAR class"""

    def __init__(self, price=10000, engine=None, tank=None, price_drop=0.01, owner=None):

        engine = engine if engine else prt.ICEngine()
        tank = tank if tank else prt.Tank()

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
    def after_overhaul_distance(self):
        return self.distance - self.last_overhaul_distance

    @property
    def next_overhaul_distance(self):
        return self.last_overhaul_distance + self.engine.resource

    @property
    def left_overhaul_distance(self):
        return self.next_overhaul_distance - self.distance

    @property
    def fuel_consumption(self):
        return self.engine.consumption * (1 + self.engine.consumption_up * self.after_overhaul_distance)

    def run(self, distance):
        self._tachograph.run(distance)

    def refuel(self, fuel_station):
        fuel_station.refuel(self)

    def overhaul(self, service_station):
        service_station.overhaul(self)

    def set_engine(self, engine):
        assert isinstance(engine, prt.Engine)
        self._engine = engine
        self._last_overhaul_distance = self.distance

    def set_owner(self, owner):
        self._owner = owner

    def __str__(self):
        return "<{} #{} ${} {} {}/{}L {}L/100km {}km>".format(
                    type(self).__name__,
                    id(self),
                    self.price,
                    self.fuel.__name__,
                    self.tank.level,
                    self.tank.volume,
                    self.fuel_consumption,
                    self.distance
                )

    def __repr__(self):
        return str(self)

