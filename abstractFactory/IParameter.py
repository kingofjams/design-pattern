from abc import ABCMeta, abstractmethod


class IParameter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def horsepower(self):
        pass
