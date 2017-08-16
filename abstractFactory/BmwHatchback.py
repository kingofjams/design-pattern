from abstractFactory.IHatchback import IHatchback


class BmwHatchback(IHatchback):
    def price(self):
        print('is a BmwHatchback.price')
        return 25000000

    def horsepower(self):
        print('is a BmwHatchback.horsepower')
        return 250
