from game_generation.Hero.FactoryAbstract.hero_factory import HeroAbstractFactory
from game_generation.Hero.FactoryUnit.dwarf_ranger import DwarfRanger
from game_generation.Hero.FactoryUnit.dwarf_sorcerer import DwarfSorcerer
from game_generation.Hero.FactoryUnit.dwarf_warrior import DwarfWarrior
from game_generation.Hero.FactoryUnit.dwarf_wizard import DwarfWizard
from game_generation.Hero.FactoryUnit.elf_ranger import ElfRanger
from game_generation.Hero.FactoryUnit.elf_sorcerer import ElfSorcerer
from game_generation.Hero.FactoryUnit.elf_warrior import ElfWarrior
from game_generation.Hero.FactoryUnit.elf_wizard import ElfWizard
from game_generation.Hero.FactoryUnit.gnome_ranger import GnomeRanger
from game_generation.Hero.FactoryUnit.gnome_sorcerer import GnomeSorcerer
from game_generation.Hero.FactoryUnit.gnome_warrior import GnomeWarrior
from game_generation.Hero.FactoryUnit.gnome_wizard import GnomeWizard
from game_generation.Hero.FactoryUnit.halfling_ranger import HalflingRanger
from game_generation.Hero.FactoryUnit.halfling_sorcerer import HalflingSorcerer
from game_generation.Hero.FactoryUnit.halfling_warrior import HalflingWarrior
from game_generation.Hero.FactoryUnit.halfling_wizard import HalflingWizard
from game_generation.Hero.FactoryUnit.human_ranger import HumanRanger
from game_generation.Hero.FactoryUnit.human_sorcerer import HumanSorcerer
from game_generation.Hero.FactoryUnit.human_warrior import HumanWarrior
from game_generation.Hero.FactoryUnit.human_wizard import HumanWizard
from game_generation.Hero.hero_constructor import HeroConstructor


def create_hero(name, race, hero_class) -> HeroAbstractFactory:
    m_name = name.lower().capitalize()
    m_race = race.lower().capitalize()
    m_hero_class = hero_class.lower().capitalize()
    factory_name = m_race + m_hero_class
    factory_dict = {
        "DwarfRanger": DwarfRanger,
        "DwarfSorcerer": DwarfSorcerer,
        "DwarfWarrior": DwarfWarrior,
        "DwarfWizard": DwarfWizard,
        "ElfRanger": ElfRanger,
        "ElfSorcerer": ElfSorcerer,
        "ElfWarrior": ElfWarrior,
        "ElfWizard": ElfWizard,
        "GnomeRanger": GnomeRanger,
        "GnomeSorcerer": GnomeSorcerer,
        "GnomeWarrior": GnomeWarrior,
        "GnomeWizard": GnomeWizard,
        "HalflingRanger": HalflingRanger,
        "HalflingSorcerer": HalflingSorcerer,
        "HalflingWarrior": HalflingWarrior,
        "HalflingWizard": HalflingWizard,
        "HumanRanger": HumanRanger,
        "HumanSorcerer": HumanSorcerer,
        "HumanWarrior": HumanWarrior,
        "HumanWizard": HumanWizard,
    }
    return factory_dict[factory_name](m_name, m_race, m_hero_class)


if __name__ == '__main__':
    name = "Max"
    race = "elf"
    hero_class = "sorcerer"
    unit = create_hero(name, race, hero_class)
    hero = HeroConstructor(unit)
    hero.create_hero()
    attributs = hero.set_attr(4)
    attr = hero.hero_attr()
    hero.make_damage()
    hero.race_skill_1()
    print(attr)

