from math import ceil, floor

def main(omega):
    # Вычисляем множество Theta
    theta = {ceil(omega_i // 3) for omega_i in omega if -59 < omega_i < 30}
    
    # Вычисляем множество Z
    z = {theta_i - 7 * theta_i for theta_i in theta if theta_i >= -37}
    
    # Вычисляем множество H
    h = omega.union(theta)
    
    # Вычисляем множество M
    m = {floor(eta // 5) + ceil(eta // 6) for eta in h if eta < -5}
    
    # Вычисляем множество Upsilon
    upsilon = z.union(m)
    
    # Вычисляем delta
    delta = len(m) + sum(v % 2 for v in upsilon)
    
    return delta

# Примеры использования
print(main({-94, 38, 7, 9, 12, -14, -45, -69, -33}))  # Ожидаемый результат: 8
print(main({64, -93, 5, -26, -57, 83, 52, 91, 93, -33}))  # Ожидаемый результат: 10