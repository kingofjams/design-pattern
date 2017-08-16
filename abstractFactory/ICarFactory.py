from abc import ABCMeta, abstractmethod


class ICarFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_hatchback(self):
        pass

    @abstractmethod
    def create_sedan(self):
        pass
