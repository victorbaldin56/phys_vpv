# A simple script for Lagrange points calculation.
#
# Copyright (C) Victor Baldin, 2024.

import numpy as np
import matplotlib as plt

# Выбирает из массива корней действительный корень, лежащий в [min, max].
def find_real_root(roots, min, max):
    for i in range(0, roots.__len__()):
        if roots[i].imag == 0 and min <= roots[i].real and roots[i] <= max:
            return roots[i].real

# Нахоит корни уравнения для данного значения alpha
def lagrange_solve(alpha):
    roots = [0.0] * 3
    coeff = [
        [1, 3 - alpha, 3 - 2 * alpha,    -alpha, 0,  alpha],
        [1, 3 - alpha, 3 - 2 * alpha,     alpha, 0, -alpha],
        [1, 3 - alpha, 3 - 2 * alpha, 2 - alpha, 0,  alpha],
    ]
    rmin = [-1.0, 0.0   , -np.inf]
    rmax = [ 0.0, np.inf,    -1.0]
    for i in range(0, coeff.__len__()):
        roots[i] = find_real_root(np.roots(coeff[i]), rmin[i], rmax[i])
    return roots

# Вычисляем положения точек Лагранжа с шагом 0.001, вывод перенаправляем в 
# файл. 
print('alpha,u1,u2,u3')
alpha = 0.001
while (alpha < 1.0):
    roots = lagrange_solve(alpha)
    print('{0:.3f},{1},{2},{3}'.format(alpha, roots[0], roots[1], roots[2]))
    alpha += 0.001
