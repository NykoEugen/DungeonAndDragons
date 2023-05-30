from game_generation.Monster.MonsterAbstract.monster_factory import MonsterAbstractFactory


class MonsterConstructor:
    def __init__(self, factory: MonsterAbstractFactory):
        self._monster_factory = factory

    def create_monster(self):
        self.monster = self._monster_factory.getMonster()
        self.monster_type = self._monster_factory.getType()
        self.monster.create()
        self.monster_type.create()

    def set_attr(self, points):
        return self.monster.set_attr(points)

    def monster_attr(self):
        return self.monster.monster_attr()

    def type_skill_1(self):
        return self.monster_type.type_skill_1()

    def health(self, attr):
        return self.monster_type.health(attr)

    def damage(self, attr, points):
        return self.monster_type.damage(attr, points)
