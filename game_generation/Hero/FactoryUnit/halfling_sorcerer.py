from game_generation.Hero.Class.sorcerer import Sorcerer
from game_generation.Hero.FactoryAbstract.abstract_unit import AbstractUnit
from game_generation.Hero.FactoryAbstract.hero_class import HeroClass
from game_generation.Hero.FactoryAbstract.hero_factory import HeroAbstractFactory
from game_generation.Hero.FactoryAbstract.race import Race
from game_generation.Hero.Race.halfling import Halfling
from game_generation.Hero.Unit.unit_halfling import UnitHalfling


class HalflingSorcerer(HeroAbstractFactory):
    def __init__(self, name, race, hero_class):
        self.name = name
        self.race = race
        self.hero_class = hero_class

    def getHero(self) -> AbstractUnit:
        return UnitHalfling(self.name)

    def getRace(self) -> Race:
        return Halfling(self.race)

    def getClass(self) -> HeroClass:
        return Sorcerer(self.hero_class)
