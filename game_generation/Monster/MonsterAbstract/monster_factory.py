from abc import ABC, abstractmethod

from game_generation.Monster.MonsterAbstract.monster_abs import MonsterAbc
from game_generation.Monster.MonsterAbstract.monster_type import MonsterType


class MonsterAbstractFactory(ABC):
    @abstractmethod
    def getMonster(self) -> MonsterAbc: pass

    @abstractmethod
    def getType(self) -> MonsterType: pass
