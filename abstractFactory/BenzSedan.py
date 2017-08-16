from abstractFactory.ISedan import ISedan


class BenzSedan(ISedan):
    def price(self):
        print('is a BenzSedan.price')
        return 3000000

    def horsepower(self):
        print('is a BenzSedan.horsepower')
        return 300