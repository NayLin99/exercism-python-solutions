import random
import math


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        dice_roll = sorted(
            [random.randint(1, 6)
                for _ in range(4)])
        return sum(dice_roll[1:])


def modifier(value):
    return math.floor((value-10)/2)
