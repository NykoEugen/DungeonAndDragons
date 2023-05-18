from abc import ABC, abstractmethod


class Race(ABC):
    def __init__(self, race):
        self.race = race

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def race_skill_1(self): pass
