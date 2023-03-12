# В лотерее 100 билетов. Из них 2 выигрышных.
# Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?


import math


def Comb(a, b):
    return int(math.factorial(a) / (math.factorial(b) * math.factorial(a - b)))


def Prob(a, b):
    return round(a / b, 4)


m = 1
n = Comb(100, 2)
print(f'Вероятность что 2 их 100 билетов выигрышные: {Prob(m, n)}')