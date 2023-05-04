class HeroAction:
    def __init__(self, hero):
        self.hero = hero
        self.health = self.hero["health"]
        self.defence = self.hero["defence"]

    def make_damage(self, dice):
        damage = self.hero["damage"] + dice
        return damage

    def healing(self, heal):
        self.health += heal
        self.hero["health"] = self.health
        print(f"Health: {self.health}")

    def take_damage(self, damage):
        self.health -= damage - (self.defence/10)
        self.hero["health"] = self.health
        print(f"Health: {self.health}")







# hero = HeroAction({"name": "Stefan", "race": "Elv", "class": "Wizard", "level": 1, "health": 80, "strength": 5, "agility": 12, "intellect": 10, "charisma": 5, "type_attack": "Range", "damage": 15, "defence": 0, "ability": "None"})
# take_damage = 12
# hero.take_damage(take_damage)
# print(hero.hero)
#


