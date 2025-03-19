from math import pow, ceil


def main(x):
    if x < -4:
        a = 79 * pow(x, 3)
        return a
    elif x >= -4 and x < 93:
        a = 86 * pow(x, 5)
        return a
    elif x >= 93 and x < 167:
        a = int(pow(x, 7) / 55)
        return a
    else:
        a = 42 * pow(x, 6) + pow(x, 2) / 77
        b = 95 * pow(ceil(x * x - 77 - x), 5)
        return a + b