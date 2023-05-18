from game_generation.Hero.Class.wizard import Wizard
from game_generation.Hero.FactoryAbstract.abstract_unit import AbstractUnit
from game_generation.Hero.FactoryAbstract.hero_class import HeroClass
from game_generation.Hero.FactoryAbstract.hero_factory import HeroAbstractFactory
from game_generation.Hero.FactoryAbstract.race import Race
from game_generation.Hero.Race.gnome import Gnome
from game_generation.Hero.Unit.unit_gnome import UnitGnome


class GnomeWizard(HeroAbstractFactory):
    def __init__(self, name, race, hero_class):
        self.name = name
        self.race = race
        self.hero_class = hero_class

    def getHero(self) -> AbstractUnit:
        return UnitGnome(self.name)

    def getRace(self) -> Race:
        return Gnome(self.race)

    def getClass(self) -> HeroClass:
        return Wizard(self.hero_class)
