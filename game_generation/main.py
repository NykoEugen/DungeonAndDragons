from game_generation.dice import Dice
from game_generation.Hero.hero import Hero
from game_generation.Hero.hero_action import HeroAction


def main():
    hero1 = Hero()
    print(f"Stage to set atribut")
    dice1 = Dice()
    throw_result = dice1.throw_dice("d6", "3")
    hero1_attr = hero1.set_atribut(throw_result)
    print(hero1_attr)







if __name__ == "__main__":
    main()
