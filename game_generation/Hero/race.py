from game_generation.Hero.hero import Hero


class Race(Hero):
    def __init__(self, hero):
        super().__init__()
        self.hero = hero
