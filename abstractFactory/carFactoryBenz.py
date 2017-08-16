from iCarFactory import ICarFactory
from benzHatchback import BenzHatchback
from benzSedan import BenzSedan


class CarFactoryBenz(ICarFactory):
    def create_hatchback(self):
        return BenzHatchback()

    def create_sedan(self):
        return BenzSedan()

