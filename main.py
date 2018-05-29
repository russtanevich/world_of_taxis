# -*- coding: utf-8 -*-
"""TEST module"""


from world_of_taxies import cars, fuels, organizations, parts, settings


autos = [cars.Car(price=10000) for i in range(5)]
company = organizations.TaxiCompany(balance=1000000)
company.buy_cars(*autos)
fuel_station = organizations.FuelStation()


for auto in autos:
    auto.refuel(fuel_station)
    auto.run(10000)
    auto.set_engine(parts.ICEngine())
    auto.run(10000)

for auto in autos:
        format_string = "{car}"
        format_line = {
            "car": auto
        }
        settings.statistic.info(format_string.format(**format_line))
