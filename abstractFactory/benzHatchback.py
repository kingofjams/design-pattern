from iParameter import IParameter


class BenzHatchback(IParameter):
    def price(self):
        print('is a BenzHatchback.price')
        return 20000000

    def horsepower(self):
        print('is a BenzHatchback.horsepower')
        return 200
