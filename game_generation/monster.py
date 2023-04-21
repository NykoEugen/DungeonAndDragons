import random


class Monster:
    def generate_monster(self):
        adjectives = ["Жахливий", "Смертоносний", "Лютісний", "Кривавий", "Мерзенний"]
        nouns = ["Гидра", "Міномет", "Гоблін", "Відьма", "Мандрівний чумак", "Дракон"]
        monster_name = random.choice(adjectives) + " " + random.choice(nouns)
        monster_type_lst = ["common", "uncommon", "rare", "mythical", "legendary"]
        weights = [0.5, 0.3, 0.3, 0.05, 0.01]
        monster_type = random.choices(monster_type_lst, weights=weights)[0]
        unit = {"name": monster_name,
                "type": monster_type,
                "health": random.randint(60, 100),
                "damage": random.randint(5, 30),
                "reward_xp": random.randint(1, 7),
                "reward_gold": 5}
        return unit
