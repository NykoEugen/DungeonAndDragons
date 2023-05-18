from game_generation.Hero.FactoryAbstract.race import Race


class Dwarf(Race):
    def __init__(self, race):
        self.race = race
        super().__init__(self.race)

    def create(self):
        print(f"Your hero race is {self.race}")

    def race_skill_1(self):
        print("First skill of dwarf")
