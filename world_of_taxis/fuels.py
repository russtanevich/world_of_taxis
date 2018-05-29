# -*- coding: utf-8 -*-
"""Fuels module"""


class Fuel(object):
    """Fuel class"""
    pass


class LiquidFuel(Fuel):
    """Liquid fuel class"""
    pass


class Gasoline(LiquidFuel):
    pass


class Diesel(LiquidFuel):
    pass


class Gas(LiquidFuel):
    pass


class AI92(Gasoline):
    pass


class AI95(Gasoline):
    pass
