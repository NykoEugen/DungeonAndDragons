from game_generation.Hero.Class.warrior import Warrior
from game_generation.Hero.Race.human import Human
from game_generation.Hero.Factory.abstractunit import AbstractUnit
from game_generation.Hero.Factory.hero_class import HeroClass
from game_generation.Hero.Factory.hero_factory import HeroAbstractFactory
from game_generation.Hero.Factory.race import Race
from game_generation.Hero.Factory.unit import Unit


class HumanWarriorFactory(HeroAbstractFactory):
    def __init__(self, name, race, hero_class):
        self.name = name
        self.race = race
        self.hero_class = hero_class

    def getHero(self) -> AbstractUnit:
        return Unit(self.name)

    def getRace(self) -> Race:
        return Human(self.race)

    def getClass(self) -> HeroClass:
        return Warrior(self.hero_class)

