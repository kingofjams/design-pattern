from iSubject import ISubject


class OrderSubject(ISubject):
    observers = []

    def add_observer(self, observer_obj):
        self.observers.append(observer_obj)

    def notify(self):
        for observer in self.observers:
            observer.update()
