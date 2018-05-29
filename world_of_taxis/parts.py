# -*- coding: utf-8 -*-
"""Parts module"""

from . import fuels as fu


class Engine(object):
    """Auto engine class"""

    def __init__(self, fuel=fu.Gasoline, consumption=8, resource=200000, consumption_up=0.01/1000):
        self._fuel = fuel
        self._consumption = consumption
        self._resource = resource
        self._consumption_up = consumption_up

    @property
    def fuel(self):
        return self._fuel

    @property
    def consumption(self):
        return self._consumption

    @property
    def resource(self):
        return self._resource

    @property
    def consumption_up(self):
        return self._consumption_up

    def __str__(self):
        return "{} {}".format(self.__class__.__name__, self.fuel.__name__)

    def __repr__(self):
        return str(self)


class ICEngine(Engine):
    """Internal Combustion Engine"""

    _allowed_fuel = (fu.Diesel, fu.Gas, fu.Gasoline)
    _default_consumption = 8
    _default_resource = 200000

    def __init__(self, fuel=_allowed_fuel[0], consumption=_default_consumption, resource=_default_resource):
        super(ICEngine, self).__init__(fuel, consumption, resource)

    def set_gasoline(self, gasoline):
        if issubclass(self.fuel, fu.Gasoline) and issubclass(gasoline, fu.Gasoline):
            self._fuel = gasoline
        else:
            TypeError("You can change fuel only for Gasoline Engines. But get {} and {}".format(self, petrol))


class Tank(object):
    """A car tank class"""

    def __init__(self, volume=60, level=0):
        self._volume = volume
        self._level = level
        self._fill_counter = 0

    @property
    def volume(self):
        return self._volume

    @property
    def level(self):
        return round(self._level, 3)

    @property
    def fill_counter(self):
        return self._fill_counter

    def fill(self):
        self._level = self.volume
        self._fill_counter += 1

    def spend(self, fuel_spent):
        self._level -= fuel_spent


class Tachograph(object):
    """A car tachograph class"""

    def __init__(self):
        self._distance = 0

    @property
    def distance(self):
        return round(self._distance, 3)

    def run(self, km):
        self._distance += km



