from iCarFactory import ICarFactory
from bmwHatchback import BmwHatchback
from bmwSedan import BmwSedan


class CarFactoryBmw(ICarFactory):
    def create_hatchback(self):
        return BmwHatchback()

    def create_sedan(self):
        return BmwSedan()
