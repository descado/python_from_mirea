import math


def main(y):
    aboba1 = (79 * y - math.pow(y, 7) / 6)
    aboba2 = (1 - math.pow(math.cos(y - math.pow(y, 3)), 4) / 6)
    return aboba1 / aboba2 + y / 22 + y * y