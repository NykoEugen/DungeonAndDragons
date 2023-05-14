from abc import ABC, abstractmethod

from game_generation.Hero.Factory.hero_class import HeroClass
from game_generation.Hero.Factory.race import Race
from game_generation.Hero.Factory.abstractunit import AbstractUnit


class HeroAbstractFactory(ABC):
    @abstractmethod
    def getHero(self) -> AbstractUnit: pass

    @abstractmethod
    def getRace(self) -> Race: pass

    @abstractmethod
    def getClass(self) -> HeroClass: pass
