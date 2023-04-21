import json
import os
from json import JSONDecodeError


class WorkWithJson:
    def __init__(self):
        self.heroes_lst = None


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

    def read_from_json(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            try:
                json_data = file.read()
                self.heroes_lst = json.loads(json_data)
            except JSONDecodeError:
                self.heroes_lst = []

        return self.heroes_lst

    def choose_hero(self, hero_name):
        for name in self.heroes_lst:
            if hero_name == name.get("name"):
                return name

            else:
                return print("Hero with this name doesn't exist")
