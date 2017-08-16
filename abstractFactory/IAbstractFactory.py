from abc import ABCMeta, abstractmethod


class IAbstractFactory(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_factory(self):
        pass
