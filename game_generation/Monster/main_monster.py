from game_generation.Dice.dice import Dice
from game_generation.Monster.MonsterAbstract.monster_factory import MonsterAbstractFactory
from game_generation.Monster.MonsterFactory.maneater_factory import ManeaterFactory
from game_generation.Monster.monster_constructor import MonsterConstructor


def create_monster(name, monster_type) -> MonsterAbstractFactory:
    m_name = name.lower().capitalize()
    m_monster_type = monster_type.lower().capitalize()
    factory_name = m_monster_type
    factory_dict = {
        "Maneater": ManeaterFactory,
    }
    return factory_dict[factory_name](m_name, m_monster_type)


if __name__ == '__main__':
    name = "Monster"
    monster_type = "Maneater"
    unit = create_monster(name, monster_type)
    monster = MonsterConstructor(unit)
    monster.create_monster()
    attributs = monster.set_attr(10)
    attr = monster.monster_attr()
    healt = monster.health(attr["constitution"])
    points = Dice.throw_dice("d4", "2")
    damage = monster.damage(attr["dexterity"] + attr["strength"], points)
    monster.type_skill_1()
    print(attr)
    print(healt, damage)

    full_monster = {"name": name,
                    "type": monster_type,
                    "attributs": attr,
                    "health": healt,
                    "damage": damage}

    print(full_monster)

    print(full_monster["attributs"]["wisdom"])
