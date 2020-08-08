"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from collections import Counter
from functools import partial

# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def sum_of_ns(number, dice):
    return sum(n for n in dice if n == number)


def full_house(dice):
    counter = Counter(dice)
    return sum(dice) if set(counter.values()) == {3, 2} else 0


def four_of_a_kind(dice):
    counter = Counter(dice)
    number, count = counter.most_common()[0]
    return 4 * number if count >= 4 else 0


def little_straight(dice):
    return 30 if set(dice) == {1, 2, 3, 4, 5} else 0


def big_straight(dice):
    return 30 if set(dice) == {2, 3, 4, 5, 6} else 0


def yacht(dice):
    return 50 if len(set(dice)) == 1 else 0


def choice(dice):
    return sum(dice)


def score(dice, category):
    try:
        if category == YACHT:
            return yacht(dice)
        elif category == ONES:
            return sum_of_ns(1, dice)
        elif category == TWOS:
            return sum_of_ns(2, dice)
        elif category == THREES:
            return sum_of_ns(3, dice)
        elif category == FOURS:
            return sum_of_ns(4, dice)
        elif category == FIVES:
            return sum_of_ns(5, dice)
        elif category == SIXES:
            return sum_of_ns(6, dice)
        elif category == FULL_HOUSE:
            return full_house(dice)
        elif category == FOUR_OF_A_KIND:
            return four_of_a_kind(dice)
        elif category == LITTLE_STRAIGHT:
            return little_straight(dice)
        elif category == BIG_STRAIGHT:
            return big_straight(dice)
        elif category == CHOICE:
            return choice(dice)
    except IndexError:
        raise ValueError("No such category.")
