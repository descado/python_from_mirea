import math


def main(x):
    if x < -4:
        return 79 * math.pow(x, 3)
    if x >= -4 and x < 93:
        return 86 * math.pow(x, 5)
    if x >= 93 and x < 167:
        return int(math.pow(x, 7) / 55)
    if x >= 167:
        a = 42 * math.pow(x, 6) + math.pow(x, 2) / 77
        b = 95 * math.pow(math.ceil(x * x - 77 - x), 5)
        return a + b