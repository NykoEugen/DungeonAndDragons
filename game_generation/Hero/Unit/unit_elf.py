from game_generation.Hero.FactoryAbstract.abstract_unit import AbstractUnit


class UnitElf(AbstractUnit):
    def __init__(self, name):
        self.name = name
        super().__init__(self.name)
        self.level = 1

        self.strength = 0
        self.dexterity = 2
        self.constitution = 0
        self.intelligence = 1
        self.wisdom = 0
        self.charisma = 0

    def create(self):
        print(f"Your hero name is {self.name}")

    def set_attr(self, points):
        while points != 0:
            print(f"You have {points} points.")
            attr = input("Choose attribut to add point (strength, dexterity, constitution,"
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

    def hero_attr(self):
        hero_attributs = {"strength": self.strength,
                          "dexterity": self.dexterity,
                          "constitution": self.constitution,
                          "intelligence": self.intelligence,
                          "wisdom": self.wisdom,
                          "charisma": self.charisma
                          }
        return hero_attributs
