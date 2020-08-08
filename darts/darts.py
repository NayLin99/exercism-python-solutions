import math


def score(x, y):
    distance = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    if distance <= 1:
        return 10
    elif distance > 1 and distance <= 5:
        return 5
    elif distance > 5 and distance <= 10:
        return 1
    else:
        return 0
