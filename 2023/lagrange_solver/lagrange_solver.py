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

# Вычисляем положения точек Лагранжа с шагом 0.001. 
alpha = [(i + 1) / 10000 for i in range(100)] + [i / 1000 for i in range(10, 1000)]

roots = []
for i in range(alpha.__len__()):
    roots.append(lagrange_solve(alpha[i]))

colors = ['blue', 'red', 'green']
# Графики
plt.figure()
for j in range(3):
    plt.scatter(alpha, [roots[i][j] for i in range(roots.__len__())], s=0.5,
                label='$L_{0}$'.format(j + 1), color=colors[j]) 

plt.xlabel('$\\alpha$')
plt.ylabel('$x/R$')
plt.grid() 
plt.legend(markerscale=2)
plt.savefig('plots/all.pgf')

# Графики с аппроксимациями.

x = np.linspace(0.0, 1.0, 200)
fig, axs = plt.subplots(3)
for j in range(3):
    axs[j].scatter(alpha, [roots[i][j] for i in range(roots.__len__())], s=0.5, 
                   color=colors[j])
    axs[j].grid()
    axs[j].set_title('$L_{0}$'.format(j + 1))

axs[0].plot(x, 1 - (x / 3)**(1 / 3), color='orange', 
            label='$\\frac{{x}}{{R}}=1-\\left(\\frac{{\\alpha}}{{3}}\\right)^{{1/3}}$')
axs[1].plot(x, 1 + (x / 3)**(1 / 3), color='orange', 
            label='$\\frac{{x}}{{R}}=1+\\left(\\frac{{\\alpha}}{{3}}\\right)^{{1/3}}$')
axs[2].plot(x, -1 - (5 / 12) * x, color='orange', 
            label='$\\frac{{x}}{{R}}=-\\left(1+\\frac{{5}}{{12}}\\alpha\\right)$')

for j in range(3):
    axs[j].legend()

plt.tight_layout()

plt.xlabel('$\\alpha$')
plt.ylabel('$x/R')
plt.savefig('plots/subplots.pgf')

fig, axs = plt.subplots(3)

# Ошибки аппроксимации
NUM_LOW_VALUES = 300
NUM_VERY_LOW_VALUES = 200

errors = [[]] * 3
errors[0] = [abs((roots[i][0] - 1 + (alpha[i] / 3)**(1 / 3)) / roots[i][0]) 
                   for i in range(roots.__len__())]
errors[1] = [abs((roots[i][1] - 1 - (alpha[i] / 3)**(1 / 3)) / roots[i][1])
                       for i in range(roots.__len__())]
errors[2] = [abs((roots[i][2] + 1 + 5 / 12 * alpha[i]) / roots[i][2])
                       for i in range(roots.__len__())]

for j in range(3):
    axs[j].scatter(alpha[:NUM_VERY_LOW_VALUES], errors[j][:NUM_VERY_LOW_VALUES], s=1.0)
    axs[j].grid()
    axs[j].set_title('$L_{0}'.format(j + 1))

plt.tight_layout()

plt.xlabel('$\\alpha$')
plt.ylabel('$\\varepsilon$')
plt.savefig('plots/errors.pgf')

plt.figure()
for j in range(3):
    plt.scatter(alpha[:NUM_LOW_VALUES], errors[j][:NUM_LOW_VALUES], 
                s=0.5, label='$L_{0}'.format(j + 1))

plt.grid()
plt.xlabel('$\\alpha$')
plt.ylabel('$\\varepsilon$')
plt.legend(markerscale=2)
plt.savefig('plots/errors_all.pgf')

# Пишем в таблицу.
print('alpha,L1,L2,L3,e1,e2,e3')

for j in range(roots.__len__()):
    print('{0},{1},{2},{3},{4},{5},{6}'.format(alpha[j], 
                                               roots[j][0], roots[j][1], roots[j][2],
                                               errors[0][j], errors[1][j], errors[2][j]))
