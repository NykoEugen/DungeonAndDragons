# hero = {"name": "Stefan",
#         "race": "Elv",
#         "class": "Wizard",
#         "level": 1,
#         "health": 80,
#         "strength": 5,
#         "agility": 12,
#         "intellect": 10,
#         "charisma": 5,
#         "type_attack": "Range",
#         "damage": 15, "defence": 0,
#         "ability": "None"}
#
# damage = hero.get("damage")
# print(hero["health"])
#
# type_dice = "d20"
# dice_t = list(type_dice)
# dice_t.remove("d")
# dice = int("".join(dice_t))
# print(dice)
#
#
# def func(name=""):
#     if name != "":
#         print(name)
#     else:
#         print("empty")
#
#
# abc = func("fox")
# import random
# level = 3
# reward_xp = round(random.randint(1, 3) * level * 1.1, 1)
# print(reward_xp)
from game_generation.application import Application

hero = Application()
hero.choose_race()
hero.choose_hero_class()
print(hero.name, hero.race, hero.hero_class)
