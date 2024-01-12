/**
 * @file
 * @brief Main header for lagrange solver.
 * 
 * @copyright Copyright (C) Victor Baldin, 2024.
 */
#ifndef SOLVER_H_
#define SOLVER_H_

#include <assert.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include <gsl/gsl_poly.h>

/**
 * @brief 
 *
 * @param n_cases A number of points we need for our dependency.
 * @return A packed array of the first 3 L-points coords for each alpha. 
 */
double* solve_lagrange_problem(size_t n_cases);

/**
 * 
 */
void print_lagrange_coords_to_csv(const double solutions[], size_t n_cases);

#endif // SOLVER_H_
