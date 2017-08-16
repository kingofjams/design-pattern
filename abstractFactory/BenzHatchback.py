from abstractFactory.IHatchback import IHatchback


class BenzHatchback(IHatchback):
    def price(self):
        print('is a BenzHatchback.price')
        return 20000000

    def horsepower(self):
        print('is a BenzHatchback.horsepower')
        return 200
