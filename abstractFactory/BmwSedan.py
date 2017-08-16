from abstractFactory.ISedan import ISedan


class BmwSedan(ISedan):
    def price(self):
        print('is a BmwSedan.price')
        return 35000000

    def horsepower(self):
        print('is a BmwSedan.horsepower')
        return 300


