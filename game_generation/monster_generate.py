import json


class Monster:
    def unpack_json(self):
        with open("rooms.json", "r+") as file:
            data = file.read()
            dict_data = json.loads(data)
        return dict_data