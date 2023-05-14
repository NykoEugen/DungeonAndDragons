from abc import abstractmethod, ABC


class HeroClass(ABC):
    def __init__(self, hero_class):
        self.hero_class = hero_class

    @abstractmethod
    def create(self): pass

    @abstractmethod
    def make_damage(self): pass
