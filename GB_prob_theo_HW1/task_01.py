# Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести.
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.

import math


def Comb(a, b):
    return int(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))


def Prob(a, b):
    return round(a / b, 4)


m = Comb(13, 4)
n = Comb(52, 4)
print(f'Вероятность того что все крести {Prob(m, n)}')
m = Comb(4, 1) * Comb(48, 3) + Comb(4, 2) * Comb(48, 2) + Comb(4, 3) * Comb(48, 1) + 1
print(f'Вероятность того что хотя бы один туз {Prob(m, n)}')
