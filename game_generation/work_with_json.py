import json
import os
from json import JSONDecodeError


class WorkWithJson:
    def __init__(self):
        self.heroes_lst = None

    def load_to_json(self, file_name, new_data, hero_name=""):
        if not os.path.isfile(file_name):
            with open(file_name, "w", encoding="utf-8") as file:
                file.write('[]')
        with open(file_name, "r", encoding="utf-8") as file:
            try:
                json_data = file.read()
                data = json.loads(json_data)
            except JSONDecodeError:
                data = []

        if hero_name != "":
            for hero in data:
                if hero["name"] == hero_name:
                    data.remove(hero)
            data.append(new_data)
        else:
            data.append(new_data)

        new_json_data = json.dumps(data, ensure_ascii=False)
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(new_json_data)
        return print("Hero was update successful")

    def read_from_json(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            try:
                json_data = file.read()
                self.heroes_lst = json.loads(json_data)
            except JSONDecodeError:
                self.heroes_lst = []

        return self.heroes_lst


data = {"name": "Fox",
        "race": "Elv",
        "class": "Warrior",
        "level": 20,
        "health": 30,
        "strength": 5,
        "agility": 12,
        "intellect": 10,
        "charisma": 5,
        "type_attack": "Range",
        "damage": 15,
        "defence": 0,
        "ability": "None"}
abc = WorkWithJson()
lst = abc.load_to_json("Heroes.json", data, "Fox")
lst = abc.read_from_json("Heroes.json")
print(lst)
