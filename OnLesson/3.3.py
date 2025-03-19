def f(x):
    a = x + x # 2
    b = a + a # 4
    c = b + b# 8
    c1 = x - c
    d = c - c1
    return d

print(f(1))
print(f(100))