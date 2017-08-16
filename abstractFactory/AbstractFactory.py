from abstractFactory.IAbstractFactory import IAbstractFactory
from abstractFactory.CarFactoryBenz import CarFactoryBenz
from abstractFactory.CarFactoryBmw import CarFactoryBmw


class AbstractFactory(IAbstractFactory):
    def create_benz_factory(self):
        return CarFactoryBenz()

    def create_bmw_factory(self):
        return CarFactoryBmw()






