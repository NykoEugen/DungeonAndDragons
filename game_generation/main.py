from game_generation.hero import Hero


def main():
    name = input("Create hero name: ")
    hero1 = Hero(name)
    hero1.set_race()
    hero1.set_class()
    hero1.get_hero()


if __name__ == "__main__":
    while True:
        main()
