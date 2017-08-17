from iObserver import IObserver


class CashierObserver(IObserver):

    def update(self):
        print('我是出纳员，我给登记入账。')
