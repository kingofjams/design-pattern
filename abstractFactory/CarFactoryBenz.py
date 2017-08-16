from abstractFactory.ICarFactory import ICarFactory
from abstractFactory.BenzHatchback import BenzHatchback
from abstractFactory.BenzSedan import BenzSedan


class CarFactoryBenz(ICarFactory):
    def create_hatchback(self):
        return BenzHatchback()

    def create_sedan(self):
        return BenzSedan()

