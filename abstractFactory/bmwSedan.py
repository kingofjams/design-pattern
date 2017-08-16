from iParameter import IParameter


class BmwSedan(IParameter):
    def price(self):
        print('is a BmwSedan.price')
        return 35000000

    def horsepower(self):
        print('is a BmwSedan.horsepower')
        return 300


