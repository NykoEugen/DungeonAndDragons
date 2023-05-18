from abc import ABC, abstractmethod


class AbstractUnit(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def set_attr(self, points): pass

    @abstractmethod
    def hero_attr(self): pass
