from abstractFactory.ICarFactory import ICarFactory
from abstractFactory.BmwHatchback import BmwHatchback
from abstractFactory.BmwSedan import BmwSedan


class CarFactoryBenz(ICarFactory):
    def create_hatchback(self):
        return BmwHatchback()

    def create_sedan(self):
        return BmwSedan()