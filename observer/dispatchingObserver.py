from iObserver import IObserver


class DispatchingObserver(IObserver):

    def update(self):
        print('我是配送员，我来发货。')
