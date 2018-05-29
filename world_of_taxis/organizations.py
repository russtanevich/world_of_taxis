# -*- coding: utf-8 -*-
"""Organizations module"""
from settings import logger
from .cars import Car
import fuels as fu
import parts as prt


class TaxiCompany(object):
    """Owner class of taxopark"""
    _CAR_TYPE = Car

    def __init__(self, cars=(), balance=0):

        assert all(isinstance(car, type(self)._CAR_TYPE) for car in cars)  # Check for vehicle type
        assert balance >= 0  # check for money

        self._cars = set(cars)
        self._balance = balance

        logger.info("[CREATE COMPANY] {}".format(self))

    @property
    def cars(self):
        return self._cars

    @property
    def balance(self):
        return self._balance

    def pay(self, payment):
        self._balance -= payment
        logger.info("[PAYMENT] {} -- {}".format(self, payment))

    def error_if_not_car(self, car):
        if not isinstance(car, type(self)._CAR_TYPE):
            raise TypeError("{} is not {}".format(car, type(self)._CAR_TYPE))

    def add_car(self, car):
        self.error_if_not_car(car)
        self._cars.add(car)

    def add_cars(self, *cars):
        for car in cars:
            self.buy_car(car)

    def buy_car(self, car):
        self.error_if_not_car(car)
        self.pay(car.price)
        self.add_car(car)
        car.set_owner(self)
        logger.info("[BUY CAR] {} -- {}".format(self, car))

    def buy_cars(self, *cars):
        for car in cars:
            self.buy_car(car)

    def __str__(self):
        return "<{} #{}, ${}, {} cars>".format(
                    type(self).__name__,
                    id(self),
                    self.balance,
                    len(self.cars)
                )

    def __repr__(self):
        return str(self)


class ServiceStation(object):
    """Service station module"""
    _CAR_TYPE = Car

    _price_service = {
        fu.Diesel: 700,
        fu.Gas: 700,
        fu.AI92: 500,
        fu.AI95: 500
    }
    _price_parts = {
        prt.ICEngine: 3000
    }

    def __init__(self, price_service=_price_service, price_parts=_price_parts):
        self._price_service = price_service
        self._price_parts = price_parts

    @property
    def price_service(self):
        return self._price_service

    @property
    def price_parts(self):
        return self._price_parts

    def overhaul(self, car):
        assert isinstance(car, type(self)._CAR_TYPE)
        payment = self.bill_overhaul(car.engine)                            # CALCULATE PAYMENT
        car.owner.pay(payment)                                              # PAYMENT FOR OVERHAUL
        self.change_engine(car)                                             # CHANGE ENGINE

    def change_engine(self, car):
        fuel = fu.AI92 if issubclass(car.engine.fuel, fu.Gasoline) else car.engine.fuel
        engine = type(car.engine)(fuel=fuel, consumption=car.engine.consumption, resource=car.engine.resource)  # THE SAME ENGINE
        car.set_engine(engine)

    def bill_overhaul(self, engine):
        for type_engine in type(engine).__mro__:
            if type_engine in self.price_parts:
                price_engine = self.price_parts[type_engine]
                price_service = self.price_service[engine.fuel]
                return price_service + price_engine

        raise LookupError("NO {} in {}".format(engine, self))




class FuelStation(object):
    """Fuel Station class"""
    _CAR_TYPE = Car
    _prices = {
        fu.AI92: 2.2,
        fu.AI95: 2.4,
        fu.Diesel: 1.8,
        fu.Gas: 1.0
    }

    def __init__(self, prices=_prices):
        self._prices = prices

    @property
    def prices(self):
        return self._prices

    def refuel(self, car):
        assert isinstance(car, type(self)._CAR_TYPE)

        payment = (car.tank.volume - car.tank.level) * self.prices[car.fuel]
        car.owner.pay(payment)
        car.tank.fill()
