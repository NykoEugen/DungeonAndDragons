from game_generation.Hero.Class.warrior import Warrior
from game_generation.Hero.FactoryAbstract.abstract_unit import AbstractUnit
from game_generation.Hero.FactoryAbstract.hero_class import HeroClass
from game_generation.Hero.FactoryAbstract.hero_factory import HeroAbstractFactory
from game_generation.Hero.FactoryAbstract.race import Race
from game_generation.Hero.Race.elf import Elf
from game_generation.Hero.Unit.unit_elf import UnitElf


class ElfWarrior(HeroAbstractFactory):
    def __init__(self, name, race, hero_class):
        self.name = name
        self.race = race
        self.hero_class = hero_class

    def getHero(self) -> AbstractUnit:
        return UnitElf(self.name)

    def getRace(self) -> Race:
        return Elf(self.race)

    def getClass(self) -> HeroClass:
        return Warrior(self.hero_class)
