from abc import ABCMeta, abstractmethod


class ISubject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def add_observer(self, observer_obj):
        pass
