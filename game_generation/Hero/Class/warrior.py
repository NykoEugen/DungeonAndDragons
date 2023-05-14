from game_generation.Hero.Factory.hero_class import HeroClass


class Warrior(HeroClass):
    def __init__(self, hero_class):
        self.hero_class = hero_class
        super().__init__(self.hero_class)

    def create(self):
        print(f"Your hero class is {self.hero_class}")

    def make_damage(self):
        print("Damage")
