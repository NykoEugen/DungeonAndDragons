from abc import ABC, abstractmethod


class MonsterType(ABC):
    def __init__(self, monster_type):
        self.type = monster_type

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def type_skill_1(self): pass

    @abstractmethod
    def health(self, attr): pass

    @abstractmethod
    def damage(self, attr, points): pass



