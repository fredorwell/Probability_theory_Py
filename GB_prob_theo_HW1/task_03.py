# В ящике имеется 15 деталей, из которых 9 окрашены.
# Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

import math


def Comb(a, b):
    return int(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))


def Prob(a, b):
    return round(a / b, 4)


m = Comb(9, 3)
n = Comb(15, 3)
print(f'Вероятность что 3 из 3х деталей окрашены: {Prob(m, n)}')
