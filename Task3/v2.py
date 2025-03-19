from math import pow


def main(n, b, a):
    arr = []
    for c in range(1, a + 1):
        for j in range(1, b + 1):
            for i in range(1, n + 1):
                x1 = pow(j, 4) - 72 * pow(i, 3)
                x2 = pow(84 * pow(c, 3) + j, 7) / 28
                arr.append(x1 - x2)
    return sum(arr)
