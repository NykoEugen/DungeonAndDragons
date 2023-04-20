import json
import os
import random
from json import JSONDecodeError


class GenerateItem:

    def load_to_json(self, file_name, new_data):
        if not os.path.isfile(file_name):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write('[]')
        with open(file_name, "r", encoding="utf-8") as file:
            try:
                json_data = file.read()
                data = json.loads(json_data)
            except JSONDecodeError:
                data = []

        data.append(new_data)

        new_json_data = json.dumps(data, ensure_ascii=False)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(new_json_data)



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
        GenerateItem.load_to_json(self, "monsters.json", unit)
        return unit

    def generate_lvl(self):
        adjectives = ["Глибока", "Жахлива", "Містична", "Нижня", "Мерзенна"]
        nouns = ["Печера", "Грот", "Колодязь", "заглибина"]
        lvl_name = random.choice(adjectives) + " " + random.choice(nouns)
        monsters = random.randint(0, 1)
        chest = random.randint(0, 1)
        lvl = {"lvl_name": lvl_name,
               "monster": monsters,
               "chest": chest}
        GenerateItem.load_to_json(self, "rooms.json", lvl)
        return lvl


level = GenerateItem()
print(level.generate_lvl())
print(level.generate_monster())