# -*- coding: utf-8 -*-
"""TEST module"""


from world_of_taxies import cars, fuels, organizations, parts


autos = [cars.Car(price=10000)]
company = organizations.TaxiCompany(balance=1000000)
company.buy_cars(*autos)


for auto in autos:
    auto.run(1000000)


print autos[0].distance
print company.balance
