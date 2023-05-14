from game_generation.Hero.Factory.hero_factory import HeroAbstractFactory
from game_generation.Hero.Factory.base_class_factory import HumanWarriorFactory


class Application:
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



def create_factory(name, race, hero_class) -> HeroAbstractFactory:
    factory_name = race + hero_class
    factory_dict = {
        "HumanWarrior": HumanWarriorFactory
    }
    return factory_dict[factory_name](name, race, hero_class)


if __name__ == '__main__':
    name = "Alex"
    race = "Human"
    hero_class = "Warrior"
    unit = create_factory(name, race, hero_class)
    hero = Application(unit)
    hero.create_hero()
    attributs = hero.set_attr(10)
    attr = hero.hero_attr()
    hero.make_damage()
    hero.race_skill_1()
    print(attr)

