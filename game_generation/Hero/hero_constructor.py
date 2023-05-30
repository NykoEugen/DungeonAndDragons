from game_generation.Hero.FactoryAbstract.hero_factory import HeroAbstractFactory


class HeroConstructor:
    def __init__(self, factory: HeroAbstractFactory):
        self._hero_factory = factory

    def create_hero(self):
        self.unit = self._hero_factory.getHero()
        self.race = self._hero_factory.getRace()
        self.hero_class = self._hero_factory.getClass()
        self.unit.create()
        self.race.create()
        self.hero_class.create()

    def set_attr(self, points):
        return self.unit.set_attr(points)

    def hero_attr(self):
        return self.unit.hero_attr()

    def make_damage(self):
        return self.hero_class.make_damage()

    def race_skill_1(self):
        return self.race.race_skill_1()
