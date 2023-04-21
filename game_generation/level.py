import random


class Level:
    def generate_lvl(self):
        adjectives = ["Глибока", "Жахлива", "Містична", "Нижня", "Мерзенна"]
        nouns = ["Печера", "Грот", "Колодязь", "заглибина"]
        lvl_name = random.choice(adjectives) + " " + random.choice(nouns)
        monsters = random.randint(0, 1)
        chest = random.randint(0, 1)
        lvl = {"lvl_name": lvl_name,
               "monster": monsters,
               "chest": chest}
        return lvl
