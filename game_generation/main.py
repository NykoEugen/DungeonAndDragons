from game_generation.dice import Dice
from game_generation.hero import Hero
from game_generation.hero_action import HeroAction


def main():
    name = input("Create hero name: ")
    hero1 = Hero(name)
    hero1.set_race()
    hero1.set_class()
    all_inf = hero1.get_hero()
    action_hero1 = HeroAction(all_inf)
    dice = Dice()
    hero1_dice = dice.trow_dice("d6", "2")
    print(hero1_dice)




if __name__ == "__main__":
    main()
