from abc import ABCMeta, abstractmethod


class IAbstractFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_benz_factory(self):
        pass

    @abstractmethod
    def create_bmw_factory(self):
        pass