from math import pow, log10


def main(n):
    if n == 0:
        return 0.42
    if n == 1:
        return 0.79
    a = pow(log10(pow(main(n - 2), 2) / 64), 3) / 41
    b = pow(main(n - 2), 2)
    c = main(n - 1) / 47
    return a + b + c