import numpy as np

import math

data = np.genfromtxt("samples/r2z1.csv", delimiter=",", skip_header=1)

X = data[:, 0]
Y = data[:, 1]

D = Y - X
D_nonzero = D[D != 0]
n = len(D_nonzero)

S = np.sum(D_nonzero > 0)

alpha = 0.025


def nCk(n, k):
    return math.comb(n, k)


def binom_pmf(k, n, p=0.5):
    return nCk(n, k) * (p**k) * ((1 - p)**(n - k))


def binom_sf(k, n, p=0.5):
    return sum(binom_pmf(i, n, p) for i in range(k, n + 1))


S_crit = None
for k in range(n + 1):
    if binom_sf(k, n, 0.5) <= alpha:
        S_crit = k
        break

p = binom_sf(S, n, 0.5)


print("N =", n)
print("Число положительных знаков S =", S)
print("Критическое значение S_crit =", S_crit)
print("p =", p)

if S >= S_crit:
    print("\nВывод: отвергаем H0. Есть статистически значимое увеличение.")
else:
    print("\nВывод: нет оснований отвергнуть H0. Увеличение статистически не подтверждено.")
