from math import pow, log10


def main(n, cache={0: 0.42, 1: 0.79}):
    if n in cache:
        return cache[n]

    a = pow(log10(pow(main(n - 2, cache), 2) / 64), 3) / 41
    b = pow(main(n - 2, cache), 2)
    c = main(n - 1, cache) / 47
    result = a + b + c
    cache[n] = result
    return result
