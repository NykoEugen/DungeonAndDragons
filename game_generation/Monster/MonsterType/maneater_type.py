from game_generation.Dice.dice import Dice
from game_generation.Monster.MonsterAbstract.monster_type import MonsterType


class ManeaterType(MonsterType):
    def __init__(self, monster_type):
        self.monster_type = monster_type
        super().__init__(self.monster_type)

    def create(self):
        print(f"Monster type is {self.monster_type}")

    def type_skill_1(self):
        print("First skill of Maneater")

    def health(self, attr):
        health = Dice.throw_dice("d20", "2")
        health += attr
        return health

    def damage(self, attr, points):
        damage = points + attr
        return damage
