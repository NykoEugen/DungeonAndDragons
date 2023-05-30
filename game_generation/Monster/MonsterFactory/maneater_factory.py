from game_generation.Monster.MonsterAbstract.monster_abs import MonsterAbc
from game_generation.Monster.MonsterAbstract.monster_factory import MonsterAbstractFactory
from game_generation.Monster.MonsterAbstract.monster_type import MonsterType
from game_generation.Monster.MonsterBase.maneater_base import ManeaterBase
from game_generation.Monster.MonsterType.maneater_type import ManeaterType


class ManeaterFactory(MonsterAbstractFactory):
    def __init__(self, name, monster_type):
        self.name = name
        self.monster_type = monster_type

    def getMonster(self) -> MonsterAbc:
        return ManeaterBase(self.name)

    def getType(self) -> MonsterType:
        return ManeaterType(self.monster_type)
