# A simple script for Lagrange points calculation.
#
# Copyright (C) Victor Baldin, 2024.

import math
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# Выбирает из массива корней действительный корень, лежащий в [min, max].
def find_real_root(roots, rmin, rmax):
    for i in range(0, roots.__len__()):
        if math.isclose(roots[i].imag, 0) and rmin <= roots[i].real and roots[i].real <= rmax:
            return roots[i].real
    return np.nan

# Нахоит корни уравнения для данного значения alpha
def lagrange_solve(alpha):
    roots = [0.0] * 3
    coeff = [
        [1, 3 - alpha, 3 - 2 * alpha,     alpha,  2 * alpha,  alpha],
        [1, 3 - alpha, 3 - 2 * alpha,    -alpha, -2 * alpha, -alpha],
        [1, 3 - alpha, 3 - 2 * alpha, 2 - alpha,  2 * alpha,  alpha],
    ]
    rmin = [-1,      0, -np.inf]
    rmax = [ 0, np.inf,      -1]
    for i in range(0, coeff.__len__()):
        roots[i] = find_real_root(np.roots(coeff[i]), rmin[i], rmax[i]) + 1.0 - alpha
    return roots

# Вычисляем положения точек Лагранжа с шагом 0.001, вывод перенаправляем в 
# файл. 
print('alpha,L1,L2,L3')

alpha = 0.001
i = 0
roots = []
while (alpha < 1.0):
    roots.append(lagrange_solve(alpha))
    print('{0:.3f},{1},{2},{3}'.format(alpha, roots[i][0], roots[i][1], 
                                       roots[i][2]))
    alpha += 0.001
    i += 1

# Графики
alpha = [(1 + i) / 1000 for i in range(roots.__len__())]

plt.figure()
for j in range(3):
    plt.scatter(alpha, [roots[i][j] for i in range(roots.__len__())]) 

plt.grid() 
plt.savefig('plots/all.pgf')
