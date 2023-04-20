import json
import random


class RoomGenerate:
    def unpack_json(self):
        with open("rooms.json", "r+") as file:
            data = file.read()
            dict_data = json.loads(data)
        return dict_data

    def room_choose(self):
        room_lst = RoomGenerate.unpack_json(self)
        room = random.choice(room_lst)
        return room

