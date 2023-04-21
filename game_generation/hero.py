from game_generation.work_with_json import WorkWithJson


class Hero:
    def __init__(self, hero_name, hero_race="Human", hero_class="None", strength=8, agility=8, intellect=8, charisma=8):
        self.hero_name = hero_name
        self.hero_race = hero_race
        self.hero_class = hero_class

        self.level = 1

        self.health_point = 100
        self.strength = strength
        self.agility = agility
        self.intellect = intellect
        self.charisma = charisma

        self.type_attack = "Melee"
        self.damage = 10
        self.defence = 5

        self.ability = None
        print(f"Hero {self.hero_name} created")

    def set_race(self):
        self.hero_race = input("Choose your hero race: ")
        match self.hero_race:
            case "Human":
                self.health_point = 100
                self.strength = 10
                self.agility = 7
                self.intellect = 5
                self.charisma = 10
            case "Elv":
                self.health_point = 80
                self.strength = 5
                self.agility = 12
                self.intellect = 10
                self.charisma = 5
            case "Dwarv":
                self.health_point = 110
                self.strength = 12
                self.agility = 5
                self.intellect = 8
                self.charisma = 7
            case "Halfling":
                self.health_point = 75
                self.strength = 5
                self.agility = 12
                self.intellect = 7
                self.charisma = 8
            case _:
                print("No one")
        return print(f"Your hero race: {self.hero_race}")

    def set_class(self):
        self.hero_class = input("Choose your hero class: ")
        match self.hero_class:
            case "Warrior":
                self.type_attack = "Melee"
                self.damage = 12
                self.defence = 10
            case "Wizard":
                self.type_attack = "Range"
                self.damage = 15
                self.defence = 0
            case "Priest":
                self.type_attack = "Range"
                self.damage = 5
                self.defence = 3
            case "Robber":
                self.type_attack = "Melee"
                self.damage = 8
                self.defence = 7
            case _:
                print("No one")
        return print(f"Your hero class: {self.hero_class}")

    def set_ability(self):
        pass

    def get_hero(self):
        hero = {"name": self.hero_name,
                "race": self.hero_race,
                "class": self.hero_class,
                "level": self.level,
                "health": self.health_point,
                "strength": self.strength,
                "agility": self.agility,
                "intellect": self.intellect,
                "charisma": self.charisma,
                "type_attack": self.type_attack,
                "damage": self.damage,
                "defence": self.defence,
                "ability": self.ability}
        filename = "Heroes.json"
        json = WorkWithJson()
        json.load_to_json(filename, hero)
        return hero



# hero = Hero("Clark")
# hero.set_race()
# hero.set_class()
# print(hero.hero_name)
# print(hero.hero_race)
# print(hero.hero_class)
# print(hero.strength)
# print(hero.agility)
# print(hero.intellect)
# print(hero.charisma)
# print(hero.damage)
# print(hero.defence)
# print(hero.type_attack)
# print(hero.get_hero())

