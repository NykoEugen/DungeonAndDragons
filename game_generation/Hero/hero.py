from game_generation.work_with_json import WorkWithJson


class Hero:
    def __init__(self):
        self.hero_name = input("Create hero name: ")
        self.level = 1

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

        print(f"Hero {self.hero_name} created")


    def set_atribut(self, points):
        while points != 0:
            print(f"You have {points} points.")
            attr = input("Choose atribut to add point (strength, dexterity, constitution,"
                         "intelligence, wisdom, charisma): ")
            number_of_points = int(input("How many points add: "))
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

        hero_attr = {"strength": self.strength,
                     "dexterity": self.dexterity,
                     "constitution": self.constitution,
                     "intelligence": self.intelligence,
                     "wisdom": self.wisdom,
                     "charisma": self.charisma
                    }

        return hero_attr

    # def set_race(self):
    #     self.hero_race = input("Choose your hero race: ")
    #     match self.hero_race:
    #         case "Human":
    #             self.health_point = 100
    #             self.strength = 10
    #             self.agility = 7
    #             self.intellect = 5
    #             self.charisma = 10
    #         case "Elv":
    #             self.health_point = 80
    #             self.strength = 5
    #             self.agility = 12
    #             self.intellect = 10
    #             self.charisma = 5
    #         case "Dwarv":
    #             self.health_point = 110
    #             self.strength = 12
    #             self.agility = 5
    #             self.intellect = 8
    #             self.charisma = 7
    #         case "Halfling":
    #             self.health_point = 75
    #             self.strength = 5
    #             self.agility = 12
    #             self.intellect = 7
    #             self.charisma = 8
    #         case _:
    #             print("No one")
    #     return print(f"Your hero race: {self.hero_race}")
    #
    # def set_class(self):
    #     self.hero_class = input("Choose your hero class: ")
    #     match self.hero_class:
    #         case "Warrior":
    #             self.type_attack = "Melee"
    #             self.damage = 12
    #             self.defence = 10
    #         case "Wizard":
    #             self.type_attack = "Range"
    #             self.damage = 15
    #             self.defence = 0
    #         case "Priest":
    #             self.type_attack = "Range"
    #             self.damage = 5
    #             self.defence = 3
    #         case "Robber":
    #             self.type_attack = "Melee"
    #             self.damage = 8
    #             self.defence = 7
    #         case _:
    #             print("No one")
    #     return print(f"Your hero class: {self.hero_class}")
    #
    # def set_ability(self):
    #     pass
    #
    # def get_hero(self):
    #     hero = {"name": self.hero_name,
    #             "race": self.hero_race,
    #             "class": self.hero_class,
    #             "level": self.level,
    #             "health": self.health_point,
    #             "strength": self.strength,
    #             "agility": self.agility,
    #             "intellect": self.intellect,
    #             "charisma": self.charisma,
    #             "type_attack": self.type_attack,
    #             "damage": self.damage,
    #             "defence": self.defence,
    #             "ability": self.ability}
    #     filename = "../Heroes.json"
    #     json = WorkWithJson()
    #     json.load_to_json(filename, hero)
    #     return hero



# hero = Hero()
# print(hero.hero_name)
# print(hero.strength)
# print(hero.dexterity)
# print(hero.intelligence)
# print(hero.charisma)
# hero_attr = hero.set_atribut(10)
# print(hero.strength)
# print(hero.dexterity)
# print(hero.intelligence)
# print(hero.charisma)
# print(hero_attr)
