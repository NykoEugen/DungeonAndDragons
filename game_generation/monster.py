import random

from game_generation.work_with_json import WorkWithJson


class Monster:
    def get_monster(self, level):
        adjectives = ["Horrible", "Deadly", "Ferocious", "Bloody", "Nasty"]
        nouns = ["Hydra", "Mortar", "Goblin", "Witch", "Wanderer", "Dragon"]
        monster_name = random.choice(adjectives) + " " + random.choice(nouns)
        monster_type_lst = ["common", "uncommon", "rare", "mythical", "legendary"]
        weights = [0.5, 0.3, 0.3, 0.05, 0.01]
        monster_type = random.choices(monster_type_lst, weights=weights)[0]

        health = random.randint(60, 100) * level
        damage = random.randint(2, 15) * level
        match monster_type:
            case "common":
                reward_xp = round(random.randint(1, 3) * level)
                reward_gold = 1 * level
            case "uncommon":
                reward_xp = round(random.randint(1, 3) * level * 1.1, 1)
                reward_gold = 1 * level * 1.1
            case "rare":
                reward_xp = round(random.randint(1, 3) * level * 1.3, 1)
                reward_gold = 1 * level * 1.3
            case "mythical":
                reward_xp = round(random.randint(1, 3) * level * 1.5)
                reward_gold = 1 * level * 1.5
            case "legendary":
                reward_xp = round(random.randint(1, 3) * level * 1.8)
                reward_gold = 1 * level * 1.8

        unit = {"name": monster_name,
                "type": monster_type,
                "level": level,
                "health": health,
                "damage": damage,
                "reward_xp": reward_xp,
                "reward_gold": reward_gold}
        filename = "Monsters.json"
        json = WorkWithJson()
        json.load_to_json(filename, unit)
        return unit


# unit = Monster()
# unit.get_monster(2)