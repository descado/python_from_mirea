import math


def main(z, y, x):
    n = len(x)
    total = 0
    for i in range(1, n + 1):
        z_index = math.ceil(i / 4)
        term = 35 * x[i - 1]**2 - 15 * z[z_index - 1] - 47 * y[n - i]**3
        total += term ** 3
    return 78 * total

