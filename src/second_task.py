import numpy as np

X = np.genfromtxt("samples/r2z2.csv", delimiter=",", skip_header=1)

n = len(X)
X_sorted = np.sort(X)

lambda_param = 2
F_theoretical = 1 - np.exp(-lambda_param * X_sorted)
F_empirical = np.arange(1, n+1) / n

def D_crit(alpha, n):
    return np.sqrt(-np.log(alpha / 2) / (2 * n))

D = np.max(np.abs(F_empirical - F_theoretical))
alpha = 0.01
D_alpha = D_crit(alpha, n)

print("Статистика D =", D)
print("Критическое значение D_alpha =", D_alpha)

if D > D_alpha:
    print("Вывод: H0 отвергается. Выборка не соответствует распределению E(λ=2)")
else:
    print("Вывод: нет оснований отвергать H0. Выборка согласуется с E(λ=2)")
