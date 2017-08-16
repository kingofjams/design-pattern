from iAbstractFactory import IAbstractFactory
from carFactoryBenz import CarFactoryBenz
from carFactoryBmw import CarFactoryBmw


class AbstractFactory(IAbstractFactory):
    def create_benz_factory(self):
        return CarFactoryBenz()

    def create_bmw_factory(self):
        return CarFactoryBmw()






