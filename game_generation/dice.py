import random


class Dice:
    def throw_dice(self, type_dice, number_of_dice):
        dice_t = list(type_dice)
        dice_t.remove("d")
        dice = int("".join(dice_t))
        match number_of_dice:
            case "1":
                dice_point = [random.randint(1, dice)]
                print(f"Dice: {dice_point[0]}")
            case "2":
                dice_point = [random.randint(1, dice), random.randint(1, dice)]
                print(f"Dice: {dice_point[0]}, {dice_point[1]}")
            case "3":
                dice_point = [random.randint(1, dice), random.randint(1, dice), random.randint(1, dice)]
                print(f"Dice: {dice_point[0]}, {dice_point[1]}, {dice_point[2]}")
        result = sum(dice_point)
        print(f"Result points is: {result}")
        return result


# dice = Dice()
# result = dice.trow_dice("d6", "2")
# print(result)
