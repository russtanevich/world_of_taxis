# -*- coding: utf-8 -*-
"""Parts module"""

from . import fuels as fu


class Engine(object):
    """Auto engine class"""

    def __init__(self, fuel, consumption, resource):
        self._fuel = fuel
        self._consumption = consumption
        self._resource = resource

    @property
    def fuel(self):
        return self._fuel

    @property
    def consumption(self):
        return self._consumption

    @property
    def resource(self):
        return self._resource


class ICEngine(Engine):
    """Internal Combustion Engine"""

    _allowed_fuel = (fu.Diesel, fu.Gas, fu.Gasoline)
    _default_consumption = 8
    _default_resource = 200000

    def __init__(self, fuel=_allowed_fuel[0], consumption=_default_consumption, resource=_default_resource):
        super(ICEngine, self).__init__(fuel, consumption, resource)


class Tank(object):
    """A car tank class"""

    def __init__(self, volume, level=0):
        self._volume = volume
        self._level = level
        self._fill_counter = 0

    @property
    def volume(self):
        return self._volume

    @property
    def level(self):
        return self._level

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
        return self._distance

    def run(self, km):
        self._distance += km



