from abc import ABC, abstractmethod


class MonsterAbc(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def set_attr(self, points): pass

    @abstractmethod
    def monster_attr(self): pass
