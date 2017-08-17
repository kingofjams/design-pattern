from iObserver import IObserver


class AccountingObserver(IObserver):

    def update(self):
        print('我是会计，我来开具发票。')
