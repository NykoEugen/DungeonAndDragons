from game_generation.choose_confirm import ChooseConfirm


class Application:
    def __init__(self, name=None, race=None, hero_class=None):
        print("Welcome Hero")
        self.name = name
        self.name = input("Choose your hero name: ").lower().capitalize()
        self.race = race
        self.hero_class = hero_class

    def choose_race(self):
        temp = True
        while temp:
            self.race = input("Choose hero race, some info: ").lower().capitalize()
            match self.race:
                case "Human":
                    print("Human race hero have advantages:"
                          "+1 to all attributes."
                          "Disadvantages: None")

                case "Halfling":
                    print("Halfling race hero have advantages:"
                          "+2 to dexterity."
                          "Disadvantages: None")

                case "Gnome":
                    print("Gnome race hero have advantages:"
                          "+2 to intelligence."
                          "Disadvantages: None")

                case "Elf":
                    print("Elf race hero have advantages:"
                          "+2 to dexterity,"
                          "+1 to intelligence"
                          "Disadvantages: None")

                case "Dwarf":
                    print("Dwarf race hero have advantages:"
                          "+2 to constitution."
                          "Disadvantages: None")

                case _:
                    print("This race is not define!")
                    return True
            temp = ChooseConfirm.choose_confirm()
        print(f"You choose race {self.race}")
        return self.race

    def choose_hero_class(self):
        temp = True
        while temp:
            self.hero_class = input("Choose hero class, some info: ").lower().capitalize()
            match self.hero_class:
                case "Ranger":
                    print("Ranger hero class have advantages: None."
                          "Disadvantages: None")

                case "Sorcerer":
                    print("Sorcerer hero class have advantages: None."
                          "Disadvantages: None")

                case "Warrior":
                    print("Warrior hero class have advantages: None."
                          "Disadvantages: None")

                case "Wizard":
                    print("Wizard hero class have advantages: None."
                          "Disadvantages: None")

                case _:
                    print("This class is not define!")
                    return True
            temp = ChooseConfirm.choose_confirm()
        print(f"You choose class {self.hero_class}")
        return self.hero_class
