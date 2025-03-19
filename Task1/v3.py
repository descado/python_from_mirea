from math import pow, cos


def main(y):
    aboba1 = (79 * y - pow(y, 7) / 6)
    aboba2 = (1 - pow(cos(y - pow(y, 3)), 4) / 6)
    return (79 * y - pow(y, 7) / 6) / (1 - pow(cos(y - pow(y, 3)), 4) / 6) + y / 22 + y * y