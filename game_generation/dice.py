import random


class Dice:
    def trow_dice(self, type_dice, number_of_dice):
        dice_t = list(type_dice)
        dice_t.remove("d")
        dice = int("".join(dice_t))
        match number_of_dice:
            case "1":
                result = [random.randint(1, dice)]
                return result
            case "2":
                result = [random.randint(1, dice), random.randint(1, dice)]
                return result
            case "3":
                result = [random.randint(1, dice), random.randint(1, dice), random.randint(1, dice)]
                return result

# dice = Dice()
# result = dice.trow_dice("d10", "3")
# print(result)
