import random

from game_generation.Monster.MonsterAbstract.monster_abs import MonsterAbc


class ManeaterBase(MonsterAbc):
    def __init__(self, name):
        self.name = name
        super().__init__(self.name)
        self.level = 1

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

    def create(self):
        print(f"Monster is created. {self.name}")

    def set_attr(self, points):
        while points != 0:
            attr_lst = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
            attr = random.choice(attr_lst)
            number_of_points = random.randint(0, points)
            match attr:
                case "strength":
                    self.strength += number_of_points
                    points -= number_of_points
                case "dexterity":
                    self.dexterity += number_of_points
                    points -= number_of_points
                case "constitution":
                    self.constitution += number_of_points
                    points -= number_of_points
                case "intelligence":
                    self.intelligence += number_of_points
                    points -= number_of_points
                case "wisdom":
                    self.wisdom += number_of_points
                    points -= number_of_points
                case "charisma":
                    self.charisma += number_of_points
                    points -= number_of_points

    def monster_attr(self):
        monster_attributs = {"strength": self.strength,
                          "dexterity": self.dexterity,
                          "constitution": self.constitution,
                          "intelligence": self.intelligence,
                          "wisdom": self.wisdom,
                          "charisma": self.charisma
                          }
        return monster_attributs
